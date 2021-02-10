# !/bin/bash

set -e

echo "\n**** Generating VFs ****\n"
mkdir -p fonts
fontmake -m sources/Radio-Canada.designspace -o variable --no-production-names --output-path fonts/RadioCanada[wdth,wght].ttf
echo "\n**** Post Processing VFs ****\n"
echo "\n**** Done ****\n"
