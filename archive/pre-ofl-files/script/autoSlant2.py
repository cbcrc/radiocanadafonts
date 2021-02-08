font = CurrentFont()
a = 12
for glyph in font:
    glyph.skew(a)

font.info.italicAngle = -a

#ext = "-slant-%s.ufo" % 12
#savePath = font.path.replace(".ufo", ext)
#font.save(savePath)