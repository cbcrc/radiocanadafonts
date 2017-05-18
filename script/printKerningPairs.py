from fontTools.agl import AGL2UV

font = CurrentFont()


for pair in font.kerning.keys():
    left, right = pair
    
    if left.startswith("@"):
        left = font.groups[left][0]
    if right.startswith("@"):
        right = font.groups[right][0]
    
    if left in AGL2UV and right in AGL2UV:
        print unichr(AGL2UV[left]) + unichr(AGL2UV[right])