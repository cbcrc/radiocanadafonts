# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
# Note: Run this script from the project root directory with DrawBot installed.
# Note: e.g. $ python3 documentation/proofs/spacing-proof.py
# Mono-Space Typeface Used: https://input.fontbureau.com
# Unit Space: 72dpi (dots per inch)
from drawBot import *
from datetime import date
import math

# CONSTANTS
W = 792  # Width
H = 612  # Hight
M = 36   # Margin
U = 18   # Unit
TODAY = str(date.today())
KERN_KING_LOWERCASE = '''
lynx tuft frogs, dolphins abduct by proxy the ever awkward klutz, dud, dummkopf, jinx snubnose filmgoer, orphan sgt. renfruw grudgek reyfus, md. sikh psych if halt tympany jewelry sri heh! twyer vs jojo pneu fylfot alcaaba son of nonplussed halfbreed bubbly playboy guggenheim daddy coccyx sgraffito effect, vacuum dirndle impossible attempt to disvalue, muzzle the afghan czech czar and exninja, bob bixby dvorak wood dhurrie savvy, dizzy eye aeon circumcision uvula scrungy picnic luxurious special type carbohydrate ovoid adzuki kumquat bomb? afterglows gold girl pygmy gnome lb. ankhs acme aggroupment akmed brouhha tv wt. ujjain ms. oz abacus mnemonics bhikku khaki bwana aorta embolism vivid owls often kvetch otherwise, wysiwyg densfort wright you’ve absorbed rhythm, put obstacle kyaks krieg kern wurst subject enmity equity coquet quorum pique tzetse hepzibah sulfhydryl briefcase ajax ehler kafka fjord elfship halfdressed jugful eggcup hummingbirds swingdevil bagpipe legwork reproachful hunchback archknave baghdad wejh rijswijk rajbansi rajput ajdir okay weekday obfuscate subpoena liebknecht marcgravia ecbolic arcticward dickcissel pincpinc boldface maidkin adjective adcraft adman dwarfness applejack darkbrown kiln palzy always farmland flimflam unbossy nonlineal stepbrother lapdog stopgap sx countdown basketball beaujolais vb. flowchart aztec lazy bozo syrup tarzan annoying dyke yucky hawg gagzhukz cuzco squire when hiho mayhem nietzsche szasz gumdrop milk emplotment ambidextrously lacquer byway ecclesiastes stubchen hobgoblins crabmill aqua hawaii blvd. subquality byzantine empire debt obvious cervantes jekabzeel anecdote flicflac mechanicville bedbug couldn’t i’ve it’s they’ll they’d dpt. headquarter burkhardt xerxes atkins govt. ebenezer lg. lhama amtrak amway fixity axmen quumbabda upjohn hrumpf
'''
KERN_KING_UPPERCASE = '''
LYNX TUFT FROGS, DOLPHINS ABDUCT BY PROXY THE EVER AWKWARD KLUTZ, DUD, DUMMKOPF, JINX SNUBNOSE FILMGOER, ORPHAN SGT. RENFRUW GRUDGEK REYFUS, MD. SIKH PSYCH IF HALT TYMPANY JEWELRY SRI HEH! TWYER VS JOJO PNEU FYLFOT ALCAABA SON OF NONPLUSSED HALFBREED BUBBLY PLAYBOY GUGGENHEIM DADDY COCCYX SGRAFFITO EFFECT, VACUUM DIRNDLE IMPOSSIBLE ATTEMPT TO DISVALUE, MUZZLE THE AFGHAN CZECH CZAR AND EXNINJA, BOB BIXBY DVORAK WOOD DHURRIE SAVVY, DIZZY EYE AEON CIRCUMCISION UVULA SCRUNGY PICNIC LUXURIOUS SPECIAL TYPE CARBOHYDRATE OVOID ADZUKI KUMQUAT BOMB? AFTERGLOWS GOLD GIRL PYGMY GNOME LB. ANKHS ACME AGGROUPMENT AKMED BROUHHA TV WT. UJJAIN MS. OZ ABACUS MNEMONICS BHIKKU KHAKI BWANA AORTA EMBOLISM VIVID OWLS OFTEN KVETCH OTHERWISE, WYSIWYG DENSFORT WRIGHT YOU’VE ABSORBED RHYTHM, PUT OBSTACLE KYAKS KRIEG KERN WURST SUBJECT ENMITY EQUITY COQUET QUORUM PIQUE TZETSE HEPZIBAH SULFHYDRYL BRIEFCASE AJAX EHLER KAFKA FJORD ELFSHIP HALFDRESSED JUGFUL EGGCUP HUMMINGBIRDS SWINGDEVIL BAGPIPE LEGWORK REPROACHFUL HUNCHBACK ARCHKNAVE BAGHDAD WEJH RIJSWIJK RAJBANSI RAJPUT AJDIR OKAY WEEKDAY OBFUSCATE SUBPOENA LIEBKNECHT MARCGRAVIA ECBOLIC ARCTICWARD DICKCISSEL PINCPINC BOLDFACE MAIDKIN ADJECTIVE ADCRAFT ADMAN DWARFNESS APPLEJACK DARKBROWN KILN PALZY ALWAYS FARMLAND FLIMFLAM UNBOSSY NONLINEAL STEPBROTHER LAPDOG STOPGAP SX COUNTDOWN BASKETBALL BEAUJOLAIS VB. FLOWCHART AZTEC LAZY BOZO SYRUP TARZAN ANNOYING DYKE YUCKY HAWG GAGZHUKZ CUZCO SQUIRE WHEN HIHO MAYHEM NIETZSCHE SZASZ GUMDROP MILK EMPLOTMENT AMBIDEXTROUSLY LACQUER BYWAY ECCLESIASTES STUBCHEN HOBGOBLINS CRABMILL AQUA HAWAII BLVD. SUBQUALITY BYZANTINE EMPIRE DEBT OBVIOUS CERVANTES JEKABZEEL ANECDOTE FLICFLAC MECHANICVILLE BEDBUG COULDN’T I’VE IT’S THEY’LL THEY’D DPT. HEADQUARTER BURKHARDT XERXES ATKINS GOVT. EBENEZER LG. LHAMA AMTRAK AMWAY FIXITY AXMEN QUUMBABDA UPJOHN HRUMPF
'''
KERN_KING_SENTENCECASE = '''
Aaron Abraham Adam Aeneas Agfa Ahoy Aileen Akbar Alanon Americanism Anglican Aorta April Fool’s Day Aqua Lung (Tm.) Arabic Ash Wednesday Authorized Version Ave Maria Away Axel Ay Aztec Bhutan Bill Bjorn Bk Btu. Bvart Bzonga California Cb Cd Cervantes Chicago Clute City, Tx. Cmdr. Cnossus Coco Cracker State, Georgia Cs Ct. Cwacker Cyrano David Debra Dharma Diane Djakarta Dm Dnepr Doris Dudley Dwayne Dylan Dzerzhinsk Eames Ectomorph Eden Eerie Effingham, Il. Egypt Eiffel Tower Eject Ekland Elmore Entreaty Eolian Epstein Equine Erasmus Eskimo Ethiopia Europe Eva Ewan Exodus Jan van Eyck Ezra Fabian February Fhara Fifi Fjord Florida Fm France Fs Ft. Fury Fyn Gabriel Gc Gdynia Gehrig Ghana Gilligan Karl Gjellerup Gk. Glen Gm Gnosis Gp.E. Gregory Gs Gt. Br. Guinevere Gwathmey Gypsy Gzags Hebrew Hf Hg Hileah Horace Hrdlicka Hsia Hts. Hubert Hwang Hai Hyacinth Hz. Iaccoca Ibsen Iceland Idaho If Iggy Ihre Ijit Ike Iliad Immediate Innocent Ione Ipswitch Iquarus Ireland Island It Iud Ivert Iwerks Ixnay Iy Jasper Jenks Jherry Jill Jm Jn Jorge Jr. Julie Kerry Kharma Kiki Klear Koko Kruse Kusack Kylie Laboe Lb. Leslie Lhihane Llama Lorrie Lt. Lucy Lyle Madeira Mechanic Mg. Minnie Morrie Mr. Ms. Mt. Music My Nanny Nellie Nillie Novocane Null Nyack Oak Oblique Occarina Odd Oedipus Off Ogmane Ohio Oil Oj Oklahoma Olio Omni Only Oops Opera Oqu Order Ostra Ottmar Out Ovum Ow Ox Oyster Oz Parade Pd. Pepe Pfister Pg. Phil Pippi Pj Please Pneumonia Porridge Price Psalm Pt. Purple Pv Pw Pyre Qt. Quincy Radio Rd. Red Rhea Right Rj Roche Rr Rs Rt. Rural Rwanda Ryder Sacrifice Series Sgraffito Shirt Sister Skeet Slow Smore Snoop Soon Special Squire Sr St. Suzy Svelte Swiss Sy Szach Td Teach There Title Total Trust Tsena Tulip Twice Tyler Tzean Ua Udder Ue Uf Ugh Uh Ui Uk Ul Um Unkempt Uo Up Uq Ursula Use Utmost Uvula Uw Uxurious Uzßai Valerie Velour Vh Vicky Volvo Vs Water Were Where With World Wt. Wulk Wyler Xavier Xerox Xi Xylophone Yaboe Year Yipes Yo Ypsilant Ys Yu Zabar’s Zero Zhane Zizi Zorro Zu Zy Don’t I’ll I’m I’se
'''
SPACING_STRINGS_LETTERS_LOWERCASE = '''
nnonnoonoo nnannooaoo nnbnnooboo nncnnoocoo nndnnoodoo nnennooeoo nnfnnoofoo nngnnoogoo nnhnnoohoo nninnooioo nnjnnoojoo nnknnookoo nnlnnooloo nnmnnoomoo nnpnnoopoo nnqnnooqoo nnnnooroo nnsnnoosoo nntnnootoo nnunnoouoo nnvnnoovoo nnwnnoowoo nnxnnooxoo nnynnooyoo nnznnoozoo
'''
SPACING_STRINGS_LETTERS_UPPERCASE = '''
HHOHHOOHOO HHAHHOOAOO HHBHHOOBOO HHCHHOOCOO HHDHHOODOO HHEHHOOEOO HHFHHOOFOO HHGHHOOGOO HHIHHOOIOO HHJHHOOJOO HHKHHOOKOO HHLHHOOLOO HHMHHOOMOO HHNHHOONOO HHPHHOOPOO HHQHHOOQOO HHRHHOOROO HHSHHOOSOO HHTHHOOTOO HHUHHOOUOO HHVHHOOVOO HHWHHOOWOO HHXHHOOXOO HHYHHOOYOO HHZHHOOZOO
'''
SPACING_STRINGS_LETTERS_LOWERCASE_PUNCTUATION = '''
nn.nnoo.oo nn,nnoo,oo nn:nnoo:oo nn;nnoo;oo nn…nnoo…oo nn!nnoo!oo nn¡nnoo¡oo nn?nnoo?oo nn¿nnoo¿oo nn•nnoo•oo nn*nnoo*oo nn#nnoo#oo nn/nnoo/oo nn\nnoo\oo nn(nnoo(oo nn)nnoo)oo nn{nnoo{oo nn}nnoo}oo nn[nnoo[oo nn]nnoo]oo nn-nnoo-oo nn_nnoo_oo nn‚nnoo‚oo nn„nnoo„oo nn“nnoo“oo nn”nnoo”oo nn‘nnoo‘oo nn’nnoo’oo nn«nnoo«oo nn»nnoo»oo nn‹nnoo‹oo nn›nnoo›oo nn"nnoo"oo nn'nnoo'oo
'''
SPACING_STRINGS_LETTERS_UPPERCASE_PUNCTUATION = '''
NN.NNOO.OO NN,NNOO,OO NNNNOOOO NN;NNOO;OO NN…NNOO…OO NN!NNOO!OO NN¡NNOO¡OO NN?NNOO?OO NN¿NNOO¿OO NNNNOOOO NNNNOOOO NN#NNOO#OO NN/NNOO/OO NN\\NNOO\\OO NN(NNOO(OO NN)NNOO)OO NN{NNOO{OO NN}NNOO}OO NN[NNOO[OO NN]NNOO]OO NN-NNOO-OO NN_NNOO_OO NN‚NNOO‚OO NN„NNOO„OO NN“NNOO“OO NN”NNOO”OO NN‘NNOO‘OO NN’NNOO’OO NN«NNOO«OO NN»NNOO»OO NN‹NNOO‹OO NN›NNOO›OO NN"NNOO"OO NN'NNOO'OO
'''
SPACING_STRINGS_NUMBERS_BASIC = '''
008088088 0010088188 0020088288 0030088388 0040088488 0050088588 0060088688 0070088788 0090088988
'''
SPACING_STRINGS_NUMBERS_PI = '''
3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268
'''
SPACING_STRINGS_NUMBERS_PI = '''
3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268
'''
SPACING_STRINGS_NUMBERS_EXTRA = '''
$00 $10 $20 $30 $40 $50 $60 $70 $80 $90 £00 £10 £20 £30 £40 £50 £60 £70 £80 £90 00¢ 11¢ 22¢ 33¢ 44¢ 55¢ 66¢ 77¢ 88¢ 99¢ 00% 0‰ 0-0.0,0…0° 11% 1‰ 1-1.1,1…1° 12% 2‰ 2-2.2,2…2° 13% 3‰ 3-3.3,3…3° 14% 4‰ 4-4.4,4…4° 15% 5‰ 5-5.5,5…5° 16% 6‰ 6-6.6,6…6° 17% 7‰ 7-7.7,7…7° 18% 8‰ 8-8.8,8…8° 19% 9‰ 9-9.9,9…9°
'''

