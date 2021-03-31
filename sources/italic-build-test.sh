# !/bin/bash

set -e

echo "\n**** Generating VFs ****\n"
echo "\n**** Generating Radio Canada Italic Fonts ****\n"
mkdir fonts/temp
fontmake \
    -m sources/Radio-Canada-Italic.designspace \
    -o variable \
    --output-path fonts/temp/RadioCanada-Italic[wdth,wght].ttf
#    --output-path fonts/variable/RadioCanada-Italic[wdth,wght].ttf \
#    --verbose DEBUG 
#    --no-production-names \

echo "\n**** Done ****\n"
