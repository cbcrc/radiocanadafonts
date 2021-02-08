for font in AllFonts():
    
    font.info.openTypeHheaAscender = 950
    font.info.openTypeHheaDescender = -250
    
    font.info.openTypeOS2TypoAscender = 950
    font.info.openTypeOS2TypoDescender = -250
    
    font.info.openTypeOS2WinAscent = 950
    font.info.openTypeOS2WinDescent = 250
    
    font.save()