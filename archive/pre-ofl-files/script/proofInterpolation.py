from fontParts.world import *
from fontTools.pens.cocoaPen import CocoaPen
from AppKit import NSBezierPath

w, h = 1000, 500

path1 = "../src/Radio-Canada-BoldItalic.ufo"
font1 = OpenFont(path1, showInterface=False)
pen1 = CocoaPen(font1)

path2 = "../src/Radio-Canada-CondensedBoldItalic.ufo"
font2 = OpenFont(path2, showInterface=False)
pen2 = CocoaPen(font2)

fontX = NewFont()
fontX.interpolate(0.5, font1, font2)
penX = CocoaPen(fontX)

for char in font1.glyphOrder:
    
    glyph1 = font1[char]
    pen1.path = NSBezierPath.bezierPath()
    glyph1.draw(pen1)
    
    glyph2 = font2[char]
    pen2.path = NSBezierPath.bezierPath()
    glyph2.draw(pen2)
    
    glyphX = fontX[char]
    penX.path = NSBezierPath.bezierPath()
    glyphX.draw(penX)
    
    newPage(w, h)
    translate(100, 200)
    scale(0.25)
    
    drawPath(pen1.path)
    
    translate(glyph1.width+50)
    drawPath(penX.path)
    
    translate(glyphX.width+50)
    drawPath(pen2.path)
    
saveImage(["bolditalic-x-condensedbolditalic.pdf"])
    