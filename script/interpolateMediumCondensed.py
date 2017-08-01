reg = OpenFont("../src/Radio-Canada-Condensed.ufo", showUI=False)
bld = OpenFont("../src/Radio-Canada-CondensedBold.ufo", showUI=False)

for i in range(10+1):
    factor = i/10
    med = NewFont(showUI=False)
    med.info.update(reg.info)
    med.interpolate(factor, reg, bld)
    med.info.styleName = "Condensed Medium %s" % str(factor)
    med.info.postscriptFullName = "Radio-CanadaCondensedMedium%s" % str(factor)
    med.info.postscriptFontName = "Radio-Canada-Condensed-Medium-%s" % str(factor)
    med.removeOverlap()
    #path = "medium-condensed/Radio-Canada-CondensedMedium-%s.ufo" % factor
    #med.save(path)
    path = "mediumCondensed/Radio-Canada-CondensedMedium-%s.otf" % factor
    med.generate(path, "otf")
