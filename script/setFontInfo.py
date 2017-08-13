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

#openTypeOS2Selection

#font.info.openTypeNameWWSFamilyName
#font.info.openTypeNameWWSSubfamilyName

### Radio-Canada ###
familyName = "Radio-Canada"
### --- ###

### Light ###
font = Light
styleName = "Light"
weightName = "Light"
font.info.familyName = familyName
font.info.styleName = styleName
font.info.styleMapFamilyName = "%s %s" % (familyName, weightName)
font.info.styleMapStyleName = "regular"
font.info.openTypeNamePreferredFamilyName = familyName
font.info.openTypeNamePreferredSubfamilyName = styleName
font.info.openTypeNameCompatibleFullName = "%s %s" % (familyName, styleName)
font.info.openTypeOS2WidthClass = 5 # Medium (normal)
font.info.openTypeOS2WeightClass = 300
font.info.postscriptFontName = "%s-%s" % (familyName.replace(" ", ""), styleName.replace(" ", ""))
font.info.postscriptFullName = "%s%s" % (familyName.replace(" ", ""), styleName.replace(" ", ""))
font.info.postscriptWeightName = weightName
assert len(font.info.postscriptFontName) < 29, "postscriptFontName"
assert len(font.info.postscriptFullName) < 29, "postscriptFontName"
font.info.postscriptBlueScale = 0.039625	
font.info.postscriptBlueShift = 7
font.info.postscriptBlueFuzz = 1
font.info.openTypeOS2Type = []
font.save()
### --- ###

### Regular ###
font = Regular
styleName = "Regular"
weightName = "Normal"
font.info.familyName = familyName
font.info.styleName = styleName
font.info.styleMapFamilyName = "%s" % familyName
font.info.styleMapStyleName = "regular"
font.info.openTypeNamePreferredFamilyName = familyName
font.info.openTypeNamePreferredSubfamilyName = styleName
font.info.openTypeNameCompatibleFullName = "%s %s" % (familyName, styleName)
font.info.openTypeOS2WidthClass = 5 # Medium (normal)
font.info.openTypeOS2WeightClass = 400
font.info.postscriptFontName = "%s-%s" % (familyName.replace(" ", ""), styleName.replace(" ", ""))
font.info.postscriptFullName = "%s%s" % (familyName.replace(" ", ""), styleName.replace(" ", ""))
font.info.postscriptWeightName = weightName
assert len(font.info.postscriptFontName) < 29, "postscriptFontName"
assert len(font.info.postscriptFullName) < 29, "postscriptFontName"
font.info.postscriptBlueScale = 0.039625	
font.info.postscriptBlueShift = 7
font.info.postscriptBlueFuzz = 1
font.info.openTypeOS2Type = []
font.save()
### --- ###

### Medium ###
font = Medium
styleName = "Medium"
weightName = "Medium"
font.info.familyName = familyName
font.info.styleName = styleName
font.info.styleMapFamilyName = "%s %s" % (familyName, weightName)
font.info.styleMapStyleName = "regular"
font.info.openTypeNamePreferredFamilyName = familyName
font.info.openTypeNamePreferredSubfamilyName = styleName
font.info.openTypeNameCompatibleFullName = "%s %s" % (familyName, styleName)
font.info.openTypeOS2WidthClass = 5 # Medium (normal)
font.info.openTypeOS2WeightClass = 500
font.info.postscriptFontName = "%s-%s" % (familyName.replace(" ", ""), styleName.replace(" ", ""))
font.info.postscriptFullName = "%s%s" % (familyName.replace(" ", ""), styleName.replace(" ", ""))
font.info.postscriptWeightName = weightName
assert len(font.info.postscriptFontName) < 29, "postscriptFontName"
assert len(font.info.postscriptFullName) < 29, "postscriptFontName"
font.info.postscriptBlueScale = 0.039625	
font.info.postscriptBlueShift = 7
font.info.postscriptBlueFuzz = 1
font.info.openTypeOS2Type = []
font.save()
### --- ###

