fonts = AllFonts()

default = fonts[0]

fonts = fonts[1:]

for defaultglyph in default:
    
    for font in fonts:
        
        glyph = font[defaultglyph.name]
            
        glyph.mark = defaultglyph.mark
            
        glyph.update()
            