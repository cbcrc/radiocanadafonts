#!/bin/sh

family="Radio-Canada"
styles="Light Regular Bold LightItalic Italic BoldItalic Condensed CondensedBold"

for s in $styles
do
	stemHist master_otf/$family-$s.otf
	mv master_otf/$family-$s.otf.hstm.txt stem_hist/$family-$s.otf.hstm.txt
done