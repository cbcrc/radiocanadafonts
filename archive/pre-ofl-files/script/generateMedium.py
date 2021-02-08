reg = OpenFont("../src/Radio-Canada-Regular.ufo", showUI=False)
bld = OpenFont("../src/Radio-Canada-Bold.ufo", showUI=False)

factor = .6
med = NewFont(showUI=False)
med.info.update(reg.info)
med.features.text = reg.features.text
med.interpolate(factor, reg, bld)
med.info.styleName = "Medium"
med.info.postscriptFullName = "Radio-CanadaMedium"
med.info.postscriptFontName = "Radio-Canada-Medium"
path = "medium/Radio-Canada-Medium.ufo"
med.save(path)