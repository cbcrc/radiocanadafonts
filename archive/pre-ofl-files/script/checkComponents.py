fonts = AllFonts()

base = fonts[0]
fonts = fonts[1:]

for glyph in base:
    
    for font in fonts:
        
        other = font[glyph.name]
        
        glyphComponents = [component.baseGlyph for component in glyph.components]
        otherComponents = [component.baseGlyph for component in other.components]
        
        if glyphComponents != otherComponents:
            print "check components: ", glyph, other, font
