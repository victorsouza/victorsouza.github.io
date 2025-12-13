import tomllib
from datetime import date

KATEX = r"""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.css"
  integrity="sha384-vKruj+a13U8yHIkAyGgK1J3ArTLzrFGBbBc0tDp4ad/EyewESeXE/Iv67Aj8gKZ0"
  crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.js"
  integrity="sha384-PwRUT/YqbnEjkZO0zZxNqcxACrXe+j766U2amXcgMg5457rve2Y7I6ZJSm2A0mS4"
  crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/contrib/auto-render.min.js"
  integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05"
  crossorigin="anonymous"></script>
<script>
document.addEventListener("DOMContentLoaded", function() {
  renderMathInElement(document.body, {
  delimiters: [
    {left: '$$', right: '$$', display: true},
    {left: '$', right: '$', display: false},
    {left: '\\(', right: '\\)', display: false},
    {left: '\\[', right: '\\]', display: true}
  ],
  macros: {
    "\\AA": "\\mathbb{A}", "\\BB": "\\mathbb{B}", "\\CC": "\\mathbb{C}", "\\DD": "\\mathbb{D}",
    "\\EE": "\\mathbb{E}", "\\FF": "\\mathbb{F}", "\\GG": "\\mathbb{G}", "\\HH": "\\mathbb{H}",
    "\\II": "\\mathbb{I}", "\\JJ": "\\mathbb{J}", "\\KK": "\\mathbb{K}", "\\LL": "\\mathbb{L}",
    "\\MM": "\\mathbb{M}", "\\NN": "\\mathbb{N}", "\\OO": "\\mathbb{O}", "\\PP": "\\mathbb{P}",
    "\\QQ": "\\mathbb{Q}", "\\RR": "\\mathbb{R}", "\\SS": "\\mathbb{S}", "\\TT": "\\mathbb{T}",
    "\\UU": "\\mathbb{U}", "\\VV": "\\mathbb{V}", "\\WW": "\\mathbb{W}", "\\XX": "\\mathbb{X}",
    "\\YY": "\\mathbb{Y}", "\\ZZ": "\\mathbb{Z}",
    "\\cA": "\\mathcal{A}", "\\cB": "\\mathcal{B}", "\\cC": "\\mathcal{C}", "\\cD": "\\mathcal{D}",
    "\\cE": "\\mathcal{E}", "\\cF": "\\mathcal{F}", "\\cG": "\\mathcal{G}", "\\cH": "\\mathcal{H}",
    "\\cI": "\\mathcal{I}", "\\cJ": "\\mathcal{J}", "\\cK": "\\mathcal{K}", "\\cL": "\\mathcal{L}",
    "\\cM": "\\mathcal{M}", "\\cN": "\\mathcal{N}", "\\cO": "\\mathcal{O}", "\\cP": "\\mathcal{P}",
    "\\cQ": "\\mathcal{Q}", "\\cR": "\\mathcal{R}", "\\cS": "\\mathcal{S}", "\\cT": "\\mathcal{T}",
    "\\cU": "\\mathcal{U}", "\\cV": "\\mathcal{V}", "\\cW": "\\mathcal{W}", "\\cX": "\\mathcal{X}",
    "\\cY": "\\mathcal{Y}", "\\cZ": "\\mathcal{Z}",
    "\\bfA": "\\mathbf{A}", "\\bfB": "\\mathbf{B}", "\\bfC": "\\mathbf{C}", "\\bfD": "\\mathbf{D}",
    "\\bfE": "\\mathbf{E}", "\\bfF": "\\mathbf{F}", "\\bfG": "\\mathbf{G}", "\\bfH": "\\mathbf{H}",
    "\\bfI": "\\mathbf{I}", "\\bfJ": "\\mathbf{J}", "\\bfK": "\\mathbf{K}", "\\bfL": "\\mathbf{L}",
    "\\bfM": "\\mathbf{M}", "\\bfN": "\\mathbf{N}", "\\bfO": "\\mathbf{O}", "\\bfP": "\\mathbf{P}",
    "\\bfQ": "\\mathbf{Q}", "\\bfR": "\\mathbf{R}", "\\bfS": "\\mathbf{S}", "\\bfT": "\\mathbf{T}",
    "\\bfU": "\\mathbf{U}", "\\bfV": "\\mathbf{V}", "\\bfW": "\\mathbf{W}", "\\bfX": "\\mathbf{X}",
    "\\bfY": "\\mathbf{Y}", "\\bfZ": "\\mathbf{Z}",
    "\\bfa": "\\mathbf{a}", "\\bfb": "\\mathbf{b}", "\\bfc": "\\mathbf{c}", "\\bfd": "\\mathbf{d}",
    "\\bfe": "\\mathbf{e}", "\\bff": "\\mathbf{f}", "\\bfg": "\\mathbf{g}", "\\bfh": "\\mathbf{h}",
    "\\bfi": "\\mathbf{i}", "\\bfj": "\\mathbf{j}", "\\bfk": "\\mathbf{k}", "\\bfl": "\\mathbf{l}",
    "\\bfm": "\\mathbf{m}", "\\bfn": "\\mathbf{n}", "\\bfo": "\\mathbf{o}", "\\bfp": "\\mathbf{p}",
    "\\bfq": "\\mathbf{q}", "\\bfr": "\\mathbf{r}", "\\bfs": "\\mathbf{s}", "\\bft": "\\mathbf{t}",
    "\\bfu": "\\mathbf{u}", "\\bfv": "\\mathbf{v}", "\\bfw": "\\mathbf{w}", "\\bfx": "\\mathbf{x}",
    "\\bfy": "\\mathbf{y}", "\\bfz": "\\mathbf{z}",
    "\\GL": "\\operatorname{GL}",
    "\\sign": "\\operatorname{sign}",
    "\\chara": "\\operatorname{char}",
    "\\Sym": "\\operatorname{Sym}",
    "\\abs": "#1| #2 #1|",
    "\\card": "#1| #2 #1|",
    "\\p": "#1\\lparen #2 #1\\rparen",
    "\\set": "#1\\{ #2 #1\\}",
    "\\st": "\\,\\colon",
    "\\from": "\\,\\colon",
    "\\defined": "\\coloneqq",
    "\\defines": "\\eqqcolon",
    },
    throwOnError : false
    });
  });
</script>
"""

