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

# Draw page info
def draw_page_info(page_number):
    fill(0)
    stroke(0)
    strokeWidth(1)
    line((M, H - M - U), (W - M, H - M - U))
    line((M, M), (W - M, M))
    font("InputMonoCompressed-Regular")
    stroke(None)
    fontSize(13)
    text(str(int(page_number)), (M, (U*31)+3))
    text("Radio-Canada Variable Font v1.400", (M+(U*10), (U*31)+3))
    text(TODAY, (M+(U*25), (U*31)+3))
    text("Font Engineer: Eli Heuer", (M+(U*30.8), (U*31)+3))

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
draw_page_info(page_number)

stroke(None)
fill(0)
fontSize(50)
font("fonts/variable/RadioCanada-[wdth,wght].ttf")
fontVariations(wght = 700 )
fontVariations(wdth = 100 )

text("Radio-Canada",  (M, (U*28)))
fontSize(25)
font("fonts/variable/RadioCanada-Italic[wdth,wght].ttf")
fontVariations(wght = 400 )
fontVariations(wdth = 100 )
text("Variable Font User Manual",  (M, M+3))


new_page() #--------------------------------------------------#
# setup
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)


fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("Partial Character Set", (M, (U*29)+3))
text("Google Fonts Latin Plus", (M, (U*28)+3))


stroke(None)
fill(0)
fontSize(18)
font("fonts/variable/Radiocanada-[wdth,wght].ttf")
fontVariations(wght = 400 )
fontVariations(wdth = 100 )

gf_plus = '''! " # $ % & ' ( ) * + , - . 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~ ¡ ¢ £ ¤ ¥ ¦ § ¨ © ª « ¬ ® ¯ ° ± ² ³ ´ µ ¶ · ¸ ¹ º » ¼ ½ ¾ ¿ À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö × Ø Ù Ú Û Ü Ý Þ ß à á â ã ä å æ ç è é ê ë ì í î ï ð ñ ò ó ô õ ö ÷ ø ù ú û ü ý þ ÿ ı Œ œ – — ‘ ’ ‚ “ ” „ • … ‹ › ⁴ € − Ā ā Ă ă Ą ą Ć ć Ĉ ĉ Ċ ċ Č č Ď ď Đ đ Ē ē Ĕ ĕ Ė ė Ę ę Ě ě Ĝ ĝ Ğ ğ Ġ ġ Ģ ģ Ĥ ĥ Ħ ħ Ĩ ĩ Ī ī Ĭ ĭ Į į İ Ĵ ĵ Ķ ķ ĸ Ĺ ĺ Ļ ļ Ľ ľ Ŀ ŀ Ł ł Ń ń Ņ ņ Ň ň Ŋ ŋ Ō ō Ŏ ŏ Ő ő Ŕ ŕ Ŗ ŗ Ř ř Ś ś Ŝ ŝ Ş ş Š š Ţ ţ Ť ť Ŧ ŧ Ũ ũ Ū ū Ŭ ŭ Ů ů Ű ű Ų ų Ŵ ŵ Ŷ ŷ Ÿ Ź ź Ż ż Ž ž Ə ƒ Ơ ơ Ư ư Ǆ ǅ ǆ Ǉ ǈ ǉ Ǌ ǋ ǌ Ǧ ǧ Ǫ ǫ Ǻ ǻ Ǽ ǽ Ǿ ǿ Ȁ ȁ Ȃ ȃ Ȅ ȅ Ȇ ȇ Ȉ ȉ Ȋ ȋ 
Ȍ ȍ Ȏ ȏ Ȑ ȑ Ȓ ȓ Ȕ ȕ Ȗ ȗ Ș ș Ț ț Ȫ ȫ Ȭ ȭ Ȱ ȱ Ȳ ȳ ȷ ə ʹ ʺ ʼ Ẁ ẁ Ẃ ẃ Ẅ ẅ ẞ Ạ ạ Ả ả Ấ ấ Ầ ầ Ẩ ẩ Ẫ ẫ Ậ ậ Ắ ắ Ằ ằ Ẳ ẳ Ẵ ẵ Ặ ặ Ẹ ẹ Ẻ ẻ Ẽ ẽ Ế ế Ề ề Ể ể Ễ ễ Ệ ệ Ỉ ỉ Ị ị Ọ ọ Ỏ ỏ Ố ố Ồ ồ Ổ ổ Ỗ ỗ Ộ ộ Ớ ớ Ờ ờ Ở ở Ỡ ỡ Ợ ợ Ụ ụ Ủ ủ Ứ ứ Ừ ừ Ử ử Ữ ữ Ự ự Ỳ ỳ Ỵ ỵ Ỷ ỷ Ỹ ỹ ‐ † ‡ ‰ ′ ″ ⁒ ₡ ₣ ₤ ₦ ₧ ₩ ₫ ₭ ₱ ₲ ₵ ₹ ₺ ₼ ₽ № ™ ∙ ≈ ≠ ≤ ≥ ⟨ ⟩ ﬁ ﬂ
'''
lineHeight(30)
textBox(gf_plus, (M+(U*10), M, U*30, (U*28)+4))


