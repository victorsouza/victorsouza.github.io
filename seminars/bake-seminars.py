###########################################################
### Created by Victor Souza                             ###
###########################################################
### The purpuse of this file is to fetch a google sheet
### with seminar information and bakes an html file
### with the seminar website.
### The sheet is assumed to be of a very particular format.

import sys, argparse
import datetime, html, pyexcel, urllib.request

###########################################################
### Basic command line arguments
###########################################################

parser = argparse.ArgumentParser(description="Bake seminar pages")

parser.add_argument("-l", "--local", action="store_true", help="Use local file")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")

args = parser.parse_args()

###########################################################
### Some basic configurations
###########################################################

# File handlers
OUTPUT_HTML_FILE = "index.html"
INPUT_FILE = "seminars.ods"
CSS_FILE = "style.css"

MISSING_TITLE = "(Title to be announced)"
EMPTY_UPCOMING = "<p>No upcoming events currently determined.</p>"

# Whether abstracts are expanded by default on Upcoming or Archive sections
EXPAND_ABSTRACT_UPCOMING = True
EXPAND_ABSTRACT_ARCHIVE = False

# Whether to show seminar series
SHOW_SEMINAR_SERIES = False

# Text snippets
PAGE_TITLE = "Cornell Probability Seminar"
PAGE_HEADER = "Cornell Probability Seminar"
DESCRIPTION = """
<p>
Welcome to the experimental and yet unofficial page for the Probability Seminars of the <a href="https://math.cornell.edu">Department of Mathematics at Cornell</a>. The current organizers of the seminar are <a href="https://elalaoui.stat.cornell.edu/">Ahmed El Alaoui</a>, <a href="https://lionellevine.github.io/">Lionel Levine</a>, <a href="https://math.cornell.edu/philippe-sosoe">Philippe Sosoe</a>, and <a href="https://souza.id/">Victor Souza</a>.
</p>
"""

ABOUT = """
<p>
Here we can add some historical remarks about the seminar, like when it was initiated, by whom, and the people that organised it in the past.
</p>
"""

# Basic Katex configuration
# Can add more LaTeX macros if needed
KATEX = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.css" integrity="sha384-vKruj+a13U8yHIkAyGgK1J3ArTLzrFGBbBc0tDp4ad/EyewESeXE/Iv67Aj8gKZ0" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.js" integrity="sha384-PwRUT/YqbnEjkZO0zZxNqcxACrXe+j766U2amXcgMg5457rve2Y7I6ZJSm2A0mS4" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
          {left: '$$', right: '$$', display: true},
          {left: '$', right: '$', display: false},
      ],
      macros: {
        "\\eps": "\\varepsilon}",
      },
      throwOnError : false
    });
  });
</script>
"""

###########################################################
### Loading the spreadsheet
###########################################################

# This function grabs the google sheet from the url and saves it at the path
def gdrive_to_file(url, path):
  try:
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
      content = response.read()
      with open(path, "wb") as f:
        f.write(content)
    if args.verbose:
      print(f"Google Sheet succesfully loaded to {path}")
  except urllib.error.URLError as e:
    print(f"Error accessing URL: {e.reason}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Load the seminar google sheet into 'seminars.ods'
## Note the format=ods at the end of the url
if not args.local:
  gdrive_to_file("https://docs.google.com/spreadsheets/d/17MEK8E4jr7DEIzBiGPMltjrC-sTcJylbC6K5TdkkvfM/export?format=ods", "seminars.ods")

###########################################################
### Parsing the spreadsheet
###########################################################

ARCHIVE = {}
UPCOMING = []

# Determine the academic year from a date
## For instance, January of 2025 maps to 2024 and December 2023 maps to 2023
def academic_year(date):
  year = date.year
  if date.month <= 5:
    year -= 1
  return year

# Read the spreadsheet into a records buffer
try:
  #records = pyexcel.get_records(file_name=INPUT_FILE)
  books = pyexcel.get_book(file_name=INPUT_FILE)
  records = []
  for sheet in reversed(books):
      headers = sheet.row[0]
      for row in sheet.row[1:]:
          r = dict(zip(headers, row))
          r["Book"] = sheet.name
          records.append(r)
except Exception as e:
  print(f"An unexpected error occurred: {e}")
  sys.exit()

# Remove records that do not have a date AND do not have a title
records = [r for r in records if r["Date"] != "" or r["Title"] != ""]

# Sort by date
records.sort(key=lambda r: r["Date"] or datetime.date.max, reverse=True)

today = datetime.date.today()

n = 0
for r in records:
  n += 1
  # Handle Title
  if r["Title"]:
    title_text = r["Title"]
  else:
    title_text = MISSING_TITLE
  
  # Handle Affiliation
  if r["Affiliation"]:
    affiliation_text = f"({r["Affiliation"]})"
  else:
    affiliation_text = "" 

  # Handle Date
  date = r["Date"]
  if isinstance(date, datetime.date):
    if r["Date Unknown"]:
      date_text = date.strftime("%B %Y")
    else:
      date_text = date.strftime("%A, %-d")
      day = date.day
      if 4 <= day <= 20 or 24 <= day <= 30:
        date_text += "th"
      else:
        date_text += ["st", "nd", "rd"][day % 10 - 1]
      date_text += date.strftime(" of %B %Y")
  else:
    date_text = date
  
  # Handle wether abstract should be open by default 
  show = ""
  if date >= today:
    show = "open" if EXPAND_ABSTRACT_UPCOMING else ""
  else:
    show = "open" if EXPAND_ABSTRACT_ARCHIVE else ""
  
  # Handle Time
  time = r["Time"]
  if isinstance(time, datetime.time):
    time_text = time.strftime("%-H:%M")
  else:
    time_text = time
  
  # Handle Speaker Name and URL
  if r["Speaker URL"]:
    speaker_text = f'<a href="{r["Speaker URL"]}">{r["Speaker"]}</a>'
  else:
    speaker_text = r["Speaker"]

  # Tokenize the Series
  series_text = ""
  for s in r["Series"].split(", "):
    series_text += f"<series>{s}</series>"
  
  # Possibly empty abstract
  abstract_row = ""
  if r["Abstract"] != "":
    abstract_row = f"""
  <abstract_row>
    <input type="checkbox" class="abs" id="abs{n}" {show}>
    <label for="abs{n}" class="abs">Abstract</label> 
    <abstract>{r["Abstract"]}
    </abstract>
  </abstract_row>
  """

  if r["Abstract"] != "":
    abstract_row = f"""
  <abstract_row>
  <details {show}>
    <summary>Abstract</summary>
    <abstract>
    {r["Abstract"]}
    </abstract>
  </details>
  </abstract_row>
  """

  # Put it all together
  SEMINAR = f"""