### Bold ###
font = Bold
styleName = "Bold"
weightName = "Bold"
font.info.familyName = familyName
font.info.styleName = styleName
font.info.styleMapFamilyName = "%s" % familyName
font.info.styleMapStyleName = "bold"
font.info.openTypeNamePreferredFamilyName = familyName
font.info.openTypeNamePreferredSubfamilyName = styleName
font.info.openTypeNameCompatibleFullName = "%s %s" % (familyName, styleName)
font.info.openTypeOS2WidthClass = 5 # Medium (normal)
font.info.openTypeOS2WeightClass = 700
font.info.postscriptFontName = "%s-%s" % (familyName.replace(" ", ""), styleName.replace(" ", ""))
font.info.postscriptFullName = "%s%s" % (familyName.replace(" ", ""), styleName.replace(" ", ""))
font.info.postscriptWeightName = weightName
assert len(font.info.postscriptFontName) < 29, "postscriptFontName"
assert len(font.info.postscriptFullName) < 29, "postscriptFontName"
font.info.postscriptBlueScale = 0.039625	
font.info.postscriptBlueShift = 7
font.info.postscriptBlueFuzz = 1
font.info.openTypeOS2Type = []
font.save()
### --- ###

### LightItalic ###
font = LightItalic
styleName = "Light Italic"
weightName = "Light"
font.info.familyName = familyName
font.info.styleName = styleName
font.info.styleMapFamilyName = "%s %s" % (familyName, weightName)
font.info.styleMapStyleName = "italic"
font.info.openTypeNamePreferredFamilyName = familyName
font.info.openTypeNamePreferredSubfamilyName = styleName
font.info.openTypeNameCompatibleFullName = "%s %s" % (familyName, styleName)
font.info.openTypeOS2WidthClass = 5 # Medium (normal)
font.info.openTypeOS2WeightClass = 300
font.info.postscriptFontName = "%s-%s" % (familyName.replace(" ", ""), styleName.replace(" ", ""))
font.info.postscriptFullName = "%s%s" % (familyName.replace(" ", ""), styleName.replace(" ", ""))
font.info.postscriptWeightName = weightName
assert len(font.info.postscriptFontName) < 29, "postscriptFontName"
assert len(font.info.postscriptFullName) < 29, "postscriptFontName"
font.info.postscriptBlueScale = 0.039625	
font.info.postscriptBlueShift = 7
font.info.postscriptBlueFuzz = 1
font.info.openTypeOS2Type = []
font.save()
### --- ###

### Italic ###
font = Italic
styleName = "Italic"
weightName = "Normal"
font.info.familyName = familyName
font.info.styleName = styleName
font.info.styleMapFamilyName = "%s" % familyName
font.info.styleMapStyleName = "italic"
font.info.openTypeNamePreferredFamilyName = familyName
font.info.openTypeNamePreferredSubfamilyName = styleName
font.info.openTypeNameCompatibleFullName = "%s %s" % (familyName, styleName)
font.info.openTypeOS2WidthClass = 5 # Medium (normal)
font.info.openTypeOS2WeightClass = 400
font.info.postscriptFontName = "%s-%s" % (familyName.replace(" ", ""), styleName.replace(" ", ""))
font.info.postscriptFullName = "%s%s" % (familyName.replace(" ", ""), styleName.replace(" ", ""))
font.info.postscriptWeightName = weightName
assert len(font.info.postscriptFontName) < 29, "postscriptFontName"
assert len(font.info.postscriptFullName) < 29, "postscriptFontName"
font.info.postscriptBlueScale = 0.039625	
font.info.postscriptBlueShift = 7
font.info.postscriptBlueFuzz = 1
font.info.openTypeOS2Type = []
font.save()
### --- ###