# DRAWS A GRID
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

# DRAW PAGE INFO
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

# NEW PAGE
def new_page():
    newPage(W, H)
    fill(1)
    rect(-2, -2, W+2, H+2)

# START DRAWBOT
newDrawing()
page_number = 0

# TEST FONTS
font("fonts/variable/RadioCanada-[wdth,wght].ttf")
for axis, data in listFontVariations().items():
    print((axis, data))
# for eachFontName in installedFonts():
#    print(eachFontName)

new_page() #--------------------------------------------------#
#grid() # TOGGLE FOR GRID VIEW
page_number += 1
draw_page_info(page_number)
# SIDEBAR #-------------------#
font("InputMonoCompressed-Regular")
fontSize(13)
stroke(None)
fill(0)
text("14pt Spacing Strings", (M, (U*29)+3))
text("Roman Condensed Light", (M, (U*28)+3))
text("Weight Axis: 300", (M, (U*27)+3))
text("Width Axis: 75", (M, (U*26)+3))
# MAIN TEXT #-----------------#
font("fonts/variable/RadioCanada-[wdth,wght].ttf")
fontVariations(wght = 300)
fontVariations(wdth = 75)
fontSize(14)
lineHeight(14*1.4)
textBox(SPACING_STRINGS_LETTERS_LOWERCASE+
        SPACING_STRINGS_LETTERS_UPPERCASE+
        SPACING_STRINGS_LETTERS_LOWERCASE_PUNCTUATION+
        SPACING_STRINGS_LETTERS_UPPERCASE_PUNCTUATION,
        (M+(U*10), M, U*30, U*29))

