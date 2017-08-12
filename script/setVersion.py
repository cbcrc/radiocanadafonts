for font in AllFonts():
    
    font.info.versionMajor = 1
    font.info.versionMinor = 2
    
    print "%s.%s" % (font.info.versionMajor, font.info.versionMinor)
    
    font.save()