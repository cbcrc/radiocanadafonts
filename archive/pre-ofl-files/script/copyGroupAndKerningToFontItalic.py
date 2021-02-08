regularpath = "../src/Radio-Canada-Italic.ufo"
lightpath = "../src/Radio-Canada-LightItalic.ufo"
boldpath = "../src/Radio-Canada-BoldItalic.ufo"

regular = OpenFont(regularpath, showUI=False)
light = OpenFont(lightpath, showUI=False)
bold = OpenFont(boldpath, showUI=False)

groups = regular.groups
kerning = regular.kerning

light.groups.clear()
light.kerning.clear()
light.groups.update(groups)
light.kerning.update(kerning)
light.save()

bold.groups.clear()
bold.kerning.clear()
bold.groups.update(groups)
bold.kerning.update(kerning)
bold.save()