new_page() #--------------------------------------------------#
#grid() # TOGGLE FOR GRID VIEW
page_number += 1
draw_page_info(page_number)
# SIDEBAR #-------------------#
font("InputMonoCompressed-Regular")
fontSize(13)
stroke(None)
fill(0)
text("14pt Spacing Strings", (M, (U*29)+3))
text("Italic Condensed Light", (M, (U*28)+3))
text("Weight Axis: 300", (M, (U*27)+3))
text("Width Axis: 75", (M, (U*26)+3))
# MAIN TEXT #-----------------#
font("fonts/variable/RadioCanada-Italic[wdth,wght].ttf")
fontVariations(wght = 300)
fontVariations(wdth = 75)
fontSize(14)
lineHeight(14*1.4)
textBox(SPACING_STRINGS_LETTERS_LOWERCASE+
        SPACING_STRINGS_LETTERS_UPPERCASE+
        SPACING_STRINGS_LETTERS_LOWERCASE_PUNCTUATION+
        SPACING_STRINGS_LETTERS_UPPERCASE_PUNCTUATION,
        (M+(U*10), M, U*30, U*29))

new_page() #--------------------------------------------------#
#grid() # TOGGLE FOR GRID VIEW
page_number += 1
draw_page_info(page_number)
# SIDEBAR #-------------------#
font("InputMonoCompressed-Regular")
fontSize(13)
stroke(None)
fill(0)
text("14pt Spacing Strings", (M, (U*29)+3))
text("Roman Condensed Light", (M, (U*28)+3))
text("Weight Axis: 300", (M, (U*27)+3))
text("Width Axis: 75", (M, (U*26)+3))
# MAIN TEXT #-----------------#
font("fonts/variable/RadioCanada-[wdth,wght].ttf")
fontVariations(wght = 300)
fontVariations(wdth = 75)
fontSize(14)
lineHeight(14*1.4)
textBox(SPACING_STRINGS_NUMBERS_BASIC+
        SPACING_STRINGS_NUMBERS_PI+
        SPACING_STRINGS_NUMBERS_EXTRA,
        (M+(U*10), M, U*30, U*29))

