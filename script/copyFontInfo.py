fonts = AllFonts()

font = fonts[0]
fonts = fonts[1:]

#print font.info.asDict()

for f in fonts:
    f.info.versionMajor = font.info.versionMajor
    f.info.versionMinor = font.info.versionMinor
    
    f.info.copyright = font.info.copyright

    f.info.openTypeNameDesigner = font.info.openTypeNameDesigner
    f.info.openTypeNameDesignerURL = font.info.openTypeNameDesignerURL

    f.info.openTypeNameManufacturer = font.info.openTypeNameManufacturer
    f.info.openTypeNameManufacturerURL = font.info.openTypeNameManufacturerURL