### MediumItalic ###
font = MediumItalic
styleName = "Medium Italic"
weightName = "Medium"
font.info.familyName = familyName
font.info.styleName = styleName
font.info.styleMapFamilyName = "%s %s" % (familyName, weightName)
font.info.styleMapStyleName = "italic"
font.info.openTypeNamePreferredFamilyName = familyName
font.info.openTypeNamePreferredSubfamilyName = styleName
font.info.openTypeNameCompatibleFullName = "%s %s" % (familyName, styleName)
font.info.openTypeOS2WidthClass = 5 # Medium (normal)
font.info.openTypeOS2WeightClass = 500
font.info.postscriptFontName = "%s-%s" % (familyName.replace(" ", ""), styleName.replace(" ", ""))
font.info.postscriptFullName = "%s%s" % (familyName.replace(" ", ""), styleName.replace(" ", ""))
font.info.postscriptWeightName = weightName
assert len(font.info.postscriptFontName) < 29, "postscriptFontName"
assert len(font.info.postscriptFullName) < 29, "postscriptFontName"
font.info.postscriptBlueScale = 0.039625	
font.info.postscriptBlueShift = 7
font.info.postscriptBlueFuzz = 1
font.info.openTypeOS2Type = []
font.save()
### --- ###

### BoldItalic ###
font = BoldItalic
styleName = "Bold Italic"
weightName = "Bold"
font.info.familyName = familyName
font.info.styleName = styleName
font.info.styleMapFamilyName = "%s" % familyName
font.info.styleMapStyleName = "bold italic"
font.info.openTypeNamePreferredFamilyName = familyName
font.info.openTypeNamePreferredSubfamilyName = styleName
font.info.openTypeNameCompatibleFullName = "%s %s" % (familyName, styleName)
font.info.openTypeOS2WidthClass = 5 # Medium (normal)
font.info.openTypeOS2WeightClass = 700
font.info.postscriptFontName = "%s-%s" % (familyName.replace(" ", ""), styleName.replace(" ", ""))
font.info.postscriptFullName = "%s%s" % (familyName.replace(" ", ""), styleName.replace(" ", ""))
font.info.postscriptWeightName = weightName
assert len(font.info.postscriptFontName) < 29, "postscriptFontName"
assert len(font.info.postscriptFullName) < 29, "postscriptFontName"
font.info.postscriptBlueScale = 0.039625	
font.info.postscriptBlueShift = 7
font.info.postscriptBlueFuzz = 1
font.info.openTypeOS2Type = []
font.save()
### --- ###

### Radio-Canada ###
familyName = "Radio-Canada Condensed"
### --- ###

### CondensedRegular ###
font = CondensedRegular
styleName = "Regular"
weightName = "Normal"
font.info.familyName = familyName
font.info.styleName = styleName
font.info.styleMapFamilyName = "%s" % familyName
font.info.styleMapStyleName = "regular"
font.info.openTypeNamePreferredFamilyName = familyName
font.info.openTypeNamePreferredSubfamilyName = styleName
font.info.openTypeNameCompatibleFullName = "%s %s" % (familyName, styleName)
font.info.openTypeOS2WidthClass = 3 # Condensed
font.info.openTypeOS2WeightClass = 400
font.info.postscriptFontName = "%s-%s" % (familyName.replace(" ", "").replace("Condensed", "Cnd"), styleName.replace(" ", ""))
font.info.postscriptFullName = "%s%s" % (familyName.replace(" ", "").replace("Condensed", "Cnd"), styleName.replace(" ", ""))
font.info.postscriptWeightName = weightName
assert len(font.info.postscriptFontName) < 29, "postscriptFontName"
assert len(font.info.postscriptFullName) < 29, "postscriptFontName"
font.info.postscriptBlueScale = 0.039625	
font.info.postscriptBlueShift = 7
font.info.postscriptBlueFuzz = 1
font.info.openTypeOS2Type = []
font.save()
### --- ###