SVG = """
<svg display="none">
<symbol width="28" height="32" viewBox="0 0 32 32" id="arxiv">
  <path d="M27.599 20.536l-2.525-6.619h1.885l1.848 4.776 1.839-4.776h1.281l-2.557
  6.619zM21.729 12.803v-1.496h1.787v1.496zM21.729 20.541v-6.624h1.787v6.619zM12.443
  20.541l2.864-4.401-2.733-4.531h2.172l1.817 3.005 1.968-3.005h1.496l-2.729 4.208
  2.839 4.713h-2.167l-1.933-3.197-2.072 3.197h-1.521zM7.984
  20.541v-6.624h1.781v1.249c0.459-0.932 1.167-1.401 2.115-1.401 0.109 0 0.224 0.011
  0.328 0.032v1.593c-0.224-0.084-0.463-0.131-0.703-0.136-0.719 0-1.292 0.355-1.74
  1.068v4.219zM3.948 19.823c-0.593 0.579-1.229 0.871-1.917 0.871-0.525
  0.015-1.031-0.172-1.416-0.532-0.364-0.359-0.557-0.859-0.541-1.375-0.027-0.677
  0.307-1.323 0.88-1.693 0.583-0.396 1.421-0.599
  2.511-0.599h0.473v-0.604c0-0.683-0.391-1.027-1.172-1.027-0.744
  0.016-1.473 0.219-2.115 0.589v-1.229c0.765-0.303 1.584-0.459 2.412-0.459 1.735
  0 2.599 0.688 2.599 2.063v2.943c0 0.521 0.161 0.776 0.5 0.776 0.079 0 0.156-0.011
  0.235-0.025l0.041 1c-0.323 0.104-0.661 0.161-1 0.172-0.74
  0-1.203-0.287-1.416-0.865h-0.068zM3.948 18.864v-1.343h-0.427c-1.157 0-1.729
  0.364-1.729 1.083-0.011 0.479 0.375 0.865 0.848 0.865 0.443 0.004 0.865-0.199
  1.308-0.605z"/>
</symbol>

<symbol width="32" height="32" viewBox="0 0 32 32" id="github">
  <path d="M16 0.396c-8.839 0-16 7.167-16 16 0 7.073 4.584 13.068 10.937 15.183 0.803
  0.151 1.093-0.344 1.093-0.772 0-0.38-0.009-1.385-0.015-2.719-4.453
  0.964-5.391-2.151-5.391-2.151-0.729-1.844-1.781-2.339-1.781-2.339-1.448-0.989
  0.115-0.968 0.115-0.968 1.604 0.109 2.448 1.645 2.448 1.645 1.427 2.448 3.744
  1.74 4.661 1.328 0.14-1.031 0.557-1.74 1.011-2.135-3.552-0.401-7.287-1.776-7.287-7.907
  0-1.751 0.62-3.177 1.645-4.297-0.177-0.401-0.719-2.031 0.141-4.235 0 0 1.339-0.427 4.4
  1.641 1.281-0.355 2.641-0.532 4-0.541 1.36 0.009 2.719 0.187 4 0.541 3.043-2.068
  4.381-1.641 4.381-1.641 0.859 2.204 0.317 3.833 0.161 4.235 1.015 1.12 1.635 2.547
  1.635 4.297 0 6.145-3.74 7.5-7.296 7.891 0.556 0.479 1.077 1.464 1.077 2.959 0
  2.14-0.020 3.864-0.020 4.385 0 0.416 0.28 0.916 1.104 0.755 6.4-2.093 10.979-8.093
  10.979-15.156 0-8.833-7.161-16-16-16z"/>
</symbol>

<symbol width="32" height="32" viewBox="0 0 512 512" id="lattes">
  <path id="path2" d="M 97.871854,434.73261 C 51.534463,339.78442 23.965602,282.44369
  23.965602,281.02029 c 0,-2.32214 2.831558,-1.99974 30.672084,3.45957 48.965204,9.61389
  75.126384,12.32631 118.735104,12.34258 57.69707,0.0159 104.6807,-9.1222
  141.18473,-27.4842 19.31194,-9.71476 30.92555,-18.32755 40.43708,-29.99337
  11.716,-14.37824 15.47977,-24.28004 15.61512,-40.94646 0.11867,-15.85237
  -2.01801,-24.21167 -11.19035,-43.60874 -3.62892,-7.66433 -6.8168,-16.46265
  -7.12098,-19.54964 -0.47493,-4.96814 -0.0684,-5.68084 3.59445,-6.10361
  8.00292,-0.94846 47.50732,37.40224 62.05491,60.24069 25.07592,39.38574
  27.11161,81.99337 5.88408,123.1953 -13.03903,25.31314 -27.44972,42.82712
  -51.57723,62.73362 -40.09844,33.06211 -86.70754,56.08608 -151.06833,74.63514 C
  186.61557,459.91141 130.71496,472 119.20225,472 c -2.44075,0 -7.02006,-8.00296
  -21.295953,-37.28315 l -0.03402,0.0151 z M 110.77601,281.61191 C 65.760136,275.77998
  27.985273,270.70947 26.81537,270.33687 24.815625,269.6926 17.660677,245.82107
  13.624773,226.39004 12.607902,221.4726 11.11559,208.45131 10.30202,197.43174
  6.6716589,148.26132 17.370799,114.26648 46.041165,83.697237 94.583571,31.98518
  198.51713,25.694031 315.77765,67.369458 c 20.58274,7.324215 28.75504,12.410983
  24.975,15.580668 -2.79708,2.339846 -21.75315,2.305883 -54.50916,-0.102387
  -51.20464,-3.763759 -90.18335,3.357226 -110.27491,20.176211 -30.58742,25.60158
  -25.92345,81.72365 13.53071,162.68196 4.27316,8.76586 8.57881,17.34466 9.56318,19.09094
  2.28966,4.01773 0.62803,7.74899 -3.3572,7.56196 -1.69755,-0.0813 -39.91486,-4.91203
  -84.92926,-10.74592 z m 151.01614,-44.04726 c -35.92814,-6.45997 -68.22691,-28.7388
  -78.65437,-54.22127 -5.00209,-12.24165 -4.76437,-28.2131 0.57585,-37.77483
  4.83279,-8.64723 17.3107,-18.64993 28.48481,-22.83843 18.59924,-6.96791
  51.17019,-4.18853 74.90688,6.40975 22.53229,10.05487 42.50672,27.73816
  49.93183,44.18457 9.52925,21.10841 1.59321,44.65955 -18.82072,55.90059
  -13.5307,7.44285 -39.82676,11.32572 -56.44249,8.34109 h 0.0181 z"
  style="stroke-width:0.0675235" />
</symbol>

<symbol width="32" height="32" viewBox="0 0 512 512" id="orcid">
  <path style="stroke-width:0.07717" d="m 336.6206,194.53756 c -7.12991,-3.32734
  -13.8671,-5.55949 -20.25334,-6.61343 -6.36534,-1.09517 -16.57451,-1.61223
  -30.71059,-1.61223 h -36.70409 v 152.74712 h 37.63425 c 14.6735,0 26.08126,-1.01267
  34.22385,-3.01709 8.14259,-2.00442 14.92159,-4.52592 20.35674,-7.62608 5.43519,-3.07925
  10.416,-6.8615 14.94192,-11.38742 14.4876,-14.71475 21.74129,-33.27334 21.74129,-55.7176
  0,-22.05151 -7.44016,-40.05177 -22.34085,-53.98159 -5.49732,-5.16674 -11.82143,-9.44459
  -18.88918,-12.79281 z M 255.99999,8.0000031 C 119.02153,8.0000031 8.0000034,119.04185
  8.0000034,255.99998 8.0000034,392.95812 119.02153,504 255.99999,504 392.97849,504
  504,392.95812 504,255.99998 504,119.04185 392.97849,8.0000031 255.99999,8.0000031
  Z M 173.66372,365.51268 H 144.27546 V 160.1481 h 29.38826 z M 158.94954,138.69619
  c -11.13935,0 -20.21208,-9.01056 -20.21208,-20.21208 0,-11.11841 9.05183,-20.191181
  20.21208,-20.191181 11.18058,0 20.23244,9.051831 20.23244,20.191181 -0.0219,11.22184
  -9.05186,20.21208 -20.23244,20.21208 z m 241.3866,163.59715 c -5.29051,12.54475
  -12.83407,23.58066 -22.65053,33.08742 -9.98203,9.83734 -21.59659,17.19443
  -34.84378,22.19616 -7.74983,3.01709 -14.83852,5.06335 -21.30725,6.11726
  -6.4891,1.01267 -18.82759,1.50883 -37.07593,1.50883 H 219.5033 V 160.1481 h
  69.23318 c 27.96195,0 50.03378,4.1541 66.31951,12.54476 16.26485,8.36977
  29.18144,20.72859 38.79164,36.97254 9.61013,16.26483 14.4254,34.01757
  14.4254,53.19607 0.0227,13.76426 -2.66619,26.90802 -7.93576,39.43187 z" />
</symbol>

<symbol width="32" height="32" viewBox="0 0 512 512" id="cv">
<path style="stroke-width:0.07717" d="m 249.17973,328.32402 c -9.78758,15.38441
-19.17851,30.4337 -40.22128,45.05521 -11.25687,7.89055 -37.16464,23.30604
-73.9908,23.30604 -70.258325,0 -126.9676516,-51.07979 -126.9676516,-140.88446
0,-78.48565 53.3447156,-140.48607 128.4662816,-140.48607 30.4337,0 57.47396,10.52167
77.38654,26.30447 18.41392,14.65033 27.03796,29.30348 34.56291,42.45573 l -52.58013,26.27338
c -3.76134,-8.62631 -8.28954,-17.64933 -19.91259,-27.40585 -12.78437,-10.15549
-25.53991,-13.15224 -36.45998,-13.15224 -42.821335,0 -65.364452,39.82459
-65.364452,84.14459 0,58.23852 29.700162,87.14305 65.364452,87.14305 34.5629,0
48.47976,-24.0418 57.47396,-39.42563 l 52.24332,26.67235 z M 433.37382,123.57317
H 504 L 411.96314,388.7947 H 344.36647 L 253.46212,123.57317 h 70.62446
l 54.84337,188.60017 z" id="path2" />
</symbol>

<symbol width="32" height="32" viewBox="2.5 2.25 45 45" id="google-scholar">
<path d="M 25 3 C 12.85 3 3 12.85 3 25 C 3 37.15 12.85 47 25 47 C 37.15 47 47
37.15 47 25 C 47 12.85 37.15 3 25 3 z M 21 11 L 38 11 L 36.980469 11.880859 C
36.980469 11.920859 37 11.96 37 12 L 37 17.279297 C 37.6 17.619297 38 18.26 38
19 L 38 25 C 38 26.1 37.1 27 36 27 C 34.9 27 34 26.1 34 25 L 34 19 C 34 18.26
34.4 17.619297 35 17.279297 L 35 13.570312 L 31.410156 16.650391 C 31.760156
17.350391 32 18.200234 32 19.240234 C 32 21.960234 30.480703 23.309766 28.970703
24.509766 C 28.500703 24.989766 27.949219 25.510312 27.949219 26.320312 C 27.949219
27.120313 28.500391 27.570625 28.900391 27.890625 L 30.189453 28.919922 C 31.779453
30.279922 33.220703 31.530547 33.220703 34.060547 C 33.220703 37.510547 29.930469 41
23.730469 41 C 18.500469 41 15.980469 38.47 15.980469 35.75 C 15.980469 34.43 16.629766
32.559531 18.759766 31.269531 C 20.989766 29.879531 24.020391 29.690078 25.650391
29.580078 C 25.140391 28.920078 24.560547 28.230078 24.560547 27.080078 C 24.560547
26.470078 24.749687 26.100391 24.929688 25.650391 C 24.529688 25.690391 24.129531
25.730469 23.769531 25.730469 C 19.969531 25.730469 17.799297 22.85 17.779297 20 L 11
20 L 21 11 z M 24.269531 14.240234 C 23.339531 14.240234 22.33 14.710938 21.75 15.460938
C 21.14 16.220938 20.949219 17.210156 20.949219 18.160156 C 20.949219 20.620156 22.370938
24.699219 25.460938 24.699219 C 26.370938 24.699219 27.339922 24.259922 27.919922 23.669922
C 28.739922 22.819922 28.820312 21.65 28.820312 21 C 28.820312 18.35 27.269531 14.240234
24.269531 14.240234 z M 26.039062 30.609375 C 25.719062 30.609375 23.769766 30.679219
22.259766 31.199219 C 21.459766 31.499219 19.160156 32.370469 19.160156 34.980469 C
19.160156 37.590469 21.64 39.460938 25.5 39.460938 C 28.97 39.460938 30.800781 37.760234
30.800781 35.490234 C 30.800781 33.620234 29.620859 32.630391 26.880859 30.650391 C
26.590859 30.610391 26.409063 30.609375 26.039062 30.609375 z"/>
</symbol>

</svg>
"""

