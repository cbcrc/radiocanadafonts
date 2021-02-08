from fontParts.world import *
from fontTools.pens.cocoaPen import CocoaPen
from AppKit import NSBezierPath

def drawMetrics(fnt, italicAngle=0, italicOffset=0):
    save()
    translate(italicOffset)
    skew(-italicAngle)
    stroke(0.5)
    fill(None)
    rect(0, fnt.info.descender, glyph.width, fnt.info.ascender-fnt.info.descender)
    line((0, 0), (glyph.width, 0))
    line((0, fnt.info.xHeight), (glyph.width, fnt.info.xHeight))
    line((0, fnt.info.capHeight), (glyph.width, fnt.info.capHeight))
    restore()

def drawGlyph(glyph):
    pen.path = NSBezierPath.bezierPath()
    glyph.draw(pen)
    stroke(1, 0, 0)
    fill(None)
    drawPath(pen.path)

w, h = 792, 612
glyphMargin = 0

romans = [
    #"../src/Radio-Canada-Light.ufo",
    "../src/Radio-Canada-Regular.ufo",
    #"../src/Radio-Canada-Medium.ufo",
    #"../src/Radio-Canada-Bold.ufo",
    "../src/Radio-Canada-Condensed-Regular.ufo",
    #"../src/Radio-Canada-Condensed-Bold.ufo",
    ]
italics = [
    #"../src/Radio-Canada-LightItalic.ufo",
    "../src/Radio-Canada-Italic.ufo",
    #"../src/Radio-Canada-MediumItalic.ufo",
    #"../src/Radio-Canada-BoldItalic.ufo",
    "../src/Radio-Canada-Condensed-Italic.ufo",
    #"../src/Radio-Canada-Condensed-BoldItalic.ufo",
    ]
    
romanfonts = []
for path in romans:
    fnt = OpenFont(path, showInterface=False)
    pen = CocoaPen(fnt)
    romanfonts.append((fnt, pen))
italicfonts = []
for path in italics:
    fnt = OpenFont(path, showInterface=False)
    pen = CocoaPen(fnt)
    italicfonts.append((fnt, pen))

glyphSet = ['grave', 'grave.cap', 'acute', 'acute.cap', 'circumflex', 'circumflex.cap', 'caron', 'caron.cap', 'caron.alt', 'tilde', 'tilde.cap', 'dieresis', 'dieresis.cap', 'macron', 'macron.cap', 'macronmod', 'breve', 'breve.cap', 'ring', 'ring.cap', 'ring_acute', 'ring_acute.cap', 'hungarumlaut', 'hungarumlaut.cap', 'dotaccent', 'dotaccent.cap', 'cedilla', 'dotbelow', 'ogonek', 'commaaccent', 'commaaccent.alt']
upm = fnt.info.unitsPerEm

for i, glyphName in enumerate(glyphSet):
    
    newPage(w, h)
    
    translate(72, height()-72)

    scale(0.25)
    translate(0, -upm)    
    save()
    for fnt, pen in romanfonts:
        glyph = fnt[glyphName]
        drawMetrics(fnt)
        drawGlyph(glyph)
        translate(50) ###
    restore()
    translate(upm, 0)
    save()
    for fnt, pen in italicfonts:
        glyph = fnt[glyphName]
        drawMetrics(fnt, fnt.info.italicAngle, fnt.lib["com.typemytype.robofont.italicSlantOffset"])
        drawGlyph(glyph)
        translate(50) ###
    restore()      
    
saveImage(["accentProof.pdf"])
    