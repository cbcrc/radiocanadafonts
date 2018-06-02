#!/bin/sh

# clean existing build artifacts
rm -rf desktop/
mkdir desktop/

family="Radio-Canada"
styles="Light Regular Medium Bold LightItalic Italic MediumItalic BoldItalic"

for s in $styles
do
  cp master_otf/$family-$s.otf desktop/$family-$s.otf
  autohint desktop/$family-$s.otf
done

family="Radio-Canada-Condensed"
styles="Regular Bold Italic BoldItalic"

for s in $styles
do
  cp master_otf/$family-$s.otf desktop/$family-$s.otf
  autohint desktop/$family-$s.otf
done
