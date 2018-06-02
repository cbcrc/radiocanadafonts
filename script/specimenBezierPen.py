from glyphNameFormatter import GlyphName

class GlyphPointsBezierPen(object):
    
    def __init__(self, sc=1, onCurveRadius=1.5, offCurveRadius=1, color=(0, 0.95, 1, 0)):
        self.path = BezierPath()
        self.points = []
        self.scale = s
        self.onCurveRadius = onCurveRadius/s
        self.offCurveRadius = offCurveRadius/s
        self.color = color
        
    def beginPath(self):
        pass
    
    def addPoint(self, p, segmentType=None, smooth=None, name=None):
        self.points.append((p, segmentType, smooth, name))
    
    def endPath(self):
        nPoints = len(self.points)
        i = 0
        while i < nPoints:
            p1, segmentType, smooth, name = self.points[i]
            if segmentType == "line":
                self.dot(p1, smooth, self.onCurveRadius)
            elif segmentType == None: # curve
                p, _, _, _ = self.points[(i-1) % nPoints]
                p2, _, _, _ = self.points[(i+1) % nPoints]
                p3, smooth, _, _ = self.points[(i+2) % nPoints]
                self.handles(p, p1, p2, p3)
                self.dot(p3, smooth, self.onCurveRadius)
                i += 2
            i += 1
        self.points = []
    
    def dot(self, (x, y), smooth, r):
        cmykStroke(None)
        cmykFill(*self.color)
        oval(x-r, y-r, r*2, r*2)
    
    def handles(self, p, p1, p2, p3):
        cmykStroke(*self.color)
        strokeWidth(0.5/self.scale)
        cmykFill(None)
        line(p, p1)
        line(p2, p3)
        self.dot(p1, True, self.offCurveRadius)
        self.dot(p2, True, self.offCurveRadius)

class GlyphBezierPen(object):

    def __init__(self):
        path = BezierPath()
        self.path = path
    
    def moveTo(self, p):
        self.path.moveTo(p)
    
    def lineTo(self, p):
        self.path.lineTo(p)
    
    def curveTo(self, p1, p2, p3):
        self.path.curveTo(p1, p2, p3)
    
    def closePath(self):
        self.path.closePath()
    
    def addComponent(self, component, offset):
        pass
    
    def endPath(self):
        pass
    
    
def getRGB(r, g, b):
    return r/255, g/255, b/255


glyphNames = [
"C",
"I",
"Q",
"R",
"a",
"e",
"m",
"Aring",
"Dcroat",
"eacute",
"Hbar",
"Ntilde",
"eng",
"Oslash",
"oe",
"Rcaron",
"germandbls",
"f_f",
"ampersand",
"at",
"asterisk",
"question",
"braceleft",
"numbersign",
"perthousand",
"divide",
"section",
"sterling",
"numero",
"Delta",
"integral",
"quotedblright",
"Thorn",
]

ufos = [
    u"/Users/alexandresaumierdemers/Documents/Projets/Type/RC/rc-fonts/src/Radio-Canada-Bold.ufo", u"/Users/alexandresaumierdemers/Documents/Projets/Type/RC/rc-fonts/src/Radio-Canada-BoldItalic.ufo", u"/Users/alexandresaumierdemers/Documents/Projets/Type/RC/rc-fonts/src/Radio-Canada-Condensed-Bold.ufo", u"/Users/alexandresaumierdemers/Documents/Projets/Type/RC/rc-fonts/src/Radio-Canada-Condensed-BoldItalic.ufo", u"/Users/alexandresaumierdemers/Documents/Projets/Type/RC/rc-fonts/src/Radio-Canada-Condensed-Italic.ufo", u"/Users/alexandresaumierdemers/Documents/Projets/Type/RC/rc-fonts/src/Radio-Canada-Condensed-Regular.ufo", u"/Users/alexandresaumierdemers/Documents/Projets/Type/RC/rc-fonts/src/Radio-Canada-Italic.ufo", u"/Users/alexandresaumierdemers/Documents/Projets/Type/RC/rc-fonts/src/Radio-Canada-Light.ufo", u"/Users/alexandresaumierdemers/Documents/Projets/Type/RC/rc-fonts/src/Radio-Canada-LightItalic.ufo", u"/Users/alexandresaumierdemers/Documents/Projets/Type/RC/rc-fonts/src/Radio-Canada-Medium.ufo", u"/Users/alexandresaumierdemers/Documents/Projets/Type/RC/rc-fonts/src/Radio-Canada-MediumItalic.ufo", u"/Users/alexandresaumierdemers/Documents/Projets/Type/RC/rc-fonts/src/Radio-Canada-Regular.ufo"
    ]


    
for ufo in ufos:
    
    newDrawing()    
    
    f = OpenFont(ufo, showUI=False)
    
    for name in glyphNames:

        g = f[name]
        g.decompose()
        g.removeOverlap()
        uni = g.unicodes[0]
        gn = GlyphName(uni)
        
        
        newPage(612+90+90, 792)
        
        #image("RC_Specimen_portrait_p192.pdf", (0, 0))

        
        save()
        
        s = 400/1000 # 400 pt
        
        save()
        cmykFill(None)
        cmykStroke(0, 0, 0, 0.2)
        strokeWidth(0.5)
        
        y = height()/2 - f.info.capHeight/2*s
        line((0, y), (width(), y))
        line((0, y+f.info.descender*s), (width(), y+f.info.descender*s))
        line((0, y+f.info.xHeight*s), (width(), y+f.info.xHeight*s))
        line((0, y+f.info.capHeight*s), (width(), y+f.info.capHeight*s))
        line((0, y+f.info.ascender*s), (width(), y+f.info.ascender*s))
        
        x = width()/2 - g.width/2*s
        line((x, y+f.info.descender*s), (x, y+f.info.ascender*s))
        line((x+g.width*s, y+f.info.descender*s), (x+g.width*s, y+f.info.ascender*s))
        
        restore()
        
        translate(width()/2, height()/2)
        scale(s)
        translate(-g.width/2, -f.info.capHeight/2)
        
        pen = GlyphPointsBezierPen(sc=s)
        g.drawPoints(pen)
        drawPath(pen.path)
        
        cmykFill(None)
        cmykStroke(0, 0, 0, 1)
        strokeWidth(0.5/s)
        pen = GlyphBezierPen()
        g.draw(pen)
        drawPath(pen.path)
        
        
        restore()
        
        """
        cmykFill(0, 0, 0, 1)
        cmykStroke(None)
        t = FormattedString(font="Radio-Canada", fontSize=7, lineHeight=10, openTypeFeatures=dict(cpsp=True))

        t.append(gn.uniLetter)
        t.append("\n")
        t.append(gn.uniName)
        #t.append(gn.uniRangeName)
        t.append("\n")
        u = "U+{:04x}".format(uni).upper()
        t.append(u)
        textBox(t, (36, 72, 300, 72))
        """
        
        print gn.uniLetter
        print gn.uniName
        print "U+{:04x}".format(uni).upper()
        print
    
    pdfname = "specimen-%s-%s.pdf" % (f.info.familyName, f.info.styleName)
    saveImage([pdfname])
    f.close()
    endDrawing()
    