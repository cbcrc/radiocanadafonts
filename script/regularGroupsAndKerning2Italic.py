regularpath = "../src/Radio-Canada-Regular.ufo"
italicpath = "../src/Radio-Canada-Italic.ufo"

regular = OpenFont(regularpath, showUI=False)
italic = OpenFont(italicpath, showUI=False)

groups = regular.groups
kerning = regular.kerning

italic.groups.clear()
italic.kerning.clear()
italic.groups.update(groups)
italic.kerning.update(kerning)
italic.save()