glyphs = set()

for glyph in CurrentFont():
    
    for contour in glyph.contours:
        
        for segment in contour.segments:
            
            if segment.onCurve.y in [-194, -9, 524, 699, 729]:
                
                glyphs.add(glyph)
                #glyph.mark = (1, 0, 0, 0.5)
                print glyph
print len(glyphs)