new_page() #--------------------------------------------------#
#grid() # TOGGLE FOR GRID VIEW
page_number += 1
draw_page_info(page_number)
# SIDEBAR #-------------------#
font("InputMonoCompressed-Regular")
fontSize(13)
stroke(None)
fill(0)
text("14pt Spacing Strings", (M, (U*29)+3))
text("Italic Condensed Light", (M, (U*28)+3))
text("Weight Axis: 300", (M, (U*27)+3))
text("Width Axis: 75", (M, (U*26)+3))
# MAIN TEXT #-----------------#
font("fonts/variable/RadioCanada-Italic[wdth,wght].ttf")
fontVariations(wght = 300)
fontVariations(wdth = 75)
fontSize(14)
lineHeight(14*1.4)
textBox(SPACING_STRINGS_NUMBERS_BASIC+
        SPACING_STRINGS_NUMBERS_PI+
        SPACING_STRINGS_NUMBERS_EXTRA,
        (M+(U*10), M, U*30, U*29))

new_page() #--------------------------------------------------#
#grid() # TOGGLE FOR GRID VIEW
page_number += 1
draw_page_info(page_number)
# SIDEBAR #-------------------#
font("InputMonoCompressed-Regular")
fontSize(13)
stroke(None)
fill(0)
text("14pt Kern King", (M, (U*29)+3))
text("Roman Condensed Light", (M, (U*28)+3))
text("Weight Axis: 300", (M, (U*27)+3))
text("Width Axis: 75", (M, (U*26)+3))
# MAIN TEXT #-----------------#
font("fonts/variable/RadioCanada-[wdth,wght].ttf")
fontVariations(wght = 300)
fontVariations(wdth = 75)
lineHeight(14*1.4)
fontSize(14)
textBox(KERN_KING_LOWERCASE*2, (M+(U*10), M, U*30, U*29))

