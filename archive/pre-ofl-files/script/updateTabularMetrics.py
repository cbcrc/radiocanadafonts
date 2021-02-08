font = CurrentFont()

for g in font.selection:
    
    glyph = font[g]
    
    if glyph.width != 500:
        m = (glyph.width - 500) / 2
        glyph.leftMargin -= m
        glyph.rightMargin -= m
        glyph.mark = None
        glyph.update()