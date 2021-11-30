# drawbot.com - use drawbot-skia on Linux systems
# $ pip install git+https://github.com/typemytype/drawbot
from drawBot import *


# Constants, these are the main "settings" for the image
WIDTH = 2048
HEIGHT = 512
MARGIN = 128
FRAMES = 1
GRID_VIEW = False  # Change this from "False" to "True" for a grid overlay


# Draws a grid
def grid():
    stroke(1, 0, 0, 0.75)
    strokeWidth(2)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = MARGIN / 2, MARGIN / 2
    rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(29):
        polygon((MARGIN + STEP_X, MARGIN), (MARGIN + STEP_X, HEIGHT - MARGIN))
        STEP_X += INCREMENT_X
    for y in range(12):
        polygon((MARGIN, MARGIN + STEP_Y), (WIDTH - MARGIN, MARGIN + STEP_Y))
        STEP_Y += INCREMENT_Y
    polygon((WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    polygon((0, HEIGHT / 2), (WIDTH, HEIGHT / 2))


# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    newPage(WIDTH, HEIGHT)
    fill(0)
    rect(-2, -2, WIDTH + 2, HEIGHT + 2)
    if GRID_VIEW:
        grid()
        pass
    else:
        pass


# Print font info
font("RadioCanada[wdth,wght].ttf")
for axis, data in listFontVariations().items():
    print((axis, data))


# Draws the image
def draw_image():
    draw_background()
    fill(0.95)
    stroke(None)
    font("RadioCanada[wdth,wght].ttf")
    fontSize(MARGIN * 1.83)
    fontVariations(wght=700)
    fontVariations(wdth=100)
    text("Radio-Canada", (MARGIN - 8, MARGIN + 53))


# Build and save the image
if __name__ == "__main__":
    newDrawing()
    draw_image()
    saveImage("nameplate.png")
    endDrawing()
    print("DrawBot: Done :-)")