new_page() #--------------------------------------------------#
#grid() # TOGGLE FOR GRID VIEW
page_number += 1
draw_page_info(page_number)
# SIDEBAR #-------------------#
font("InputMonoCompressed-Regular")
fontSize(13)
stroke(None)
fill(0)
text("14pt Kern King", (M, (U*29)+3))
text("Italic Condensed Light", (M, (U*28)+3))
text("Weight Axis: 300", (M, (U*27)+3))
text("Width Axis: 75", (M, (U*26)+3))
# MAIN TEXT #-----------------#
font("fonts/variable/RadioCanada-Italic[wdth,wght].ttf")
fontVariations(wght = 300)
fontVariations(wdth = 75)
lineHeight(14*1.4)
fontSize(14)
textBox(KERN_KING_LOWERCASE*2, (M+(U*10), M, U*30, U*29))

new_page() #--------------------------------------------------#
#grid() # TOGGLE FOR GRID VIEW
page_number += 1
draw_page_info(page_number)
# SIDEBAR #-------------------#
font("InputMonoCompressed-Regular")
fontSize(13)
stroke(None)
fill(0)
text("14pt Kern King", (M, (U*29)+3))
text("Roman Condensed Light", (M, (U*28)+3))
text("Weight Axis: 300", (M, (U*27)+3))
text("Width Axis: 75", (M, (U*26)+3))
# MAIN TEXT #-----------------#
font("fonts/variable/RadioCanada-[wdth,wght].ttf")
fontVariations(wght = 300)
fontVariations(wdth = 75)
lineHeight(14*1.4)
fontSize(14)
textBox(KERN_KING_UPPERCASE, (M+(U*10), M, U*30, U*29))

