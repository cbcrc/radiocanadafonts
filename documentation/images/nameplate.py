# RENDER THIS DOCUMENT WITH DRAWBOT: https://www.drawbot.com
# $ pip install git+https://github.com/typemytype/drawbot

from drawBot import *
import math


# CONSTANTS
W = 1024  # Width
H = 256  # Height
M = 64  # Margin
U = 32  # Unit (Grid Unit)
F = 64  # Frames (Animation)


# DRAWS A GRID
def grid():
    strokeWidth(0.5)
    stroke(1, 0, 0, 0.5)
    step_X = 0
    step_Y = 0
    increment_X = U
    increment_Y = U
    for x in range(28):
        polygon((M + step_X, M), (M + step_X, H - M))
        step_X += increment_X
    for y in range(6):
        polygon((M, M + step_Y), (W - M, M + step_Y))
        step_Y += increment_Y
    fill(None)
    rect(M, M, W - (2 * M), H - (2 * M))


# NEW PAGE
def new_page():
    newPage(W, H)
    fill(0)
    rect(-2, -2, W + 2, H + 2)


# START DRAWBOT
newDrawing()


# TEST FONTS
font("../../fonts/variable/RadioCanada-[wdth,wght].ttf")
for axis, data in listFontVariations().items():
    print((axis, data))
# for eachFontName in installedFonts():
#    print(eachFontName)


# MAIN
new_page()
#grid()  # Toggle for grid view

font("../../fonts/variable/RadioCanada-[wdth,wght].ttf")
fontSize(U * 3.6)
stroke(None)
fill(1)
fontVariations(wght=700)
fontVariations(wdth=100)
text("Radio-Canada", ( M+(U*0.05), M+(U*0.85) ))

# SAVE THE IMAGE IN THIS SCRIPT'S DIRECTORY
saveImage("nameplate.png")

# END DRAWBOT
endDrawing()
