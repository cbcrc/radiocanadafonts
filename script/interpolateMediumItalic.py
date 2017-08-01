reg = OpenFont("../src/Radio-Canada-Italic.ufo", showUI=False)
bld = OpenFont("../src/Radio-Canada-BoldItalic.ufo", showUI=False)

for i in range(10+1):
    factor = i/10
    med = NewFont(showUI=False)
    med.info.update(reg.info)
    med.interpolate(factor, reg, bld)
    med.info.styleName = "Medium Italic %s" % str(factor)
    med.info.postscriptFullName = "Radio-CanadaMediumItalic%s" % str(factor)
    med.info.postscriptFontName = "Radio-Canada-Medium-Italic-%s" % str(factor)
    med.removeOverlap()
    #path = "medium-italic/Radio-Canada-MediumItalic-%s.ufo" % factor
    #med.save(path)
    path = "mediumItalic/Radio-Canada-MediumItalic-%s.otf" % factor
    med.generate(path, "otf")