new_page() #--------------------------------------------------#
#grid() # TOGGLE FOR GRID VIEW
page_number += 1
draw_page_info(page_number)
# SIDEBAR #-------------------#
font("InputMonoCompressed-Regular")
fontSize(13)
stroke(None)
fill(0)
text("14pt Kern King", (M, (U*29)+3))
text("Italic Condensed Light", (M, (U*28)+3))
text("Weight Axis: 300", (M, (U*27)+3))
text("Width Axis: 75", (M, (U*26)+3))
# MAIN TEXT #-----------------#
font("fonts/variable/RadioCanada-Italic[wdth,wght].ttf")
fontVariations(wght = 300)
fontVariations(wdth = 75)
lineHeight(14*1.4)
fontSize(14)
textBox(KERN_KING_UPPERCASE, (M+(U*10), M, U*30, U*29))

new_page() #--------------------------------------------------#
#grid() # TOGGLE FOR GRID VIEW
page_number += 1
draw_page_info(page_number)
# SIDEBAR #-------------------#
font("InputMonoCompressed-Regular")
fontSize(13)
stroke(None)
fill(0)
text("14pt Kern King", (M, (U*29)+3))
text("Roman Condensed Light", (M, (U*28)+3))
text("Weight Axis: 300", (M, (U*27)+3))
text("Width Axis: 75", (M, (U*26)+3))
# MAIN TEXT #-----------------#
font("fonts/variable/RadioCanada-[wdth,wght].ttf")
fontVariations(wght = 300)
fontVariations(wdth = 75)
lineHeight(14*1.4)
fontSize(14)
textBox(KERN_KING_SENTENCECASE*2, (M+(U*10), M, U*30, U*29))

new_page() #--------------------------------------------------#
#grid() # TOGGLE FOR GRID VIEW
page_number += 1
draw_page_info(page_number)
# SIDEBAR #-------------------#
font("InputMonoCompressed-Regular")
fontSize(13)
stroke(None)
fill(0)
text("14pt Kern King", (M, (U*29)+3))
text("Italic Condensed Light", (M, (U*28)+3))
text("Weight Axis: 300", (M, (U*27)+3))
text("Width Axis: 75", (M, (U*26)+3))
# MAIN TEXT #-----------------#
font("fonts/variable/RadioCanada-Italic[wdth,wght].ttf")
fontVariations(wght = 300)
fontVariations(wdth = 75)
lineHeight(14*1.4)
fontSize(14)
textBox(KERN_KING_SENTENCECASE*2, (M+(U*10), M, U*30, U*29))

# Saving and post-processing #--------------------------------#
saveImage("documentation/proofs/spacing-proof.pdf")
print("\nDRAWBOT: Updated Spacing Proof")
