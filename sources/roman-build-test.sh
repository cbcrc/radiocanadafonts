# !/bin/bash

set -e

echo "\n**** Generating VFs ****\n"
echo "\n**** Generating Radio Canada Roman ****\n"
mkdir fonts/temp
fontmake \
    -m sources/Radio-Canada.designspace \
    -o variable \
    --no-production-names \
    --output-path fonts/temp/RadioCanada-[wdth,wght].ttf

echo "\n**** Done ****\n"
