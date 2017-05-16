for glyph in CurrentFont():
    
    if not glyph.components:
        glyph.move((-60, 0))
    else:
        if glyph.contours:
            print glyph