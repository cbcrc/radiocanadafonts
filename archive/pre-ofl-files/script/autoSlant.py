from glyphNameFormatter.data import unicode2name_AGD
import string

font = CurrentFont()

charset = string.uppercase+string.lowercase

for a in range(8, 16, 2):
    
    newFont = NewFont(font.info.familyName, font.info.styleName, showUI=False)
    
    for c in string.printable:
        
        glyph = unicode2name_AGD[ord(c)]
        
        if glyph in font:
            
            newGlyph = newFont.insertGlyph(font[glyph])
            
            newGlyph.skew(a)
    
    newFont.info.update(font.info)
    newFont.info.italicAngle = -a
    
    ext = "-slant-%s.ufo" % a
    savePath = font.path.replace(".ufo", ext)
    newFont.save(savePath)