FONTS = """
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Glass+Antiqua&display=swap" rel="stylesheet">
"""

HEADER = """
<header>
<name><a href="/">Victor Seixas Souza</a></name>
<nav>
  <a href="/publications">Publications</a>
  <a href="/teaching">Teaching</a>
</nav>
</header>
"""

FOOTER = f"""
<footer>
  <edit>{date.today().strftime("%B %Y")}</edit>
  <copyright>&copy; Victor Seixas Souza, 2023 - {date.today().year}</copyright>
</footer>
"""

def bake_page(BODY, PATH):
  HTML = f"""
  <!doctype html>
  <html lang="en">
  <link rel="icon" href="favicon/favicon-32x32.png">
  {FONTS}
  {KATEX}
  <head>
    <meta charset="utf-8">
    <title>Victor Seixas Souza</title>
    <meta name="description" content="Personal homepage of Victor Seixas Souza">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
  {HEADER}
  {BODY}
  {FOOTER}
  </body>
  </html>
  """
  with open(PATH, "w", encoding="utf-8") as f:
    f.write(HTML)



pubfile = open("data/publications.toml", "rb")
pubdata = tomllib.load(pubfile)
pubfile.close()

authorfile = open("data/authors.toml", "rb")
authordata = tomllib.load(authorfile)
authorfile.close()

