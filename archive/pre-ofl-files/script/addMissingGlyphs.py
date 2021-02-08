baseFont = OpenFont("../src/Radio-Canada-Regular.ufo", showUI=False)

font = CurrentFont()

templateNames = [glyph.name for glyph in font.templateGlyphs]

for glyph in baseFont:
    if glyph.name not in font and glyph.name not in templateNames:
        font.newGlyph(glyph.name)