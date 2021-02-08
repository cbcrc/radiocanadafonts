baseFont = OpenFont("../src/Radio-Canada-Regular.ufo", showUI=False)

font = CurrentFont()

for baseGlyph in baseFont:
    if baseGlyph.anchors:
        glyph = font[baseGlyph.name]
        baseAnchors = [anchor.name for anchor in baseGlyph.anchors]
        anchors = [anchor.name for anchor in glyph.anchors]
        if sorted(baseAnchors) != sorted(anchors):
            print glyph.name, set(baseAnchors) - set(anchors)
            