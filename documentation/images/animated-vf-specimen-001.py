# RENDER THIS DOCUMENT WITH DRAWBOT: https://www.drawbot.com
# $ pip install git+https://github.com/typemytype/drawbot
# $ gifsicle -i animated-vf-specimen-001.gif -O3 --colors 32 -o anim-001.gif

# Note: The monospace font Input is used in this document and needs
# to be installed for an exact rebuild: https://input.fontbureau.com/

from drawBot import *
import math


# CONSTANTS
W = 1024  # Width
H = 1024  # Height
M = 64  # Margin
U = 32  # Unit (Grid Unit)
F = 64  # Frames (Animation)


GF_CORE = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿıŒœˆ˚˜–—‘’‚“”„•…‹›⁄⁴€−∕"""

GF_CORE_LINE_1 = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"""

GF_CORE_LINE_2 = """!"#$%&'()*+,-./0123456789:;<=>?@[\]^_`{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶"""

GF_CORE_LINE_3 = """ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñ"""

GF_CORE_LINE_4 = """òóôõöøùúûüýþÿıŒœˆ˚˜–—‘’‚“”„•…‹›⁄⁴€−∕"""

GF_PLUS = """ĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŊŋŌōŎŏŐőŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžƏƒƠơƯưǄǅǆǇǈǉǊǋǌǦǧǪǫǺǻǼǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚțȪȫȬȭȰȱȲȳȷəʹʺʼˇ˘˙˛˝ẀẁẂẃẄẅẞẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ‐†‡‰′″⁒₡₣₤₦₧₩₫₭₱₲₵₹₺₼₽№™∙≈≠≤≥⟨⟩ﬁﬂ"""

GF_PLUS_LINE_1 = """ĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİĴĵĶķĸ"""

GF_PLUS_LINE_2 = """ĹĺĻļĽľĿŀŁłŃńŅņŇňŊŋŌōŎŏŐőŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰű"""

GF_PLUS_LINE_3 = """ŲųŴŵŶŷŸŹźŻżŽžƏƒƠơƯưǄǅǆǇǈǉǊǋǌǦǧǪǫǺǻǼǽǾǿȀȁȂȃȄȅȆȇȈȉ"""

GF_PLUS_LINE_4 = """ȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚțȪȫȬȭȰȱȲȳȷəʹʺʼˇ˘˙˛˝ẀẁẂẃẄẅẞ"""

GF_PLUS_LINE_5 = """ẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộ"""

GF_PLUS_LINE_6 = """ỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ‐†‡"""

GF_PLUS_LINE_7 = """‰′″⁒₡₣₤₦₧₩₫₭₱₲₵₹₺₼₽№™∙≈≠≤≥⟨⟩ﬁﬂ"""


# REMAP INPUT RANGE TO VARIABLE FONT AXIS RANGE
# (E.G. SINE WAVE(-1,1) to WGHT(100,900))
def remap(value, input_min, input_max, output_min, output_max):
    input_span = input_max - input_min  # FIND INPUT RANGE SPAN
    output_span = output_max - output_min  # FIND OUTPUT RANGE SPAN
    value_scaled = float(value - input_min) / float(input_span)
    return output_min + (value_scaled * output_span)


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
    for y in range(28):
        polygon((M, M + step_Y), (W - M, M + step_Y))
        step_Y += increment_Y
    fill(None)
    rect(M, M, W - (2 * M), H - (2 * M))


# NEW PAGE
def new_page():
    newPage(W, H)
    frameDuration(1 / 60)
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


# SET ANIMATION VARIABLES
varWght = 0
step = -1


# MAIN
for frame in range(F - 1):
    new_page()
    # grid()  # Toggle for grid view
    print("Sine step:", sin(step))

    font("../../fonts/variable/RadioCanada-[wdth,wght].ttf")
    fontSize(U * 0.87)
    stroke(None)
    fill(1)
    varWght = remap(sin(step), -1, 1, 300, 700)
    fontVariations(wght=varWght)
    hyphenation(False)
    text(GF_CORE_LINE_1, (M, U * 25 - (0)))
    text(GF_CORE_LINE_2, (M, U * 25 - ((U * 1.25) * 1)))
    text(GF_CORE_LINE_3, (M, U * 25 - ((U * 1.25) * 2)))
    text(GF_CORE_LINE_4, (M, U * 25 - ((U * 1.25) * 3)))

    text(GF_PLUS_LINE_1, (M, U * 17))
    text(GF_PLUS_LINE_2, (M, U * 17 - ((U * 1.25) * 1)))
    text(GF_PLUS_LINE_3, (M, U * 17 - ((U * 1.25) * 2)))
    text(GF_PLUS_LINE_4, (M, U * 17 - ((U * 1.25) * 3)))
    text(GF_PLUS_LINE_5, (M, U * 17 - ((U * 1.25) * 4)))
    text(GF_PLUS_LINE_6, (M, U * 17 - ((U * 1.25) * 5)))
    text(GF_PLUS_LINE_7, (M, U * 17 - ((U * 1.25) * 6)))

    step += 0.1

    # AUXILIARY TEXT INFO
    font("InputMonoCompressed-Regular")
    stroke(None)
    fontSize(U / 1.5)
    text(
        "Radio Canada Variable Font: fonts/variable/RadioCanada-[wdth,wght].ttf",
        (M, U * 29.25),
    )
    text("Latin Core Character Set: Weight Axis (wght) = ", (M, U * 27.25))
    text(str(int(varWght)), (M * 9.3, U * 27.25))
    text("Latin Plus Character Set: Weight Axis (wght) = ", (M, U * 19.25))
    text(str(int(varWght)), (M * 9.3, U * 19.25))
    stroke(1)
    strokeWidth(2)
    line((M, H - M), (W - M, H - M))
    line((M, H - (M + (U * 2))), (W - M, H - (M + (U * 2))))
    line((M, H - (M + (U * 10))), (W - M, H - (M + (U * 10))))

# SAVE THE ANIMATION IN THIS SCRIPT'S DIRECTORY
saveImage("animated-vf-specimen-001.gif")


# END DRAWBOT
endDrawing()
