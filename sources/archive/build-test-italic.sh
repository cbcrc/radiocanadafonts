# !/bin/bash

set -e

fontmake \
    -m sources/Radio-Canada-Italic.designspace \
    -o variable \
    --no-production-names \
    --output-path fonts/variable/Radio-Canada-Italic[wdth,wght].ttf
#    --verbose DEBUG 

echo "\n**** Done ****\n"
