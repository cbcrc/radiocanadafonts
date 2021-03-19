# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
# Note: Run this script from the project root directory with DrawBot installed in editable mode.
# Note: e.g. $ python3 documentation/slide-decks/final-project-presentation/final-project-presentation.py
# Typeface Used: https://input.fontbureau.com
# Unit Space: 72dpi (dots per inch)
from drawBot import *
from datetime import date
import math

# CONSTANTS
W = 792  # Width
H = 612  # Height
M = 36    # Margin
U = 18    # Unit
TODAY = str(date.today())

# Draws a Grid
def grid():
    strokeWidth(1)
    stroke(0.9)
    step_X = 0
    step_Y = 0
    increment_X = U
    increment_Y = U
    for x in range(40):
        polygon( (M+step_X, M), (M+step_X, H-M) )
        step_X += increment_X
    for y in range(30):
        polygon( (M, M+step_Y), (W-M, M+step_Y) )
        step_Y += increment_Y
    fill(None)
    rect(M, M, W-(2*M), H-(2*M))

# New Page
def new_page():
    newPage(W, H)
    fill(1)
    rect(-2, -2, W+2, H+2)


# START DRAWBOT
newDrawing()


# TEST FONTS
font("fonts/variable/RadioCanada-[wdth,wght].ttf")
for axis, data in listFontVariations().items():
    print((axis, data))
# for eachFontName in installedFonts():
#    print(eachFontName)

page_number = 0

new_page() #--------------------------------------------------#
# setup
#grid() # toggle for grid view
page_number += 1


fill(0)
strokeWidth(1)
line((M, H - M - U), (W - M, H - M - U))
line((M, M), (W - M, M))
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text(str(int(page_number)), (M, (U*31)+4))
text("Radio-Canada Variable Font v1.400", (M+(U*5), (U*31)+5))
text(TODAY, (M+(U*20), (U*31)+4))
text("Font Engineer: Eli Heuer", (M+(U*30.8), (U*31)+5))

stroke(None)
fill(0)
fontSize(50)
font("fonts/variable/Radiocanada-[wdth,wght].ttf")
fontVariations(wght = 700 )
fontVariations(wdth = 100 )

text("Radio-Canada typeface",  (M, (U*28)))

# Saving and post-processing
saveImage("documentation/slide-decks/radio-canada-deck.pdf")
print("Updated slide deck")
