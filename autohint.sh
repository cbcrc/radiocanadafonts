#!/bin/sh

family="Radio-Canada"
styles="Light Regular Bold LightItalic Italic BoldItalic"

# clean existing build artifacts
rm -rf desktop/
mkdir desktop/

for s in $styles
do
  cp master_otf/$family-$s.otf desktop/$family-$s.otf
  autohint desktop/$family-$s.otf
done