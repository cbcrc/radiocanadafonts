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
varWdth = 0
step = -1


# MAIN
for frame in range(F - 1):
    new_page()
    #grid()  # Toggle for grid view
    #print("Sine step:", sin(step))

    NEEDS_WORK = """" $ """
    GF_CORE_1 = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿"""
    GF_CORE_2 = """ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿıŒœˆ˚˜–—‘’‚“”„•…‹›⁄⁴€−∕"""
    GF_PLUS_1 = """ĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİĴĵĶķĸ"""
    GF_PLUS_2 = """ĹĺĻļĽľĿŀŁłŃńŅņŇňŊŋŌōŎŏŐőŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰű"""
    GF_PLUS_3 = """ŲųŴŵŶŷŸŹźŻżŽžƏƒƠơƯưǄǅǆǇǈǉǊǋǌǦǧǪǫǺǻǼǽǾǿȀȁȂȃȄȅȆȇȈȉ"""
    GF_PLUS_4 = """ȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚțȪȫȬȭȰȱȲȳȷəʹʺʼˇ˘˙˛˝ẀẁẂẃẄẅẞ"""
    GF_PLUS_5 = """ẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộ"""
    GF_PLUS_6 = """ỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ‐†‡"""
    GF_PLUS_7 = """‰′″⁒₡₣₤₦₧₩₫₭₱₲₵₹₺₼₽№™∙≈≠≤≥⟨⟩ﬁﬂ"""
    LINE_1 = """A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9"""
    LINE_2 = """a b c d e f g h i j k l m n o p q r s t u v w x y z ! ? @ # % & ( : ; ) * - – —"""
    LINE_3 = """À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö × Ø Ù Ú Û Ü Ý Þ ß Œ œ """
    LINE_4 = """à á â ã ä å æ ç è é ê ë ì í î ï ð ñ ò ó ô õ ö ø ù ú û ü ý þ ÿ ı ‘ ’ ‚ “ ” „ • … ‹  ›"""
    LINE_5 = """Ā ā Ă ă Ą ą Ć ć Ĉ ĉ Ċ ċ Č č Ď ď Đ đ Ē ē Ĕ ĕ Ė ė Ę ę Ě ě Ĝ ĝ Ğ ğ Ġ ġ Ģ ģ Ĥ"""
    LINE_6 = """ĥ Ħ ħ Ĩ ĩ Ī ī Ĭ ĭ Į į İ Ĵ ĵ Ķ ķ ĸ Ĺ ĺ Ļ ļ Ľ ľ Ŀ ŀ Ł ł Ń ń Ņ ņ Ň ň Ŋ ŋ Ō ō Ŏ ŏ Ő"""
    LINE_7 = """ő Ŕ ŕ Ŗ ŗ Ř ř Ś ś Ŝ ŝ Ş ş Š š Ţ ţ Ť ť Ŧ ŧ Ũ ũ Ū ū Ŭ ŭ Ů ů Ű ű Ų ų Ŵ ŵ Ŷ ŷ Ÿ"""
    LINE_8 = """Ź ź Ż ż Ž ž Ǻ ǻ Ǽ ǽ Ǿ ǿ Ȁ ȁ Ȃ ȃ Ȅ ȅ Ȇ ȇ Ȉ ȉ Ȋ ȋ Ȍ ȍ Ȏ ȏ Ȑ ȑ Ȓ ȓ Ȕ ȕ Ȗ ȗ † ‡"""

    font("../../fonts/variable/RadioCanada-[wdth,wght].ttf")
    fontSize(U * 0.87)
    stroke(None)
    fill(1)
    varWght = remap(sin(step), -1, 1, 300, 700)
    varWdth = remap(sin(step), -1, 1, 75, 100)

    fontVariations(wght=varWght)
    fontVariations(wdth=100)
    text(LINE_1, (M, U * 27 - (0)))
    text(LINE_2, (M, U * 27 - ((U * 1.25) * 1)))
    text(LINE_3, (M, U * 27 - ((U * 1.25) * 2)))
    text(LINE_4, (M, U * 27 - ((U * 1.25) * 3)))
    text(LINE_5, (M, U * 27 - ((U * 1.25) * 4)))
    text(LINE_6, (M, U * 27 - ((U * 1.25) * 5)))
    text(LINE_7, (M, U * 27 - ((U * 1.25) * 6)))
    text(LINE_8, (M, U * 27 - ((U * 1.25) * 7)))

    fontVariations(wght=400)
    fontVariations(wdth=varWdth)
    text(LINE_1, (M, U * 13 - (0)))
    text(LINE_2, (M, U * 13 - ((U * 1.25) * 1)))
    text(LINE_3, (M, U * 13 - ((U * 1.25) * 2)))
    text(LINE_4, (M, U * 13 - ((U * 1.25) * 3)))
    text(LINE_5, (M, U * 13 - ((U * 1.25) * 4)))
    text(LINE_6, (M, U * 13 - ((U * 1.25) * 5)))
    text(LINE_7, (M, U * 13 - ((U * 1.25) * 6)))
    text(LINE_8, (M, U * 13 - ((U * 1.25) * 7)))

    step += 0.1

    # AUXILIARY TEXT INFO
    font("InputMonoCompressed-Regular")
    stroke(None)
    fontSize(U / 1.5)
    text("Radio Canada Variable Font: Weight Axis Range (300 - 700) wght = ", (M, U * 29.25))
    text(str(int(varWght)), (M * 12.5, U * 29.25))
    text("Radio Canada Variable Font: Width Axis Range (75 - 100) wdth = ", (M, U * 15.25))
    text(str(int(varWdth)), (M * 12.2, U * 15.25))
    stroke(1)
    strokeWidth(2)
    line((M, H - M), (W - M, H - M))
    line((M, H - (M + (U * 14))), (W - M, H - (M + (U * 14))))
    line((M, H - (M + (U * 28))), (W - M, H - (M + (U * 28))))

# SAVE THE ANIMATION IN THIS SCRIPT'S DIRECTORY
saveImage("animated-vf-specimen-roman.gif")

# END DRAWBOT
endDrawing()
