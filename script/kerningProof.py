from fontParts.world import *
from fontTools.agl import AGL2UV

AGL2UV["kra"] = 312
AGL2UV["Nhookleft"] = 413
AGL2UV["guillemetleft"] = 171
AGL2UV["guillemetright"] = 187

romans = [
    'Radio-Canada-Light',
    'Radio-Canada-Regular',
    'Radio-Canada-Medium',
    'Radio-Canada-Bold',
    'Radio-CanadaCnd-Regular',
    'Radio-CanadaCnd-Bold',
]
italics = [
    'Radio-Canada-LightItalic',
    'Radio-Canada-Italic',
    'Radio-Canada-MediumItalic',
    'Radio-Canada-BoldItalic',
    'Radio-CanadaCnd-Italic',
    'Radio-CanadaCnd-BoldItalic',
]

fonts = [romans, italics]

w, h = 792, 612
fSize = 72

regular = OpenFont("../src/Radio-Canada-Regular.ufo", showInterface=False)

for i, (left, right) in enumerate(regular.kerning.keys()):
    value = "%s | %s = %s" % (left, right, regular.kerning[(left, right)])
    
    if "@" in left:
        left = regular.groups[left][0]
    if "@" in right:
        right = regular.groups[right][0]
    #print left, right
    
    leftFeature = rightFeature = None
    if "." in left:
        left, leftFeature = left.split(".")
    if "." in right:
        right, rightFeature = right.split(".")
    
    if leftFeature == "alt":
        leftFeature = dict(ss01=True, ss02=True)
    elif leftFeature == "pl":
        leftFeature = dict(pnum=True)
    else:
        leftFeature = None
        
    if rightFeature == "alt":
        rightFeature = dict(ss01=True, ss02=True)
    elif rightFeature == "pl":
        rightFeature = dict(pnum=True)
    else:
        rightFeature = None
    
    if left in AGL2UV:
        leftchar = unichr(AGL2UV[left])
    elif left == "f_f":
        leftchar = "ff"
    else:
        print left, right
    if right in AGL2UV:
        rightchar = unichr(AGL2UV[right])
    else:
        print left, right
    
    if leftchar.islower():
        leftcontext = "non"
    else:
        leftcontext = "HOH"
    if rightchar.islower():
        rightcontext = "non"
    else:
        rightcontext = "HOH"
    
    for styles in fonts:
        newPage(w, h)
        pairnumber = str(i+1)
        text(pairnumber, (width()-textSize(pairnumber)[0]-24, height()-36))
        text(str(value), (24, height()-36))
        translate(0, height()-fSize*1.5)
        for style in styles:
            string = FormattedString(font=style, fontSize=fSize)
            string.append(leftcontext)
            string.append(leftchar, openTypeFeatures=leftFeature)
            string.append(rightchar, openTypeFeatures=rightFeature)
            string.append(rightcontext)
            text(string, (width()/2-textSize(string)[0]/2, 0))
            translate(0, -fSize)
        
saveImage(["kerningProof.pdf"])
    