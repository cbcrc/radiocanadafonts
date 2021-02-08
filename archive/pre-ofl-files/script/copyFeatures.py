Light = OpenFont("../src/Radio-Canada-Light.ufo", showUI=False)
LightItalic = OpenFont("../src/Radio-Canada-LightItalic.ufo", showUI=False)
Regular = OpenFont("../src/Radio-Canada-Regular.ufo", showUI=False)
Italic = OpenFont("../src/Radio-Canada-Italic.ufo", showUI=False)
Medium = OpenFont("../src/Radio-Canada-Medium.ufo", showUI=False)
MediumItalic = OpenFont("../src/Radio-Canada-MediumItalic.ufo", showUI=False)
Bold = OpenFont("../src/Radio-Canada-Bold.ufo", showUI=False)
BoldItalic = OpenFont("../src/Radio-Canada-BoldItalic.ufo", showUI=False)

CondensedRegular = OpenFont("../src/Radio-Canada-Condensed-Regular.ufo", showUI=False)
CondensedItalic = OpenFont("../src/Radio-Canada-Condensed-Italic.ufo", showUI=False)
CondensedBold = OpenFont("../src/Radio-Canada-Condensed-Bold.ufo", showUI=False)
CondensedBoldItalic = OpenFont("../src/Radio-Canada-Condensed-BoldItalic.ufo", showUI=False)

features = Regular.features.text

Light.features.text = features
LightItalic.features.text = features
Italic.features.text = features
Medium.features.text = features
MediumItalic.features.text = features
Bold.features.text = features
BoldItalic.features.text = features
CondensedRegular.features.text = features
CondensedItalic.features.text = features
CondensedBold.features.text = features
CondensedBoldItalic.features.text = features

Light.save()
LightItalic.save()
Italic.save()
Medium.save()
MediumItalic.save()
Bold.save()
BoldItalic.save()
CondensedRegular.save()
CondensedItalic.save()
CondensedBold.save()
CondensedBoldItalic.save()
