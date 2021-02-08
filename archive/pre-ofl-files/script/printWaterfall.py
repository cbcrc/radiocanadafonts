import glyphNameFormatter as gn

charset = ""

font = CurrentFont()
for name in font.glyphOrder:
    glyph = font[name]
    unicodes = glyph.unicodes
    try:    
        charset += gn.unicodeToChar(unicodes[0])
    except IndexError:
        pass

print charset
"""
<span style='font-feature-settings: "ss01", "ss02";'>IJaąuų</span>
"""