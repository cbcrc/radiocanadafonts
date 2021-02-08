# Light = OpenFont("../src/Radio-Canada-Light.ufo", showUI=False)
# LightItalic = OpenFont("../src/Radio-Canada-LightItalic.ufo", showUI=False)
Regular = OpenFont("../src/Radio-Canada-Regular.ufo", showUI=False)
Italic = OpenFont("../src/Radio-Canada-Italic.ufo", showUI=False)
# Medium = OpenFont("../src/Radio-Canada-Medium.ufo", showUI=False)
# MediumItalic = OpenFont("../src/Radio-Canada-MediumItalic.ufo", showUI=False)
# Bold = OpenFont("../src/Radio-Canada-Bold.ufo", showUI=False)
# BoldItalic = OpenFont("../src/Radio-Canada-BoldItalic.ufo", showUI=False)

# CondensedRegular = OpenFont("../src/Radio-Canada-Condensed-Regular.ufo", showUI=False)
# CondensedItalic = OpenFont("../src/Radio-Canada-Condensed-Italic.ufo", showUI=False)
# CondensedBold = OpenFont("../src/Radio-Canada-Condensed-Bold.ufo", showUI=False)
# CondensedBoldItalic = OpenFont("../src/Radio-Canada-Condensed-BoldItalic.ufo", showUI=False)

# fonts = [Light, LightItalic, Regular, Italic, Medium, MediumItalic, Bold, BoldItalic, CondensedRegular, CondensedItalic, CondensedBold, CondensedBoldItalic]

#for font in fonts:
#    print font, len(font.kerning), len(font.groups)

for key, value in Regular.groups.items():
    if Italic.groups[key] != value:
        print "group error"

for key, value in Regular.kerning.items():
    if Italic.kerning[key] != value:
        print "kerning error"
        print key, value, Italic.kerning[key]