def bake_author(label):
  for author in authordata["author"]:
    if author["label"] == label:
      if "me" in author:
        return f"<me>{author["citename"]}</me>"
      AUTH = ""
      if "website" in author:
        AUTH +=f'<a href="{author["website"]}">'
      AUTH += author["citename"]
      if "website" in author:
        AUTH += "</a>"
      return AUTH
  return f"[AUTHOR {label} NOT FOUND]"


def comma(lis):
  if not lis:
    return ""
  elif len(lis) == 1:
    return lis[0]
  elif len(lis) == 2:
    return f"{lis[0]} and {lis[1]}"
  else:
    return f"{', '.join(lis[:-1])}, and {lis[-1]}"


def bake_publication(pub):
  PUB = f"""
<pub>
<pub-year>{pub["year"]}</pub-year>
<pub-title>{pub["title"]}</pub-title>
<pub-auth>
"""
  authlist = [bake_author(auth) for auth in pub["authors"]]
  PUB += comma(authlist)
  PUB += "</pub-auth>"
  if "journal" in pub:
    if "year" in pub["journal"]:
      PUB += f"\n<journal>{pub["journal"]["name"]}, {pub["journal"]["year"]}</journal>"
    else:
      PUB += f"\n<journal>{pub["journal"]["name"]}</journal>"
  PUB+= f"""
<input type="checkbox" class="abs" id="{pub["label"]}">
<input type="checkbox" class="cite" id="{pub["label"]}-cite">"""
  if "links" in pub:
    PUB += "\n<links>"
    for name,link in pub["links"].items():
      PUB += f'\n<a href="{link}">{name}</a> <sep></sep>'
    PUB += f"""
<label for="{pub["label"]}" class="abs">abstract</label> <sep></sep>
<label for="{pub["label"]}-cite" class="cite">cite</label>
</links>"""
  PUB += f"""
<abstract>
{pub["abstract"]}</abstract>
<cite><pre>
{pub["cite"]}
</pre></cite>
</pub>
"""
  return PUB

