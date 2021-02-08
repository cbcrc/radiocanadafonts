from fontParts.world import *
from fontTools.pens.cocoaPen import CocoaPen
from AppKit import NSBezierPath
import datetime

today = str(datetime.date.today())

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
    stroke(None)
    fill(0)
    drawPath(pen.path)

w, h = 792, 612
glyphMargin = 0

romans = [
    "../src/Radio-Canada-Light.ufo",
    "../src/Radio-Canada-Regular.ufo",
    "../src/Radio-Canada-Medium.ufo",
    "../src/Radio-Canada-Bold.ufo",
    "../src/Radio-Canada-Condensed-Regular.ufo",
    "../src/Radio-Canada-Condensed-Bold.ufo",
    ]
italics = [
    "../src/Radio-Canada-LightItalic.ufo",
    "../src/Radio-Canada-Italic.ufo",
    "../src/Radio-Canada-MediumItalic.ufo",
    "../src/Radio-Canada-BoldItalic.ufo",
    "../src/Radio-Canada-Condensed-Italic.ufo",
    "../src/Radio-Canada-Condensed-BoldItalic.ufo",
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

glyphSet = fnt.glyphOrder
upm = fnt.info.unitsPerEm

for i, glyphName in enumerate(glyphSet):
    
    newPage(w, h)
    font("Radio-Canada-Medium")
    fill(1, 0, 0)
    text("DEV", (width()-36-textSize("DEV")[0], height()-36))
    fill(0)
    text(" Radio-Canada", (36, height()-36))
    font("Radio-Canada")
    text(today, (36, 36))
    page = "%s/%s" % (i+1, len(glyphSet))
    text(page, (width()-36-textSize(page)[0], 36))
    
    translate(72, height()-72)
    text(glyphName, (0, -18))

    scale(0.09)
    translate(0, -upm*1.5)    
    save()
    for fnt, pen in romanfonts:
        glyph = fnt[glyphName]
        drawMetrics(fnt)
        drawGlyph(glyph)
        translate(glyph.width+glyphMargin, 0)
    restore()
    translate(0, -upm*1.5)
    save()
    for fnt, pen in italicfonts:
        glyph = fnt[glyphName]
        drawMetrics(fnt, fnt.info.italicAngle, fnt.lib["com.typemytype.robofont.italicSlantOffset"])
        drawGlyph(glyph)
        translate(glyph.width+glyphMargin, 0)
    restore()      
    
saveImage(["Radio-Canada-DEV.pdf"])
    