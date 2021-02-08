reg = OpenFont("../src/Radio-Canada-Regular.ufo", showUI=False)
bld = OpenFont("../src/Radio-Canada-Bold.ufo", showUI=False)

for i in range(10+1):
    factor = i/10
    med = NewFont(showUI=False)
    med.info.update(reg.info)
    med.interpolate(factor, reg, bld)
    med.info.styleName = "Medium %s" % str(factor)
    med.info.postscriptFullName = "Radio-CanadaMedium%s" % str(factor)
    med.info.postscriptFontName = "Radio-Canada-Medium-%s" % str(factor)
    med.removeOverlap()
    #path = "medium/Radio-Canada-Medium-%s.ufo" % factor
    #med.save(path)
    path = "medium/Radio-Canada-Medium-%s.otf" % factor
    med.generate(path, "otf")
