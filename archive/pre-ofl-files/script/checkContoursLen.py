fonts = AllFonts()

base = fonts[0]
fonts = fonts[1:]

count = 0
for glyph in base:
    
    for font in fonts:
        
        other = font[glyph.name]
        
        if len(glyph) != len(other):
            print "check contours: ", glyph, other
            count+=1
print count