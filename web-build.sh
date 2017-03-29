#!/bin/sh

family="Radio-Canada"
romanWeights="Light Regular Bold"

# clean existing build artifacts
rm -rf web/
mkdir web/

# --fallback-script --control-file --no-info -verbose --strong-stem-width (grayscale, GDI, DirectWrite ClearType) --windows-compatibility

for w in $romanWeights
do
  ttfautohint -f latn -m instructions/$family-$w.txt -n -v -w gGD -W master_ttf/$family-$w.ttf web/$family-$w.ttf
  
  # http for RootString wildcard?
  mkeot master_ttf/$family-$w.ttf http > web/$family-$w.eot
  
  sfnt2woff -v 1.0 -m woff-metadata.xml master_otf/$family-$w.otf
  mv master_otf/$family-$w.woff web/$family-$w.woff
  
  woff2_compress master_otf/$family-$w.otf 
  mv master_otf/$family-$w.woff2 web/$family-$w.woff2
done