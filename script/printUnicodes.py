font = CurrentFont()
for g in font.glyphOrder:
    
    glyph = font[g]
    if glyph.unicodes:
        uni = str(hex(glyph.unicodes[0]))
        print uni