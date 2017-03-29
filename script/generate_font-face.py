import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--family')
parser.add_argument('--styles', nargs='*')
args = parser.parse_args()

family = args.family
styles = args.styles

f = open('style.css', 'w')

for style in styles:
	
	f.write("@font-face {\n")
	f.write("  font-family: '%s';\n" % family)
	
	f.write("  src: url('%s-%s.eot');\n" % (family, style))
	f.write("  src: url('%s-%s.eot?#iefix') format('embedded-opentype'),\n" % (family, style))
	f.write("       url('%s-%s.woff2') format('woff2'),\n" % (family, style))
	f.write("       url('%s-%s.woff') format('woff'),\n" % (family, style))
	f.write("       url('%s-%s.ttf')  format('truetype');\n" % (family, style))
	f.write("  font-weight: normal;\n") # do something here?
	f.write("  font-style: normal;\n") # do something here?
	f.write("}\n\n")

f.close()
