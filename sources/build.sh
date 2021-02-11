# !/bin/bash

set -e

echo "\n**** Building Radio Canada Fonts ****\n"
mkdir -p fonts fonts/ttf fonts/variable

echo "\n**** Generating VFs ****\n"
echo "\n**** Generating Radio Canada Roman ****\n"
fontmake \
    -m sources/Radio-Canada.designspace \
    -o variable \
    --no-production-names \
    --output-path fonts/variable/RadioCanada-[wdth,wght].ttf
echo "\n**** Generating Radio Canada Italic ****\n"
#fontmake \
#    -m sources/Radio-Canada-Italic.designspace \
#    -o variable \
#    --no-production-names \
#    --output-path fonts/variable/RadioCanada-Italic-[wdth,wght].ttf

echo "\n**** Post Processing VFs ****\n"
vfs=$(ls fonts/variable/*.ttf)
echo $vfs
for vf in $vfs
do
    echo $vf
    #gftools fix-dsig -f $vf;
    #ttfautohint-vf --stem-width-mode nnn $vf "$vf.fix";
    #mv "$vf.fix" $vf;
done

echo "\n**** Done ****\n"
