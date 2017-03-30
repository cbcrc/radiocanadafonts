font = CurrentFont()

for g in font.selection:
    
    if "_" in g:
        components = g.split("_")
    elif len(g) == 2:
        components = g[0], g[1]
    else:
        break
        
    glyph = font[g]
    
    glyph.clear()
    
    x = 0
    
    for component in components:
        
        glyph.appendComponent(component, offset=(x, 0))
        x += font[component].width
    
    glyph.width = x
    
    glyph.mark = (1, 0, 0, 1)
