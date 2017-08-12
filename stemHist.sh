#!/bin/sh

family="Radio-Canada"
styles="Light Regular Medium Bold LightItalic Italic MediumItalic BoldItalic"

for s in $styles
do
	stemHist master_otf/$family-$s.otf
	mv master_otf/$family-$s.otf.hstm.txt stem_hist/$family-$s.otf.hstm.txt
done

family="Radio-Canada-Condensed"
styles="Regular Bold Italic BoldItalic"

for s in $styles
do
	stemHist master_otf/$family-$s.otf
	mv master_otf/$family-$s.otf.hstm.txt stem_hist/$family-$s.otf.hstm.txt
done