<seminar>
  <title_row>{title_text}</title_row>
  <speaker_row>
    <speaker>{speaker_text}</speaker>
    <affiliation>{affiliation_text}</affiliation>
  </speaker_row>
  <venue_row>
    <venue>
      <date>{date_text}</date>
      {f"at <time>{time_text}</time>" if time else ""}
      {f"in <location>{r["Room"]}</location>" if r["Room"] else ""}
    </venue>
    {f'<series_row>{series_text}</series_row>' if SHOW_SEMINAR_SERIES else ''}
  </venue_row>
  {abstract_row}
</seminar>
"""

  # Add string to UPCOMING or ARCHIVE based on date
  if date >= today:
    UPCOMING.append(SEMINAR)
  else:
    ARCHIVE.setdefault(academic_year(date), []).append(SEMINAR)
  
  ## Print some information for procesing
  if args.verbose:
    print(f"{n  :3} -> [{r["Date"]}] {r["Speaker"]} - '{r["Title"]}'")


###########################################################
### Assembling the HTML file
###########################################################

# The HTML string contains the page
HTML = ""

# Append HTML header and description
HTML += f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href='https://fonts.googleapis.com/css?family=Roboto Condensed' rel='stylesheet'>
<link href="https://cdn.jsdelivr.net/gh/vsalvino/computer-modern@main/fonts/serif.css" rel="stylesheet">
{KATEX}
<title>{PAGE_TITLE}</title>
<link rel="stylesheet" href="{CSS_FILE}">
</head>
<body>
<header>
  <pagetitle>{PAGE_HEADER}</pagetitle>
  <logo></logo>
</header>
<intro>
{DESCRIPTION}
</intro>
"""

# Append About section
HTML += f"""
<section>
<section_header>About</section_header>
{ABOUT}
</section>
"""

# Append Upcoming Seminars
HTML += f"""
<section>
<section_header>Upcoming Seminars</section_header>
{"\n".join(reversed(UPCOMING)) if UPCOMING else EMPTY_UPCOMING}
</section>
"""

# Apend Archive
HTML += f"""
<archive>
"""

# Append each year separately
for year in sorted(ARCHIVE.keys(), reverse = True):
  if year == 1999:
    daterange = "1999 &mdash; 2000"
  else:
    daterange = f"{year} &mdash; {(year+1)%100:02}"

  HTML += f"""
<details {"open" if academic_year(today) == year else ""}>
<summary>Archive of {daterange}</summary>
{"\n".join(ARCHIVE[year])}
</details>
"""

# Append end of Archive
HTML += """
</archive>
</section>
"""

# Append footer
HTML += """
<footer>
  Page designed by <a href="https://souza.id/">Victor Souza</a>
</footer>
"""

# Append end of HTML
HTML += """
</body>
</html>
"""

# Write HMTML to output file
with open(OUTPUT_HTML_FILE, "w", encoding="utf-8") as f:
  f.write(HTML)