JOR = ""
CONF = ""
SEL = ""
for pub in pubdata["publication"]:
  PUB = bake_publication(pub)
  if pub["conference"]:
    CONF += PUB
  else:
    JOR += PUB
  if pub["selected"]:
    SEL += PUB


def bake_coauthors():
  collabcount = {}
  for pub in pubdata["publication"]:
    for authlabel in pub["authors"]:
      if authlabel in collabcount:
        collabcount[authlabel] += 1
      else:
        collabcount[authlabel] = 1
  for author in authordata["author"]:
    author["papers"] = collabcount[author["label"]]
  authordata["author"].sort(key = lambda a: a["surname"], reverse = False)
  authordata["author"].sort(key = lambda a: a["papers"], reverse = True)
  CLOUD = "<cloud>"
  for author in authordata["author"]:
    if "me" in author:
      continue
    if "website" in author:
      CLOUD += f'\n<author><a href="{author["website"]}">{author["fullname"]}</a><sup>{collabcount[author["label"]]}</sup></author>'
    else:
      CLOUD += f'\n<author>{author["fullname"]}<sup>{collabcount[author["label"]]}</sup></author>'
  CLOUD += "\n</cloud>"
  return CLOUD

COAUTHORS = bake_coauthors()

INDEX_BODY = f"""
<header>
  <info>
    <title>Klarman Fellow at</title>
    <a href='https://math.cornell.edu/'>Department of Mathematics</a> <br>
    <a href='https://www.cornell.edu/'>Cornell University</a> <br>

    <br>
    505 Mallot Hall <br>
    Ithaca, 14853 NY <br>
    United States <br>
    <br>

    <title>Research Fellow at  </title>
    <a href='https://www.sid.cam.ac.uk/'>Sidney Sussex College</a> <br>
    Cambridge, CB2 3HU <br>
    United Kingdom<br>
    <br>

    <logos>
    <a href='https://orcid.org/0000-0001-7598-7792'>
      <svg class='orcid'><use xlink:href='#orcid'/></svg>
    </a>
    <a href='https://arxiv.org/a/souza_v_1.html'>
      <svg class='arxiv'><use xlink:href='#arxiv' /></svg>
    </a>
    <a href='https://github.com/victorsouza/'>
      <svg class='github'><use xlink:href='#github' /></svg>
    </a>
    <a href='https://scholar.google.com/citations?user=-MljGiMAAAAJ'>
      <svg class='google-scholar'><use xlink:href='#google-scholar' /></svg>
    </a>
    <a href='http://lattes.cnpq.br/0853141109951986'>
      <svg class='lattes'><use xlink:href='#lattes' /></svg>
    </a>
    <a href='files/cv-souza.pdf'>
      <svg class='cv'><use xlink:href='#cv' /></svg>
    </a>
    </logos>
    vsouza <bob /> cornell <bab /> edu </br>
    vss28 <bob /> cam <bab /> ac <bab /> uk 
  </info>
  <picture>
    <!-- <source media='(max-width: 767px)' srcset='img/port2.jpg'>
    <source media='(min-width: 768px)' srcset='img/port2.jpg'> -->
    <img src='img/port1.jpg'>
  </picture>
</header>

<section>
<p>
  I am a <a href="https://as.cornell.edu/research/klarman-fellowships">Klarman Fellow</a> in the <a href='https://math.cornell.edu/'>Department of Mathematics</a> at Cornell University since July of 2025.
  I am delighted to be  hosted by <a href="https://math.cornell.edu/martin-kassabov">Martin Kassabov</a> and <a href="https://www.stevenstrogatz.com/">Steven Strogatz</a>.
  In Cornell, I am one of the organisers of the <a href="/prob-at-cornell/">Probability Seminar</a>.
</p>
<p>
  I am also a Research Fellow at Sidney Sussex College, Cambridge.
  I previously held the position of Research Associate in the <a href="https://www.cst.cam.ac.uk/research/themes/algorithms-and-complexity">Algorithms and Complexity group</a> of the University of Cambridge, under the brilliant mentorship of <a href="https://www.cst.cam.ac.uk/people/tg508">Tom Gur</a>. 
</p>
<p>
  I hold a PhD from the <a href="https://www.dpmms.cam.ac.uk/"> Department of Pure Mathematics and Mathematical Statistics</a> at the University of Cambridge, where I was very fortunate of being supervised by Professor Béla Bollobás.
  Prior to that, I had the pleasure of being a master student of
  <a href="https://robiscounting.github.io/">Rob Morris</a> 
  at <a href="https://impa.br/">IMPA</a> surounded by the forests of Rio de Janeiro.
</p>
</section>

<section>
<title>Research Interests</title>

<p>
I am broadly interested in combinatorics, number theory, probability theory
and related areas in statistical physics and theoretical computer science.
</p>

<p>
Recently, I have been involved with the study of <a href="https://www.youtube.com/watch?v=RpU7JrE1uCk">synchronisation phenomena</a>.
My work on synchronisation has been recently featured in <a href="https://www.quantamagazine.org/new-proof-shows-that-expander-graphs-synchronize-20230724/"> Quanta magazine</a>.
</p>
</section>


<section>
<title>Selected Publications</title>
{SEL}
</section>

<section>
<title>Coauthors</title>
{COAUTHORS}
</section>

{SVG}
"""

