import argparse, string
parser = argparse.ArgumentParser()
parser.add_argument('--family')
parser.add_argument('--styles', nargs='*')
args = parser.parse_args()

family = args.family
styles = args.styles

hinting_min = 8
hinting_max = 50
hinting_range = range(hinting_min, hinting_max+1)

with open("unicodes-beta.txt", "r") as f:
	uni = f.read().splitlines()

glyphs = []
for u in uni:
	try:
		glyph = unichr(int(u, 16))
		glyphs.append(glyph)
	except KeyError:
		pass
	
text = ''.join(glyphs).encode("UTF-8")
print text

f = open('index.html', 'w')

header = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>ttfautohint specimen</title>
</head>
<body>
"""
footer = """</body>
</html>
"""
f.write(header)
f.write("<style>\n")
f.write("p {margin:0;font-family:Menlo,Courier,mono;font-size: 12px;}\n")

for style in styles:
	f.write("@font-face {\n")
	f.write("font-family: '%s-%s';\n" % (family, style))
	f.write("src: url('webfonts/%s-%s.ttf') format('truetype');\n" % (family, style))
	f.write("font-weight: normal;\n")
	f.write("font-style: normal;\n")
	f.write("}\n")

f.write("</style>\n")

for style in styles:
	for size in hinting_range:
		f.write("<p>%s px</p>\n"%size)
		f.write("<p style='font-family:%s-%s;font-size:%spx;'>%s</p>\n"%(family, style, size, text))
	f.write("<br/>\n")

f.write(footer)
f.close()
