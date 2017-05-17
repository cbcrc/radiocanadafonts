for font in AllFonts():
    
    font.info.versionMajor = 0
    font.info.versionMinor = 5
    
    print "%s.%s" % (font.info.versionMajor, font.info.versionMinor)
    
    font.save()