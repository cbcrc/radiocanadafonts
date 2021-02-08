reg = OpenFont("../src/Radio-Canada-Italic.ufo", showUI=False)
bld = OpenFont("../src/Radio-Canada-BoldItalic.ufo", showUI=False)

factor = .6
med = NewFont(showUI=False)
med.info.update(reg.info)
med.features.text = reg.features.text
med.interpolate(factor, reg, bld)
med.info.styleName = "Medium Italic"
med.info.postscriptFullName = "Radio-CanadaMediumItalic"
med.info.postscriptFontName = "Radio-Canada-Medium-Italic"
path = "mediumItalic/Radio-Canada-MediumItalic.ufo"
med.save(path)