new_page() #--------------------------------------------------#
# setup
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)


fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))

fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("12pt Regular", (M, (U*29)+3))
text("Weight Axis: 400", (M, (U*28)+3))
text("Width Axis: 100", (M, (U*27)+3))
text("12pt Italic", (M, (U*15)+3))
text("Weight Axis: 400", (M, (U*14)+3))
text("Width Axis: 100", (M, (U*13)+3))


stroke(None)
fill(0)
fontSize(12)
font("fonts/variable/RadioCanada-[wdth,wght].ttf")
fontVariations(wght = 400 )
fontVariations(wdth = 100 )

rc_text_one = '''
Ici Radio-Canada Télé (stylized as ICI Radio-Canada TēLē, and formerly known as Télévision de Radio-Canada) is a Canadian French-language free-to-air television network owned by the Canadian Broadcasting Corporation (known in French as Société Radio-Canada), the national public broadcaster. It is the French-language counterpart of CBC Television, the broadcaster's English-language television network.

Its headquarters are at Maison Radio-Canada in Montreal, which is also home to the network's flagship station, CBFT-DT. Until the 2012 closedown of the CBC / Radio-Canada rebroadcaster network, it was the only francophone network in Canada to broadcast terrestrially in all Canadian provinces.
'''
lineHeight(None)
textBox(rc_text_one, (M+(U*10), M, U*20, (U*28)+9))

font("fonts/variable/RadioCanada-Italic[wdth,wght].ttf")
fontVariations(wght = 400 )
fontVariations(wdth = 100 )
textBox(rc_text_one, (M+(U*10), M - U*14, U*20, (U*28)+9))


new_page() #--------------------------------------------------#
# setup
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)


fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))

fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("12pt Condensed Regular", (M, (U*29)+3))
text("Weight Axis: 400", (M, (U*28)+3))
text("Width Axis: 75", (M, (U*27)+3))
text("12pt Condensed Italic", (M, (U*15)+3))
text("Weight Axis: 400", (M, (U*14)+3))
text("Width Axis: 75", (M, (U*13)+3))

stroke(None)
fill(0)
fontSize(12)
font("fonts/variable/RadioCanada-[wdth,wght].ttf")
fontVariations(wght = 400 )
fontVariations(wdth = 75 )
lineHeight(None)
textBox(rc_text_one, (M+(U*10), M, U*19, (U*28)+9))

font("fonts/variable/RadioCanada-Italic[wdth,wght].ttf")
fontVariations(wght = 400 )
fontVariations(wdth = 75 )
textBox(rc_text_one, (M+(U*10), M - U*14, U*19, (U*28)+9))


new_page() #--------------------------------------------------#
# setup
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)


fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))

fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("12pt Bold", (M, (U*29)+3))
text("Weight Axis: 700", (M, (U*28)+3))
text("Width Axis: 100", (M, (U*27)+3))
text("12pt Bold Italic", (M, (U*15)+3))
text("Weight Axis: 700", (M, (U*14)+3))
text("Width Axis: 100", (M, (U*13)+3))

stroke(None)
fill(0)
fontSize(12)
font("fonts/variable/RadioCanada-[wdth,wght].ttf")
fontVariations(wght = 700 )
fontVariations(wdth = 100 )
lineHeight(None)
textBox(rc_text_one, (M+(U*10), M, U*20, (U*28)+9))

font("fonts/variable/RadioCanada-Italic[wdth,wght].ttf")
fontVariations(wght = 700 )
fontVariations(wdth = 100 )
textBox(rc_text_one, (M+(U*10), M - U*14, U*20, (U*28)+9))


new_page() #--------------------------------------------------#
# setup
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)


fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))

fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("12pt Condensed Bold", (M, (U*29)+3))
text("Weight Axis: 700", (M, (U*28)+3))
text("Width Axis: 75", (M, (U*27)+3))
text("12pt Condnsd Bold Italic", (M, (U*15)+3))
text("Weight Axis: 700", (M, (U*14)+3))
text("Width Axis: 75", (M, (U*13)+3))

stroke(None)
fill(0)
fontSize(12)
font("fonts/variable/RadioCanada-[wdth,wght].ttf")
fontVariations(wght = 700 )
fontVariations(wdth = 75 )
lineHeight(None)
textBox(rc_text_one, (M+(U*10), M, U*20, (U*28)+9))

font("fonts/variable/RadioCanada-Italic[wdth,wght].ttf")
fontVariations(wght = 700 )
fontVariations(wdth = 75 )
textBox(rc_text_one, (M+(U*10), M - U*14, U*20, (U*28)+9))


new_page() #--------------------------------------------------#
# setup
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)


fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))

fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("12pt Light", (M, (U*29)+3))
text("Weight Axis: 300", (M, (U*28)+3))
text("Width Axis: 100", (M, (U*27)+3))
text("12pt Light Italic", (M, (U*15)+3))
text("Weight Axis: 300", (M, (U*14)+3))
text("Width Axis: 100", (M, (U*13)+3))

stroke(None)
fill(0)
fontSize(12)
font("fonts/variable/RadioCanada-[wdth,wght].ttf")
fontVariations(wght = 300 )
fontVariations(wdth = 100 )
lineHeight(None)
textBox(rc_text_one, (M+(U*10), M, U*20, (U*28)+9))

font("fonts/variable/RadioCanada-Italic[wdth,wght].ttf")
fontVariations(wght = 300 )
fontVariations(wdth = 100 )
textBox(rc_text_one, (M+(U*10), M - U*14, U*20, (U*28)+9))


new_page() #--------------------------------------------------#
# setup
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)


fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))

fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("12pt Condensed Light", (M, (U*29)+3))
text("Weight Axis: 300", (M, (U*28)+3))
text("Width Axis: 75", (M, (U*27)+3))
text("12pt Cndnsd Light Italic", (M, (U*15)+3))
text("Weight Axis: 300", (M, (U*14)+3))
text("Width Axis: 75", (M, (U*13)+3))

stroke(None)
fill(0)
fontSize(12)
font("fonts/variable/RadioCanada-[wdth,wght].ttf")
fontVariations(wght = 300 )
fontVariations(wdth = 75 )
lineHeight(None)
textBox(rc_text_one, (M+(U*10), M, U*20, (U*28)+9))

font("fonts/variable/RadioCanada-Italic[wdth,wght].ttf")
fontVariations(wght = 300 )
fontVariations(wdth = 75 )
textBox(rc_text_one, (M+(U*10), M - U*14, U*20, (U*28)+9))


# Saving and post-processing
saveImage("documentation/slide-decks/radio-canada-deck.pdf")
print("Updated slide deck")