### CondensedItalic ###
font = CondensedItalic
styleName = "Italic"
weightName = "Normal"
font.info.familyName = familyName
font.info.styleName = styleName
font.info.styleMapFamilyName = "%s" % familyName
font.info.styleMapStyleName = "italic"
font.info.openTypeNamePreferredFamilyName = familyName
font.info.openTypeNamePreferredSubfamilyName = styleName
font.info.openTypeNameCompatibleFullName = "%s %s" % (familyName, styleName)
font.info.openTypeOS2WidthClass = 3 # Condensed
font.info.openTypeOS2WeightClass = 400
font.info.postscriptFontName = "%s-%s" % (familyName.replace(" ", "").replace("Condensed", "Cnd"), styleName.replace(" ", ""))
font.info.postscriptFullName = "%s%s" % (familyName.replace(" ", "").replace("Condensed", "Cnd"), styleName.replace(" ", ""))
font.info.postscriptWeightName = weightName
assert len(font.info.postscriptFontName) < 29, "postscriptFontName"
assert len(font.info.postscriptFullName) < 29, "postscriptFontName"
font.info.postscriptBlueScale = 0.039625	
font.info.postscriptBlueShift = 7
font.info.postscriptBlueFuzz = 1
font.info.openTypeOS2Type = []
font.save()
### --- ###

### CondensedBold ###
font = CondensedBold
styleName = "Bold"
weightName = "Bold"
font.info.familyName = familyName
font.info.styleName = styleName
font.info.styleMapFamilyName = "%s" % familyName
font.info.styleMapStyleName = "bold"
font.info.openTypeNamePreferredFamilyName = familyName
font.info.openTypeNamePreferredSubfamilyName = styleName
font.info.openTypeNameCompatibleFullName = "%s %s" % (familyName, styleName)
font.info.openTypeOS2WidthClass = 3 # Condensed
font.info.openTypeOS2WeightClass = 700
font.info.postscriptFontName = "%s-%s" % (familyName.replace(" ", "").replace("Condensed", "Cnd"), styleName.replace(" ", ""))
font.info.postscriptFullName = "%s%s" % (familyName.replace(" ", "").replace("Condensed", "Cnd"), styleName.replace(" ", ""))
font.info.postscriptWeightName = weightName
assert len(font.info.postscriptFontName) < 29, "postscriptFontName"
assert len(font.info.postscriptFullName) < 29, "postscriptFontName"
font.info.postscriptBlueScale = 0.039625	
font.info.postscriptBlueShift = 7
font.info.postscriptBlueFuzz = 1
font.info.openTypeOS2Type = []
font.save()
### --- ###

### CondensedBoldItalic ###
font = CondensedBoldItalic
styleName = "Bold Italic"
weightName = "Bold"
font.info.familyName = familyName
font.info.styleName = styleName
font.info.styleMapFamilyName = "%s" % familyName
font.info.styleMapStyleName = "bold italic"
font.info.openTypeNamePreferredFamilyName = familyName
font.info.openTypeNamePreferredSubfamilyName = styleName
font.info.openTypeNameCompatibleFullName = "%s %s" % (familyName, styleName)
font.info.openTypeOS2WidthClass = 3 # Condensed
font.info.openTypeOS2WeightClass = 700
font.info.postscriptFontName = "%s-%s" % (familyName.replace(" ", "").replace("Condensed", "Cnd"), styleName.replace(" ", ""))
font.info.postscriptFullName = "%s%s" % (familyName.replace(" ", "").replace("Condensed", "Cnd"), styleName.replace(" ", ""))
font.info.postscriptWeightName = weightName
assert len(font.info.postscriptFontName) < 29, "postscriptFontName"
assert len(font.info.postscriptFullName) < 29, "postscriptFontName"
font.info.postscriptBlueScale = 0.039625	
font.info.postscriptBlueShift = 7
font.info.postscriptBlueFuzz = 1
font.info.openTypeOS2Type = []
font.save()
### --- ###
