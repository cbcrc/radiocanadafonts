#!/bin/sh

# clean existing build artifacts
rm -rf web/
mkdir web/

family="Radio-Canada"
styles="Light Regular Medium Bold LightItalic Italic MediumItalic BoldItalic"

# --fallback-script --control-file --no-info -verbose --strong-stem-width (grayscale, GDI, DirectWrite ClearType) --windows-compatibility

for s in $styles
do
  ttfautohint -f latn -m instructions/$family-$s.txt -n -v -w gGD -W master_ttf/$family-$s.ttf web/$family-$s.ttf
  
  # http for RootString wildcard?
  mkeot master_ttf/$family-$s.ttf http > web/$family-$s.eot
  
  sfnt2woff -v 1.0 -m woff-metadata.xml master_otf/$family-$s.otf
  mv master_otf/$family-$s.woff web/$family-$s.woff
  
  woff2_compress master_otf/$family-$s.otf 
  mv master_otf/$family-$s.woff2 web/$family-$s.woff2
done

family="Radio-Canada-Condensed"
styles="Regular Bold Italic BoldItalic"

# --fallback-script --control-file --no-info -verbose --strong-stem-width (grayscale, GDI, DirectWrite ClearType) --windows-compatibility

for s in $styles
do
  ttfautohint -f latn -m instructions/$family-$s.txt -n -v -w gGD -W master_ttf/$family-$s.ttf web/$family-$s.ttf
  
  # http for RootString wildcard?
  mkeot master_ttf/$family-$s.ttf http > web/$family-$s.eot
  
  sfnt2woff -v 1.0 -m woff-metadata.xml master_otf/$family-$s.otf
  mv master_otf/$family-$s.woff web/$family-$s.woff
  
  woff2_compress master_otf/$family-$s.otf 
  mv master_otf/$family-$s.woff2 web/$family-$s.woff2
done