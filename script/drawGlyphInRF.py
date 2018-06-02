# to use in RoboFont DrawBot

font = CurrentFont()

for glyph in font:
    newPage(1000, 1000)
    drawGlyph(glyph)