# RENDER WITH: http://www.drawbot.com/
from drawBot import *
import math
import os

# STATIC VARIABLES
W,H,M = 1000,1000,20  # WIDTH, HEIGHT, MARGIN
VAR_WGHT = 100        # VARIABLE FONT WEIGHT
U = 32                # ONE GRID UNIT

def set_font_roman():
    print("Roman font set")
    font("fonts/ttf/Radio-Canada-Bold.ttf")
#    for axis, data in listFontVariations().items():
#        print((axis, data))

def set_font_italic():
    print("Italic font set")
    font("fonts/ttf/Radio-Canada-Bold.ttf")

def grid(inc):
    stroke(0.2)
    stpX, stpY = 0, 0
    incX, incY = (W-(M*2))/inc, (H-(M*2))/inc
    for x in range(inc+1):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(inc+1):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY

# DRAW NEW PAGE
newPage(W, H)
fill(0)
rect(0, 0, W, H)
#grid(30)
set_font_roman()
fill(1)

# HEADLINE
fontSize(123)
stroke(None)
text("Radio-Canada", ( M+(U*0), M+(U*27) ))

# TEXT
text("ABCDEFGHIJKL",     (M+(U*0),   M+(U*22)))
text("MNOPQRSTUV",       (M+(U*0),   M+(U*18)))
text("WXY",              (M+(U*0),   M+(U*14)))
text("&Zabcdefgh",       (M+(U*8.1), M+(U*14)))
text("ijklmnopqrstuv",   (M+(U*0),   M+(U*10)))
text("wxyz!@#,.$%*(",    (M+(U*0),   M+(U*6)))
text("1234567890",       (M+(U*0),   M+(U*2)))

# Save GIF
os.chdir("docs")
os.chdir("specimens")
saveImage("basic-specimen.gif")
# saveImage("basic-specimen.pdf")
os.chdir("..")
os.chdir("..")
