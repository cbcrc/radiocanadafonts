regularpath = "../src/Radio-Canada-Regular.ufo"
lightpath = "../src/Radio-Canada-Light.ufo"
boldpath = "../src/Radio-Canada-Bold.ufo"
cndpath = "../src/Radio-Canada-Condensed.ufo"
cndboldpath = "../src/Radio-Canada-CondensedBold.ufo"

regular = OpenFont(regularpath, showUI=False)
light = OpenFont(lightpath, showUI=False)
bold = OpenFont(boldpath, showUI=False)
cnd = OpenFont(cndpath, showUI=False)
cndbold = OpenFont(cndboldpath, showUI=False)

groups = regular.groups
kerning = regular.kerning

#light.groups.clear()
#light.kerning.clear()
#light.groups.update(groups)
#light.kerning.update(kerning)
#light.save()

#bold.groups.clear()
#bold.kerning.clear()
#bold.groups.update(groups)
#bold.kerning.update(kerning)
#bold.save()

cnd.groups.clear()
cnd.kerning.clear()
cnd.groups.update(groups)
cnd.kerning.update(kerning)
cnd.save()

cndbold.groups.clear()
cndbold.kerning.clear()
cndbold.groups.update(groups)
cndbold.kerning.update(kerning)
cndbold.save()