PUB_BODY = f"""
<section>
<title>Publications</title>
{JOR}
</section>

<section>
<title>Conference Proceedings</title>
{CONF}
</section>
"""


TEACHING_BODY = """
<section>
<title>Teaching</title>
<ul>
  <li>
    2025 - Lecturer for <a href="https://www.maths.cam.ac.uk/postgrad/part-iii/files/GtC/Combinatorics/spectral-graph-theory.pdf">Spectral Graph Theory</a> (Part III) at the University of Cambridge.
  </li>
  <li>
    2024 - Supervisor for <b>Number Theory</b> (Part II) at the University of Cambridge.
  </li>
  <li>
    2024 - Lecturer for <a href="https://impa.br/ensino/programas-de-formacao/doutorado/minicursos/fourier-analysis-and-arithmetic-progressions/">Fourier Analysis and Arithmetic Progressions</a> (Minicourse) at IMPA.
  </li>
  <li>
    2023 - Supervisor for <b>Graph Theory</b> (Part II) at the University of Cambridge.
  </li>
  <li>
    2022 - Supervisor for <b>Number Theory</b> (Part II) at the University of Cambridge.
  </li>
  <li>
    2021 - Supervisor for <b>Number Theory</b> (Part II) at the University of Cambridge.
  </li>
  <li>
    2021 - Supervisor for <b>Analysis I</b> (Part IA) at the University of Cambridge.
  </li>
  <li>
    2020  - Supervisor for <b>Number Theory</b> (Part II) at the University of Cambridge.
  </li>
  <li>
    2017 - Teacher Assistant for <b>Probability I</b> (Graduate course) at IMPA.
  </li>
</ul>
</section>
"""

bake_page(BODY = INDEX_BODY, PATH = "index.html")

bake_page(BODY = PUB_BODY, PATH = "publications.html")

bake_page(BODY = TEACHING_BODY, PATH = "teaching.html")