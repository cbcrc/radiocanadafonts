for font in AllFonts():
    
    for glyph in font:
        
        glyph.getLayer('background').clear()
        glyph.copyToLayer('background')
        glyph.update()
