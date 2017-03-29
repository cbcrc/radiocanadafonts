#!/bin/sh

family=RC
romanWeights="Light Regular Bold"

# clean existing build artifacts
rm -rf DESKTOP/
mkdir DESKTOP/ DESKTOP/OTF/ DESKTOP/TTF/


for w in $romanWeights
do
  checkOutlines Roman/$w/$family-$w.ufo > log/$family-$w-checkOutlines.txt
  autohint -all -log log/$family-$w-autohint.txt Roman/$w/$family-$w.ufo
  makeotf -f Roman/$w/$family-$w.ufo -r -o DESKTOP/OTF/$family-$w.otf
  makeotf -f Roman/$w/$family-$w.ttf -r -o DESKTOP/TTF/$family-$w.ttf
  rm Roman/$w/current.fpr # remove default options file from the source tree after building
  stemHist -g A-Z,a-z -o log/$family-$w DESKTOP/OTF/$family-$w.otf
done
