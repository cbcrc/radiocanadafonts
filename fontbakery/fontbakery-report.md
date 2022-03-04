## Fontbakery report

Fontbakery version: 0.8.7

<details><summary><b>[1] Family checks</b></summary><div><details><summary>🔥 <b>FAIL:</b> Ensure Italic styles have Roman counterparts.</summary><div>
* [com.google.fonts/check/family/italics_have_roman_counterparts](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/family/italics_have_roman_counterparts)

* 🔥 **FAIL** Italics missing a Roman counterpart: fonts/ttf/RadioCanadaCondensed-MediumItalic.ttf, fonts/ttf/RadioCanadaCondensed-LightItalic.ttf, fonts/ttf/RadioCanadaCondensed-BoldItalic.ttf, fonts/ttf/RadioCanadaCondensed-SemiBoldItalic.ttf and fonts/ttf/RadioCanadaCondensed-Italic.ttf [code: missing-roman]
</div></details><br></div></details><details><summary><b>[12] RadioCanada-SemiBold.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary><div>
* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary><div>
* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary><div>
* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + ij
	- ij + f
	- f + l
	- l + f
	- i + ij
	- ij + l
	- uni0295 + uni0315
	- uni0315 + uni02B7
	- uni1E5B + uni0315

   [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary><div>
* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Radio Canada SemiBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary><div>
* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary><div>
* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- nine.lf
	- breve.cap
	- ring.cap
	- one.lf
	- dotbelow
	- zero.lf
	- uni030C.alt
	- eight.lf
	- six.lf
	- dollar.BRACKET.100 
	- And 15 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary><div>
* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: ohorn	Contours detected: 3	Expected: 2
	- Glyph name: Uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uni01EA	Contours detected: 3	Expected: 2
	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3
	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3 
	- And 39 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks.</summary><div>
* [com.google.fonts/check/dotted_circle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle)

* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary><div>
* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* six (U+0036): X=448.0,Y=689.0 (should be at cap-height 690?)
	* nine (U+0039): X=152.0,Y=1.0 (should be at baseline 0?)
	* e (U+0065): X=408.0,Y=1.0 (should be at baseline 0?)
	* j (U+006A): X=80.0,Y=1.0 (should be at baseline 0?)
	* s (U+0073): X=352.0,Y=520.0 (should be at x-height 522?)
	* Aring (U+00C5): X=406.5,Y=689.0 (should be at cap-height 690?)
	* Aring (U+00C5): X=248.0,Y=689.0 (should be at cap-height 690?)
	* aring (U+00E5): X=153.0,Y=689.0 (should be at cap-height 690?)
	* aring (U+00E5): X=376.0,Y=689.0 (should be at cap-height 690?)
	* aring (U+00E5): X=153.0,Y=689.0 (should be at cap-height 690?) and 87 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary><div>
* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* at (U+0040) contains a short segment B<<712.0,448.0>-<708.0,426.0>-<706.5,409.0>>
	* at (U+0040) contains a short segment B<<706.5,409.0>-<705.0,392.0>-<705.0,371.0>>
	* a (U+0061) contains a short segment L<<346.0,312.0>--<346.0,317.0>>
	* f (U+0066) contains a short segment L<<107.0,522.0>--<107.0,534.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<563.0,103.0>-<572.0,103.0>-<582.0,106.0>>
	* agrave (U+00E0) contains a short segment L<<346.0,312.0>--<346.0,317.0>>
	* aacute (U+00E1) contains a short segment L<<346.0,312.0>--<346.0,317.0>>
	* acircumflex (U+00E2) contains a short segment L<<346.0,312.0>--<346.0,317.0>>
	* atilde (U+00E3) contains a short segment L<<346.0,312.0>--<346.0,317.0>>
	* adieresis (U+00E4) contains a short segment L<<346.0,312.0>--<346.0,317.0>> and 43 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary><div>
* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<123.0,244.0>--<101.0,522.0>> -> L<<101.0,522.0>--<101.0,690.0>>
	* exclam (U+0021): L<<246.0,690.0>--<246.0,522.0>> -> L<<246.0,522.0>--<223.0,244.0>>
	* exclamdown (U+00A1): L<<101.0,-185.0>--<101.0,0.0>> -> L<<101.0,0.0>--<123.0,278.0>> and exclamdown (U+00A1): L<<223.0,278.0>--<246.0,0.0>> -> L<<246.0,0.0>--<246.0,-185.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary><div>
* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni20A9 (U+20A9): L<<173.0,306.0>--<185.0,170.0>>/L<<185.0,170.0>--<199.0,306.0>> = 10.919843675814004
	* uni20A9 (U+20A9): L<<310.0,402.0>--<298.0,515.0>>/L<<298.0,515.0>--<287.0,402.0>> = 11.621736052038148 and uni20A9 (U+20A9): L<<399.0,306.0>--<413.0,167.0>>/L<<413.0,167.0>--<426.0,306.0>> = 11.094457848941124 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[11] RadioCanada-LightItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary><div>
* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary><div>
* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary><div>
* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l
	- uni0295 + uni0315
	- uni0315 + uni02B7
	- uni1E5B + uni0315

   [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary><div>
* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary><div>
* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- two.pl
	- zero.pl
	- nine.pl
	- four.pl
	- eight.pl
	- six.pl
	- three.pl
	- five.pl
	- one.pl
	- ring_acute.cap 
	- And 5 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary><div>
* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: ohorn	Contours detected: 3	Expected: 2
	- Glyph name: Uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uni01EA	Contours detected: 3	Expected: 2
	- Glyph name: uni01EB	Contours detected: 3	Expected: 2
	- Glyph name: uni023A	Contours detected: 4	Expected: 3 
	- And 40 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks.</summary><div>
* [com.google.fonts/check/dotted_circle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle)

* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary><div>
* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* Q (U+0051): X=345.0,Y=-1.0 (should be at baseline 0?)
	* f (U+0066): X=239.0,Y=689.0 (should be at cap-height 690?)
	* i (U+0069): X=253.0,Y=691.0 (should be at cap-height 690?)
	* j (U+006A): X=253.0,Y=691.0 (should be at cap-height 690?)
	* t (U+0074): X=238.5,Y=-1.0 (should be at baseline 0?)
	* braceright (U+007D): X=87.5,Y=1.5 (should be at baseline 0?)
	* ordfeminine (U+00AA): X=356.5,Y=688.0 (should be at cap-height 690?)
	* ordfeminine (U+00AA): X=413.0,Y=691.0 (should be at cap-height 690?)
	* ordfeminine (U+00AA): X=464.0,Y=691.0 (should be at cap-height 690?)
	* acircumflex (U+00E2): X=381.0,Y=689.0 (should be at cap-height 690?) and 82 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary><div>
* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* dollar (U+0024) contains a short segment L<<368.0,698.0>--<368.0,698.0>>
	* three (U+0033) contains a short segment L<<290.0,396.0>--<294.0,396.0>>
	* greater (U+003E) contains a short segment L<<520.0,302.0>--<520.0,302.0>>
	* logicalnot (U+00AC) contains a short segment L<<517.0,263.0>--<517.0,263.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<458.0,44.0>-<466.0,44.0>-<471.5,45.5>>
	* uni03BC.math (U+00B5) contains a short segment B<<471.5,45.5>-<477.0,47.0>-<482.0,48.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<472.0,0.0>-<463.0,-4.0>-<455.0,-6.0>>
	* Eng (U+014A) contains a short segment B<<325.0,-127.0>-<336.0,-132.0>-<351.0,-136.0>>
	* Eng (U+014A) contains a short segment L<<483.0,0.0>--<483.0,0.0>>
	* uni0190 (U+0190) contains a short segment L<<434.0,381.0>--<432.0,370.0>> and 27 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary><div>
* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<103.0,180.0>--<164.0,510.0>> -> L<<164.0,510.0>--<203.0,690.0>>
	* exclam (U+0021): L<<265.0,690.0>--<226.0,510.0>> -> L<<226.0,510.0>--<147.0,180.0>>
	* exclamdown (U+00A1): L<<18.0,-185.0>--<58.0,0.0>> -> L<<58.0,0.0>--<137.0,330.0>>
	* exclamdown (U+00A1): L<<181.0,330.0>--<120.0,0.0>> -> L<<120.0,0.0>--<80.0,-185.0>>
	* less (U+003C): L<<80.0,264.0>--<88.0,300.0>> -> L<<88.0,300.0>--<91.0,316.0>> and uni0190 (U+0190): L<<432.0,370.0>--<428.0,352.0>> -> L<<428.0,352.0>--<426.0,342.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary><div>
* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni023A (U+023A): L<<150.0,226.0>--<93.0,123.0>>/L<<93.0,123.0>--<172.0,226.0>> = 8.527799202996924 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[10] RadioCanada-MediumItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary><div>
* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary><div>
* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary><div>
* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l
	- uni0295 + uni0315
	- uni0315 + uni02B7
	- uni1E5B + uni0315

   [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary><div>
* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary><div>
* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- two.pl
	- zero.pl
	- nine.pl
	- four.pl
	- eight.pl
	- six.pl
	- three.pl
	- five.pl
	- one.pl
	- ring_acute.cap 
	- And 5 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary><div>
* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: ohorn	Contours detected: 3	Expected: 2
	- Glyph name: Uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uni01EA	Contours detected: 3	Expected: 2
	- Glyph name: uni01EB	Contours detected: 3	Expected: 2
	- Glyph name: uni02BA	Contours detected: 1	Expected: 2 
	- And 38 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks.</summary><div>
* [com.google.fonts/check/dotted_circle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle)

* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary><div>
* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* R (U+0052) contains a short segment B<<310.0,255.0>-<303.0,255.0>-<297.0,255.0>>
	* m (U+006D) contains a short segment B<<708.0,314.0>-<710.0,325.0>-<711.0,335.0>>
	* m (U+006D) contains a short segment B<<711.0,335.0>-<712.0,345.0>-<712.0,354.0>>
	* m (U+006D) contains a short segment B<<397.0,314.0>-<399.0,325.0>-<400.5,335.0>>
	* m (U+006D) contains a short segment B<<400.5,335.0>-<402.0,345.0>-<402.0,354.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<517.0,85.0>-<523.0,85.0>-<528.0,86.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<528.0,86.0>-<533.0,87.0>-<538.0,89.0>>
	* ae (U+00E6) contains a short segment B<<361.0,339.0>-<362.0,348.0>-<362.0,355.0>>
	* hbar (U+0127) contains a short segment B<<426.0,314.0>-<428.0,325.0>-<429.5,335.0>>
	* hbar (U+0127) contains a short segment B<<429.5,335.0>-<431.0,345.0>-<431.0,354.0>> and 31 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary><div>
* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<107.0,226.0>--<153.0,519.0>> -> L<<153.0,519.0>--<189.0,690.0>>
	* exclam (U+0021): L<<312.0,690.0>--<275.0,519.0>> -> L<<275.0,519.0>--<192.0,226.0>>
	* exclamdown (U+00A1): L<<210.0,292.0>--<166.0,0.0>> -> L<<166.0,0.0>--<127.0,-185.0>>
	* exclamdown (U+00A1): L<<4.0,-185.0>--<43.0,0.0>> -> L<<43.0,0.0>--<125.0,292.0>>
	* greater (U+003E): L<<535.0,335.0>--<521.0,270.0>> -> L<<521.0,270.0>--<515.0,242.0>>
	* less (U+003C): L<<67.0,242.0>--<72.0,267.0>> -> L<<72.0,267.0>--<87.0,335.0>>
	* trademark (U+2122): L<<773.0,690.0>--<831.0,690.0>> -> L<<831.0,690.0>--<831.0,690.0>> and trademark (U+2122): L<<831.0,690.0>--<831.0,690.0>> -> L<<831.0,690.0>--<911.0,690.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary><div>
* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)

* ⚠ **WARN** The following glyphs have jaggy segments:
	* greaterequal (U+2265): L<<551.0,403.0>--<551.0,404.0>>/L<<551.0,404.0>--<532.0,317.0>> = 12.319445256636591
	* greaterequal (U+2265): L<<555.0,421.0>--<551.0,403.0>>/L<<551.0,403.0>--<551.0,404.0>> = 12.528807709151492
	* litre (U+2113): L<<91.0,166.0>--<91.0,166.0>>/B<<91.0,166.0>-<64.0,160.0>-<37.0,155.0>> = 12.528807709151492
	* uni20A9 (U+20A9): L<<175.0,313.0>--<162.0,171.0>>/L<<162.0,171.0>--<210.0,313.0>> = 13.445894556636892
	* uni20A9 (U+20A9): L<<346.0,400.0>--<356.0,524.0>>/L<<356.0,524.0>--<314.0,400.0>> = 14.101088556439166 and uni20A9 (U+20A9): L<<412.0,313.0>--<400.0,170.0>>/L<<400.0,170.0>--<448.0,313.0>> = 13.758266618296407 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[11] RadioCanada-SemiBoldItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary><div>
* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary><div>
* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary><div>
* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l
	- uni0295 + uni0315
	- uni0315 + uni02B7
	- uni1E5B + uni0315

   [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary><div>
* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary><div>
* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- two.pl
	- zero.pl
	- nine.pl
	- four.pl
	- eight.pl
	- six.pl
	- three.pl
	- five.pl
	- one.pl
	- ring_acute.cap 
	- And 5 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary><div>
* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: ohorn	Contours detected: 3	Expected: 2
	- Glyph name: Uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uni01EA	Contours detected: 3	Expected: 2
	- Glyph name: uni01EB	Contours detected: 3	Expected: 2
	- Glyph name: uni02BA	Contours detected: 1	Expected: 2 
	- And 42 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks.</summary><div>
* [com.google.fonts/check/dotted_circle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle)

* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary><div>
* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=446.0,Y=689.0 (should be at cap-height 690?)
	* parenright (U+0029): X=-95.0,Y=-253.0 (should be at descender -255?)
	* six (U+0036): X=539.5,Y=689.5 (should be at cap-height 690?)
	* nine (U+0039): X=93.0,Y=1.0 (should be at baseline 0?)
	* i (U+0069): X=303.0,Y=688.0 (should be at cap-height 690?)
	* j (U+006A): X=303.0,Y=688.0 (should be at cap-height 690?)
	* braceright (U+007D): X=180.0,Y=691.5 (should be at cap-height 690?)
	* dieresis (U+00A8): X=-66.0,Y=690.5 (should be at cap-height 690?)
	* dieresis (U+00A8): X=138.0,Y=690.5 (should be at cap-height 690?)
	* uni03BC.math (U+00B5): X=169.0,Y=1.5 (should be at baseline 0?) and 57 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary><div>
* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* R (U+0052) contains a short segment B<<305.0,247.0>-<301.0,247.0>-<297.0,247.0>>
	* m (U+006D) contains a short segment B<<705.0,314.0>-<707.0,325.0>-<708.0,333.5>>
	* m (U+006D) contains a short segment B<<708.0,333.5>-<709.0,342.0>-<709.0,351.0>>
	* m (U+006D) contains a short segment B<<392.0,314.0>-<394.0,325.0>-<395.0,333.5>>
	* m (U+006D) contains a short segment B<<395.0,333.5>-<396.0,342.0>-<396.0,351.0>>
	* Oslash (U+00D8) contains a short segment B<<195.0,265.0>-<195.0,265.0>-<195.0,263.0>>
	* ae (U+00E6) contains a short segment B<<357.0,336.0>-<358.0,344.0>-<358.0,349.0>>
	* ae (U+00E6) contains a short segment B<<482.0,219.0>-<476.0,219.0>-<470.0,219.0>>
	* ae (U+00E6) contains a short segment B<<470.0,219.0>-<469.0,209.0>-<469.0,199.0>>
	* hbar (U+0127) contains a short segment B<<421.0,314.0>-<423.0,325.0>-<424.0,333.5>> and 44 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary><div>
* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<107.0,243.0>--<148.0,522.0>> -> L<<148.0,522.0>--<183.0,690.0>>
	* exclam (U+0021): L<<328.0,690.0>--<292.0,522.0>> -> L<<292.0,522.0>--<207.0,243.0>>
	* exclamdown (U+00A1): L<<-3.0,-185.0>--<36.0,0.0>> -> L<<36.0,0.0>--<120.0,279.0>>
	* exclamdown (U+00A1): L<<220.0,279.0>--<181.0,0.0>> -> L<<181.0,0.0>--<142.0,-185.0>>
	* greater (U+003E): L<<539.0,342.0>--<527.0,284.0>> -> L<<527.0,284.0>--<517.0,235.0>>
	* less (U+003C): L<<63.0,235.0>--<72.0,276.0>> -> L<<72.0,276.0>--<86.0,342.0>>
	* trademark (U+2122): L<<776.0,689.0>--<839.0,690.0>> -> L<<839.0,690.0>--<839.0,690.0>> and trademark (U+2122): L<<839.0,690.0>--<839.0,690.0>> -> L<<839.0,690.0>--<929.0,690.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary><div>
* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni023A (U+023A): L<<369.0,503.0>--<243.0,273.0>>/L<<243.0,273.0>--<377.0,439.0>> = 10.196394317688243
	* uni20A9 (U+20A9): L<<184.0,306.0>--<167.0,170.0>>/L<<167.0,170.0>--<209.0,306.0>> = 10.036902453963481
	* uni20A9 (U+20A9): L<<341.0,402.0>--<353.0,515.0>>/L<<353.0,515.0>--<318.0,402.0>> = 11.147768731819275 and uni20A9 (U+20A9): L<<409.0,306.0>--<394.0,167.0>>/L<<394.0,167.0>--<436.0,306.0>> = 10.653463206281126 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] RadioCanadaCondensed-MediumItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary><div>
* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary><div>
* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary><div>
* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l
	- uni0295 + uni0315
	- uni0315 + uni02B7
	- uni1E5B + uni0315

   [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary><div>
* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Radio Canada Condensed Medium' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary><div>
* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary><div>
* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- two.pl
	- zero.pl
	- nine.pl
	- four.pl
	- eight.pl
	- six.pl
	- three.pl
	- five.pl
	- one.pl
	- ring_acute.cap 
	- And 5 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary><div>
* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: ohorn	Contours detected: 3	Expected: 2
	- Glyph name: Uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uni01EA	Contours detected: 3	Expected: 2
	- Glyph name: uni01EB	Contours detected: 3	Expected: 2
	- Glyph name: uni02BA	Contours detected: 1	Expected: 2 
	- And 38 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks.</summary><div>
* [com.google.fonts/check/dotted_circle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle)

* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary><div>
* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=388.0,Y=691.0 (should be at cap-height 690?)
	* dollar (U+0024): X=148.0,Y=-2.0 (should be at baseline 0?)
	* six (U+0036): X=452.5,Y=690.5 (should be at cap-height 690?)
	* nine (U+0039): X=74.5,Y=-0.5 (should be at baseline 0?)
	* at (U+0040): X=326.0,Y=-1.0 (should be at baseline 0?)
	* g (U+0067): X=328.0,Y=517.5 (should be at x-height 519?)
	* uni03BC.math (U+00B5): X=436.0,Y=-1.0 (should be at baseline 0?)
	* onequarter (U+00BC): X=295.0,Y=691.0 (should be at cap-height 690?)
	* onequarter (U+00BC): X=355.0,Y=691.0 (should be at cap-height 690?)
	* onehalf (U+00BD): X=295.0,Y=691.0 (should be at cap-height 690?) and 67 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary><div>
* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* uni03BC.math (U+00B5) contains a short segment B<<440.0,84.0>-<445.0,84.0>-<449.0,85.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<449.0,85.0>-<453.0,86.0>-<456.0,87.0>>
	* oe (U+0153) contains a short segment B<<437.0,225.0>-<430.0,225.0>-<423.0,225.0>>
	* uni0190 (U+0190) contains a short segment L<<433.0,400.0>--<429.0,382.0>>
	* uni0190 (U+0190) contains a short segment L<<429.0,382.0>--<429.0,382.0>>
	* uni01E5 (U+01E5) contains a short segment B<<272.0,1.0>-<273.0,6.0>-<274.0,11.0>>
	* uni01E5 (U+01E5) contains a short segment B<<380.0,14.0>-<378.0,7.0>-<377.0,1.0>>
	* uni023C (U+023C) contains a short segment B<<133.0,199.0>-<133.0,197.0>-<133.0,198.0>>
	* uni023E (U+023E) contains a short segment L<<536.0,690.0>--<539.0,690.0>>
	* uni026C (U+026C) contains a short segment L<<202.0,403.0>--<201.0,403.0>> and 8 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary><div>
* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<289.0,690.0>--<252.0,518.0>> -> L<<252.0,518.0>--<170.0,226.0>>
	* exclam (U+0021): L<<93.0,226.0>--<136.0,518.0>> -> L<<136.0,518.0>--<172.0,690.0>>
	* exclamdown (U+00A1): L<<-13.0,-185.0>--<26.0,0.0>> -> L<<26.0,0.0>--<107.0,292.0>> and exclamdown (U+00A1): L<<185.0,292.0>--<141.0,0.0>> -> L<<141.0,0.0>--<102.0,-185.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary><div>
* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni023A (U+023A): L<<315.0,529.0>--<201.0,289.0>>/L<<201.0,289.0>--<319.0,463.0>> = 8.735868542989213
	* uni20A9 (U+20A9): L<<161.0,313.0>--<145.0,189.0>>/L<<145.0,189.0>--<182.0,313.0>> = 9.262045129234014
	* uni20A9 (U+20A9): L<<289.0,400.0>--<301.0,500.0>>/L<<301.0,500.0>--<271.0,400.0>> = 9.856470821362652 and uni20A9 (U+20A9): L<<340.0,313.0>--<325.0,187.0>>/L<<325.0,187.0>--<363.0,313.0>> = 9.993669570831868 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[10] RadioCanada-Italic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary><div>
* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary><div>
* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary><div>
* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l
	- uni0295 + uni0315
	- uni0315 + uni02B7
	- uni1E5B + uni0315

   [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary><div>
* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary><div>
* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- two.pl
	- zero.pl
	- nine.pl
	- four.pl
	- eight.pl
	- six.pl
	- three.pl
	- five.pl
	- one.pl
	- ring_acute.cap 
	- And 5 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary><div>
* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: ohorn	Contours detected: 3	Expected: 2
	- Glyph name: Uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uni01EA	Contours detected: 3	Expected: 2
	- Glyph name: uni01EB	Contours detected: 3	Expected: 2
	- Glyph name: uni02BA	Contours detected: 1	Expected: 2 
	- And 38 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks.</summary><div>
* [com.google.fonts/check/dotted_circle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle)

* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary><div>
* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* six (U+0036): X=535.0,Y=688.5 (should be at cap-height 690?)
	* nine (U+0039): X=103.0,Y=2.0 (should be at baseline 0?)
	* d (U+0064): X=381.5,Y=514.0 (should be at x-height 515?)
	* g (U+0067): X=382.0,Y=513.5 (should be at x-height 515?)
	* p (U+0070): X=187.5,Y=1.5 (should be at baseline 0?)
	* braceleft (U+007B): X=187.0,Y=-254.0 (should be at descender -255?)
	* braceright (U+007D): X=197.5,Y=691.0 (should be at cap-height 690?)
	* dieresis (U+00A8): X=-9.0,Y=689.0 (should be at cap-height 690?)
	* dieresis (U+00A8): X=187.0,Y=689.0 (should be at cap-height 690?)
	* uni03BC.math (U+00B5): X=158.5,Y=-1.5 (should be at baseline 0?) and 69 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary><div>
* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* m (U+006D) contains a short segment B<<711.0,313.0>-<713.0,326.0>-<714.5,337.0>>
	* m (U+006D) contains a short segment B<<714.5,337.0>-<716.0,348.0>-<716.0,358.0>>
	* logicalnot (U+00AC) contains a short segment L<<520.0,249.0>--<520.0,249.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<502.0,67.0>-<510.0,67.0>-<515.5,68.5>>
	* uni03BC.math (U+00B5) contains a short segment B<<515.5,68.5>-<521.0,70.0>-<526.0,71.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<511.0,0.0>-<502.0,-4.0>-<493.5,-7.0>>
	* ae (U+00E6) contains a short segment B<<365.5,341.5>-<367.0,352.0>-<367.0,361.0>>
	* Upsilonlatin (U+01B1) contains a short segment L<<497.0,663.0>--<497.0,663.0>>
	* Upsilonlatin (U+01B1) contains a short segment L<<497.0,663.0>--<497.0,663.0>>
	* aeacute (U+01FD) contains a short segment B<<365.5,341.5>-<367.0,352.0>-<367.0,361.0>> and 16 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary><div>
* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)

* ⚠ **WARN** The following glyphs have colinear vectors:
	* Upsilonlatin (U+01B1): L<<497.0,663.0>--<497.0,663.0>> -> L<<497.0,663.0>--<497.0,663.0>>
	* exclam (U+0021): L<<106.0,208.0>--<158.0,515.0>> -> L<<158.0,515.0>--<195.0,690.0>>
	* exclam (U+0021): L<<294.0,690.0>--<257.0,515.0>> -> L<<257.0,515.0>--<175.0,208.0>>
	* exclamdown (U+00A1): L<<11.0,-185.0>--<50.0,0.0>> -> L<<50.0,0.0>--<131.0,307.0>>
	* exclamdown (U+00A1): L<<200.0,307.0>--<149.0,0.0>> -> L<<149.0,0.0>--<110.0,-185.0>>
	* ohm (U+2126): L<<242.0,27.0>--<242.0,27.0>> -> L<<242.0,27.0>--<242.0,27.0>>
	* uni0190 (U+0190): L<<457.0,398.0>--<443.0,338.0>> -> L<<443.0,338.0>--<438.0,312.0>> and uni03A9 (U+03A9): L<<242.0,27.0>--<242.0,27.0>> -> L<<242.0,27.0>--<242.0,27.0>> [code: found-colinear-vectors]
</div></details><br></div></details><details><summary><b>[11] RadioCanada-Light.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary><div>
* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary><div>
* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary><div>
* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + ij
	- ij + f
	- f + l
	- l + f
	- i + ij
	- ij + l
	- uni0295 + uni0315
	- uni0315 + uni02B7
	- uni1E5B + uni0315

   [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary><div>
* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary><div>
* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- nine.lf
	- breve.cap
	- ring.cap
	- one.lf
	- dotbelow
	- zero.lf
	- uni030C.alt
	- eight.lf
	- six.lf
	- dollar.BRACKET.100 
	- And 15 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary><div>
* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: ohorn	Contours detected: 3	Expected: 2
	- Glyph name: Uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uni01EA	Contours detected: 3	Expected: 2
	- Glyph name: uni023A	Contours detected: 4	Expected: 3
	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3 
	- And 37 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks.</summary><div>
* [com.google.fonts/check/dotted_circle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle)

* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary><div>
* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* f (U+0066): X=161.5,Y=689.0 (should be at cap-height 690?)
	* acircumflex (U+00E2): X=249.0,Y=689.0 (should be at cap-height 690?)
	* ecircumflex (U+00EA): X=275.0,Y=689.0 (should be at cap-height 690?)
	* icircumflex (U+00EE): X=125.0,Y=689.0 (should be at cap-height 690?)
	* ocircumflex (U+00F4): X=272.0,Y=689.0 (should be at cap-height 690?)
	* ucircumflex (U+00FB): X=281.0,Y=689.0 (should be at cap-height 690?)
	* ccircumflex (U+0109): X=269.0,Y=689.0 (should be at cap-height 690?)
	* gcircumflex (U+011D): X=274.0,Y=689.0 (should be at cap-height 690?)
	* jcircumflex (U+0135): X=125.0,Y=689.0 (should be at cap-height 690?)
	* scircumflex (U+015D): X=241.0,Y=689.0 (should be at cap-height 690?) and 41 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary><div>
* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* three (U+0033) contains a short segment L<<274.0,396.0>--<290.0,396.0>>
	* at (U+0040) contains a short segment L<<671.0,492.0>--<665.0,453.0>>
	* at (U+0040) contains a short segment B<<665.0,453.0>-<662.0,431.0>-<661.0,413.0>>
	* cent (U+00A2) contains a short segment L<<355.0,558.0>--<357.0,558.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<505.0,44.0>-<512.0,44.0>-<519.0,45.5>>
	* uni03BC.math (U+00B5) contains a short segment B<<519.0,45.5>-<526.0,47.0>-<531.0,48.0>>
	* ae (U+00E6) contains a short segment B<<779.0,280.0>-<779.0,270.0>-<778.5,261.0>>
	* ae (U+00E6) contains a short segment B<<778.5,261.0>-<778.0,252.0>-<777.0,244.0>>
	* oe (U+0153) contains a short segment B<<810.5,261.0>-<810.0,252.0>-<809.0,244.0>>
	* uni018F (U+018F) contains a short segment B<<70.0,325.0>-<70.0,333.0>-<70.5,343.0>> and 13 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary><div>
* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<131.0,180.0>--<122.0,510.0>> -> L<<122.0,510.0>--<122.0,690.0>>
	* exclam (U+0021): L<<184.0,690.0>--<184.0,510.0>> -> L<<184.0,510.0>--<175.0,180.0>>
	* exclamdown (U+00A1): L<<122.0,-185.0>--<122.0,0.0>> -> L<<122.0,0.0>--<131.0,330.0>> and exclamdown (U+00A1): L<<175.0,330.0>--<184.0,0.0>> -> L<<184.0,0.0>--<184.0,-185.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary><div>
* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni023A (U+023A): L<<162.0,226.0>--<119.0,105.0>>/L<<119.0,105.0>--<186.0,226.0>> = 9.410348931967583 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] RadioCanadaCondensed-LightItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary><div>
* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary><div>
* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary><div>
* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l
	- uni0295 + uni0315
	- uni0315 + uni02B7
	- uni1E5B + uni0315

   [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary><div>
* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Radio Canada Condensed Light' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary><div>
* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary><div>
* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- two.pl
	- zero.pl
	- nine.pl
	- four.pl
	- eight.pl
	- six.pl
	- three.pl
	- five.pl
	- one.pl
	- ring_acute.cap 
	- And 5 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary><div>
* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: ohorn	Contours detected: 3	Expected: 2
	- Glyph name: Uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uni01EA	Contours detected: 3	Expected: 2
	- Glyph name: uni01EB	Contours detected: 3	Expected: 2
	- Glyph name: uni023A	Contours detected: 4	Expected: 3 
	- And 40 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks.</summary><div>
* [com.google.fonts/check/dotted_circle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle)

* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary><div>
* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* six (U+0036): X=426.0,Y=691.0 (should be at cap-height 690?)
	* f (U+0066): X=214.0,Y=689.0 (should be at cap-height 690?)
	* i (U+0069): X=243.0,Y=691.0 (should be at cap-height 690?)
	* j (U+006A): X=253.0,Y=691.0 (should be at cap-height 690?)
	* s (U+0073): X=288.5,Y=508.0 (should be at x-height 510?)
	* y (U+0079): X=192.0,Y=1.0 (should be at baseline 0?)
	* braceright (U+007D): X=87.5,Y=1.5 (should be at baseline 0?)
	* section (U+00A7): X=401.0,Y=691.5 (should be at cap-height 690?)
	* ordfeminine (U+00AA): X=306.5,Y=688.0 (should be at cap-height 690?)
	* ordfeminine (U+00AA): X=353.0,Y=691.0 (should be at cap-height 690?) and 88 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary><div>
* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* dollar (U+0024) contains a short segment L<<302.0,698.0>--<302.0,698.0>>
	* three (U+0033) contains a short segment L<<217.0,396.0>--<221.0,396.0>>
	* greater (U+003E) contains a short segment L<<440.0,302.0>--<440.0,302.0>>
	* y (U+0079) contains a short segment L<<192.0,1.0>--<192.0,0.0>>
	* y (U+0079) contains a short segment L<<192.0,0.0>--<192.0,0.0>>
	* logicalnot (U+00AC) contains a short segment L<<517.0,263.0>--<517.0,263.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<385.0,44.0>-<393.0,44.0>-<398.5,45.5>>
	* uni03BC.math (U+00B5) contains a short segment B<<398.5,45.5>-<404.0,47.0>-<409.0,48.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<399.0,0.0>-<390.0,-4.0>-<382.0,-6.0>>
	* ae (U+00E6) contains a short segment B<<322.0,342.0>-<323.0,351.0>-<323.5,357.0>> and 51 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary><div>
* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<103.0,180.0>--<164.0,510.0>> -> L<<164.0,510.0>--<203.0,690.0>>
	* exclam (U+0021): L<<265.0,690.0>--<226.0,510.0>> -> L<<226.0,510.0>--<147.0,180.0>>
	* exclamdown (U+00A1): L<<18.0,-185.0>--<58.0,0.0>> -> L<<58.0,0.0>--<137.0,330.0>>
	* exclamdown (U+00A1): L<<181.0,330.0>--<120.0,0.0>> -> L<<120.0,0.0>--<80.0,-185.0>> and less (U+003C): L<<80.0,264.0>--<88.0,300.0>> -> L<<88.0,300.0>--<91.0,316.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary><div>
* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni023A (U+023A): L<<140.0,226.0>--<100.0,147.0>>/L<<100.0,147.0>--<149.0,226.0>> = 4.954967947274491
	* uni20A9 (U+20A9): L<<150.0,345.0>--<131.0,152.0>>/L<<131.0,152.0>--<198.0,345.0>> = 13.522057184106938 and uni20A9 (U+20A9): L<<339.0,345.0>--<324.0,152.0>>/L<<324.0,152.0>--<386.0,345.0>> = 13.36517263202207 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[11] RadioCanada-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWeightClass.</summary><div>
* [com.google.fonts/check/usweightclass](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/usweightclass)

* 🔥 **FAIL** OS/2 usWeightClass is '454' when it should be '400'. [code: bad-value]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary><div>
* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary><div>
* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary><div>
* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + ij
	- ij + f
	- f + l
	- l + f
	- i + ij
	- ij + l
	- uni0295 + uni0315
	- uni0315 + uni02B7
	- uni1E5B + uni0315

   [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary><div>
* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary><div>
* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- nine.lf
	- breve.cap
	- ring.cap
	- one.lf
	- dotbelow
	- zero.lf
	- uni030C.alt
	- eight.lf
	- six.lf
	- dollar.BRACKET.100 
	- And 15 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary><div>
* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: ohorn	Contours detected: 3	Expected: 2
	- Glyph name: Uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uni01EA	Contours detected: 3	Expected: 2
	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3
	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3 
	- And 35 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks.</summary><div>
* [com.google.fonts/check/dotted_circle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle)

* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary><div>
* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* braceleft (U+007B): X=310.0,Y=-257.0 (should be at descender -255?)
	* braceright (U+007D): X=41.0,Y=-257.0 (should be at descender -255?)
	* questiondown (U+00BF): X=171.0,Y=-2.0 (should be at baseline 0?)
	* Aring (U+00C5): X=410.0,Y=690.5 (should be at cap-height 690?)
	* Aring (U+00C5): X=246.5,Y=690.5 (should be at cap-height 690?)
	* aring (U+00E5): X=150.0,Y=692.0 (should be at cap-height 690?)
	* aring (U+00E5): X=381.0,Y=692.0 (should be at cap-height 690?)
	* aring (U+00E5): X=150.0,Y=692.0 (should be at cap-height 690?)
	* aring (U+00E5): X=217.0,Y=692.0 (should be at cap-height 690?)
	* aring (U+00E5): X=313.0,Y=692.0 (should be at cap-height 690?) and 42 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary><div>
* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* at (U+0040) contains a short segment B<<697.0,450.0>-<693.0,428.0>-<691.5,410.5>>
	* at (U+0040) contains a short segment B<<691.5,410.5>-<690.0,393.0>-<690.0,372.0>>
	* a (U+0061) contains a short segment L<<360.0,309.0>--<360.0,315.0>>
	* ordfeminine (U+00AA) contains a short segment L<<284.0,531.0>--<284.0,534.0>>
	* agrave (U+00E0) contains a short segment L<<360.0,309.0>--<360.0,315.0>>
	* aacute (U+00E1) contains a short segment L<<360.0,309.0>--<360.0,315.0>>
	* acircumflex (U+00E2) contains a short segment L<<360.0,309.0>--<360.0,315.0>>
	* atilde (U+00E3) contains a short segment L<<360.0,309.0>--<360.0,315.0>>
	* adieresis (U+00E4) contains a short segment L<<360.0,309.0>--<360.0,315.0>>
	* aring (U+00E5) contains a short segment L<<360.0,309.0>--<360.0,315.0>> and 33 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary><div>
* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<125.0,220.0>--<107.0,517.0>> -> L<<107.0,517.0>--<107.0,690.0>>
	* exclam (U+0021): L<<222.0,690.0>--<222.0,517.0>> -> L<<222.0,517.0>--<204.0,220.0>>
	* exclamdown (U+00A1): L<<107.0,-185.0>--<107.0,0.0>> -> L<<107.0,0.0>--<125.0,297.0>>
	* exclamdown (U+00A1): L<<204.0,297.0>--<222.0,0.0>> -> L<<222.0,0.0>--<222.0,-185.0>>
	* lira (U+20A4): L<<241.0,477.0>--<241.0,477.0>> -> L<<241.0,477.0>--<454.0,477.0>> and lira (U+20A4): L<<68.0,477.0>--<133.0,477.0>> -> L<<133.0,477.0>--<133.0,477.0>> [code: found-colinear-vectors]
</div></details><br></div></details><details><summary><b>[11] RadioCanadaCondensed-BoldItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary><div>
* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary><div>
* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary><div>
* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l
	- uni0295 + uni0315
	- uni0315 + uni02B7
	- uni1E5B + uni0315

   [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary><div>
* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Radio Canada Condensed' / SUBFAMILY_NAME = 'Bold Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary><div>
* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary><div>
* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- two.pl
	- zero.pl
	- nine.pl
	- four.pl
	- eight.pl
	- six.pl
	- three.pl
	- five.pl
	- one.pl
	- ring_acute.cap 
	- And 5 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary><div>
* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: ohorn	Contours detected: 3	Expected: 2
	- Glyph name: Uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uni01EA	Contours detected: 3	Expected: 2
	- Glyph name: uni01EB	Contours detected: 3	Expected: 2
	- Glyph name: uni023E	Contours detected: 1	Expected: 2 
	- And 44 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks.</summary><div>
* [com.google.fonts/check/dotted_circle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle)

* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary><div>
* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* c (U+0063): X=388.5,Y=526.0 (should be at x-height 525?)
	* c (U+0063): X=276.5,Y=-1.0 (should be at baseline 0?)
	* j (U+006A): X=139.0,Y=1.0 (should be at baseline 0?)
	* k (U+006B): X=350.0,Y=526.0 (should be at x-height 525?)
	* k (U+006B): X=531.0,Y=526.0 (should be at x-height 525?)
	* s (U+0073): X=329.0,Y=523.0 (should be at x-height 525?)
	* braceleft (U+007B): X=318.5,Y=688.5 (should be at cap-height 690?)
	* exclamdown (U+00A1): X=18.0,Y=-1.0 (should be at baseline 0?)
	* exclamdown (U+00A1): X=170.0,Y=-1.0 (should be at baseline 0?)
	* uni03BC.math (U+00B5): X=451.0,Y=-2.0 (should be at baseline 0?) and 85 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary><div>
* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<317.0,690.0>--<282.0,526.0>> -> L<<282.0,526.0>--<202.0,265.0>>
	* exclam (U+0021): L<<98.0,265.0>--<130.0,526.0>> -> L<<130.0,526.0>--<165.0,690.0>>
	* exclamdown (U+00A1): L<<-21.0,-185.0>--<18.0,-1.0>> -> L<<18.0,-1.0>--<98.0,260.0>>
	* exclamdown (U+00A1): L<<202.0,260.0>--<170.0,-1.0>> -> L<<170.0,-1.0>--<131.0,-185.0>>
	* greaterequal (U+2265): L<<26.0,59.0>--<51.0,180.0>> -> L<<51.0,180.0>--<83.0,329.0>> and lessequal (U+2264): L<<436.0,317.0>--<407.0,180.0>> -> L<<407.0,180.0>--<382.0,59.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary><div>
* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)

* ⚠ **WARN** The following glyphs have jaggy segments:
	* currency (U+00A4): L<<461.0,447.0>--<461.0,448.0>>/B<<461.0,448.0>-<466.0,421.0>-<466.0,391.0>> = 10.491477012331599
	* trademark (U+2122): L<<650.0,290.0>--<714.0,590.0>>/L<<714.0,590.0>--<605.0,369.0>> = 14.210523874331708
	* uni023A (U+023A): L<<323.0,481.0>--<238.0,300.0>>/L<<238.0,300.0>--<326.0,429.0>> = 9.14528419182745
	* uni026C (U+026C): B<<189.0,510.5>-<205.0,487.0>-<206.0,458.0>>/L<<206.0,458.0>--<261.0,715.0>> = 14.054464997496973
	* uni20A9 (U+20A9): L<<162.0,298.0>--<144.0,177.0>>/L<<144.0,177.0>--<178.0,298.0>> = 7.233636000848635
	* uni20A9 (U+20A9): L<<285.0,403.0>--<299.0,496.0>>/L<<299.0,496.0>--<274.0,403.0>> = 6.485502261033817 and uni20A9 (U+20A9): L<<336.0,298.0>--<319.0,172.0>>/L<<319.0,172.0>--<353.0,298.0>> = 7.417116331651419 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] RadioCanadaCondensed-SemiBoldItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary><div>
* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary><div>
* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary><div>
* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l
	- uni0295 + uni0315
	- uni0315 + uni02B7
	- uni1E5B + uni0315

   [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary><div>
* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Radio Canada Condensed SemiBold' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary><div>
* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary><div>
* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- two.pl
	- zero.pl
	- nine.pl
	- four.pl
	- eight.pl
	- six.pl
	- three.pl
	- five.pl
	- one.pl
	- ring_acute.cap 
	- And 5 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary><div>
* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: ohorn	Contours detected: 3	Expected: 2
	- Glyph name: Uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uni01EA	Contours detected: 3	Expected: 2
	- Glyph name: uni01EB	Contours detected: 3	Expected: 2
	- Glyph name: uni023E	Contours detected: 1	Expected: 2 
	- And 44 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks.</summary><div>
* [com.google.fonts/check/dotted_circle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle)

* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary><div>
* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=393.0,Y=691.0 (should be at cap-height 690?)
	* dollar (U+0024): X=137.0,Y=-1.0 (should be at baseline 0?)
	* g (U+0067): X=326.0,Y=522.5 (should be at x-height 522?)
	* braceleft (U+007B): X=178.0,Y=689.0 (should be at cap-height 690?)
	* exclamdown (U+00A1): X=22.0,Y=-1.0 (should be at baseline 0?)
	* exclamdown (U+00A1): X=155.0,Y=-1.0 (should be at baseline 0?)
	* section (U+00A7): X=387.0,Y=-1.0 (should be at baseline 0?)
	* dieresis (U+00A8): X=-51.5,Y=692.0 (should be at cap-height 690?)
	* dieresis (U+00A8): X=129.5,Y=692.0 (should be at cap-height 690?)
	* uni03BC.math (U+00B5): X=444.0,Y=-1.0 (should be at baseline 0?) and 77 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary><div>
* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* ampersand (U+0026) contains a short segment L<<282.0,433.0>--<282.0,433.0>>
	* at (U+0040) contains a short segment B<<582.0,109.0>-<590.0,88.0>-<607.0,88.0>>
	* R (U+0052) contains a short segment B<<257.0,250.0>-<253.0,249.0>-<249.0,249.0>>
	* sterling (U+00A3) contains a short segment B<<267.0,286.0>-<266.0,277.0>-<264.0,268.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<453.0,103.0>-<460.0,103.0>-<467.0,106.0>>
	* ae (U+00E6) contains a short segment B<<300.0,334.5>-<301.0,344.0>-<301.0,352.0>>
	* Ccaron (U+010C) contains a short segment L<<345.0,753.0>--<345.0,753.0>>
	* ccaron (U+010D) contains a short segment L<<257.0,585.0>--<257.0,585.0>>
	* Dcaron (U+010E) contains a short segment L<<311.0,753.0>--<311.0,753.0>>
	* Ecaron (U+011A) contains a short segment L<<309.0,753.0>--<309.0,753.0>> and 47 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary><div>
* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<303.0,690.0>--<267.0,522.0>> -> L<<267.0,522.0>--<186.0,245.0>>
	* exclam (U+0021): L<<95.0,245.0>--<133.0,522.0>> -> L<<133.0,522.0>--<169.0,690.0>>
	* exclamdown (U+00A1): L<<-17.0,-185.0>--<22.0,-1.0>> -> L<<22.0,-1.0>--<103.0,276.0>> and exclamdown (U+00A1): L<<193.0,276.0>--<155.0,-1.0>> -> L<<155.0,-1.0>--<116.0,-185.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary><div>
* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)

* ⚠ **WARN** The following glyphs have jaggy segments:
	* greaterequal (U+2265): L<<53.0,170.0>--<71.0,182.0>>/L<<71.0,182.0>--<54.0,176.0>> = 14.250032697803595
	* uni023A (U+023A): L<<319.0,505.0>--<220.0,295.0>>/L<<220.0,295.0>--<323.0,445.0>> = 9.235559093165962
	* uni20A9 (U+20A9): L<<161.0,306.0>--<144.0,182.0>>/L<<144.0,182.0>--<180.0,306.0>> = 8.382805427791155
	* uni20A9 (U+20A9): L<<287.0,402.0>--<300.0,500.0>>/L<<300.0,500.0>--<272.0,402.0>> = 8.389051844483356 and uni20A9 (U+20A9): L<<338.0,306.0>--<322.0,179.0>>/L<<322.0,179.0>--<358.0,306.0>> = 8.645618578452384 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[11] RadioCanada-Medium.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary><div>
* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary><div>
* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary><div>
* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + ij
	- ij + f
	- f + l
	- l + f
	- i + ij
	- ij + l
	- uni0295 + uni0315
	- uni0315 + uni02B7
	- uni1E5B + uni0315

   [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary><div>
* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary><div>
* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- nine.lf
	- breve.cap
	- ring.cap
	- one.lf
	- dotbelow
	- zero.lf
	- uni030C.alt
	- eight.lf
	- six.lf
	- dollar.BRACKET.100 
	- And 15 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary><div>
* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: ohorn	Contours detected: 3	Expected: 2
	- Glyph name: Uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uni01EA	Contours detected: 3	Expected: 2
	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3
	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3 
	- And 35 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks.</summary><div>
* [com.google.fonts/check/dotted_circle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle)

* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary><div>
* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* six (U+0036): X=443.5,Y=688.5 (should be at cap-height 690?)
	* nine (U+0039): X=156.5,Y=1.5 (should be at baseline 0?)
	* aring (U+00E5): X=151.0,Y=691.0 (should be at cap-height 690?)
	* aring (U+00E5): X=380.0,Y=691.0 (should be at cap-height 690?)
	* aring (U+00E5): X=151.0,Y=691.0 (should be at cap-height 690?)
	* aring (U+00E5): X=219.0,Y=691.0 (should be at cap-height 690?)
	* aring (U+00E5): X=311.0,Y=691.0 (should be at cap-height 690?)
	* aring (U+00E5): X=219.0,Y=691.0 (should be at cap-height 690?)
	* dcaron (U+010F): X=561.0,Y=690.5 (should be at cap-height 690?)
	* uni0123 (U+0123): X=313.0,Y=692.0 (should be at cap-height 690?) and 58 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary><div>
* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* at (U+0040) contains a short segment B<<702.0,449.0>-<698.0,427.0>-<696.5,410.0>>
	* at (U+0040) contains a short segment B<<696.5,410.0>-<695.0,393.0>-<695.0,372.0>>
	* a (U+0061) contains a short segment L<<356.0,310.0>--<356.0,315.0>>
	* ordfeminine (U+00AA) contains a short segment L<<281.0,532.0>--<281.0,533.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<550.0,88.0>-<559.0,88.0>-<569.0,91.0>>
	* agrave (U+00E0) contains a short segment L<<356.0,310.0>--<356.0,315.0>>
	* aacute (U+00E1) contains a short segment L<<356.0,310.0>--<356.0,315.0>>
	* acircumflex (U+00E2) contains a short segment L<<356.0,310.0>--<356.0,315.0>>
	* atilde (U+00E3) contains a short segment L<<356.0,310.0>--<356.0,315.0>>
	* adieresis (U+00E4) contains a short segment L<<356.0,310.0>--<356.0,315.0>> and 40 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary><div>
* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<125.0,228.0>--<105.0,519.0>> -> L<<105.0,519.0>--<105.0,690.0>>
	* exclam (U+0021): L<<230.0,690.0>--<230.0,519.0>> -> L<<230.0,519.0>--<210.0,228.0>>
	* exclamdown (U+00A1): L<<105.0,-185.0>--<105.0,0.0>> -> L<<105.0,0.0>--<125.0,291.0>>
	* exclamdown (U+00A1): L<<210.0,291.0>--<230.0,0.0>> -> L<<230.0,0.0>--<230.0,-185.0>> and uni2C65 (U+2C65): L<<356.0,310.0>--<356.0,310.0>> -> L<<356.0,310.0>--<356.0,310.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary><div>
* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni20A9 (U+20A9): L<<163.0,313.0>--<180.0,171.0>>/L<<180.0,171.0>--<198.0,313.0>> = 14.05117803251903 and uni20A9 (U+20A9): L<<314.0,400.0>--<298.0,524.0>>/L<<298.0,524.0>--<283.0,400.0>> = 14.249806917644122 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] RadioCanadaCondensed-Italic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary><div>
* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary><div>
* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary><div>
* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l
	- uni0295 + uni0315
	- uni0315 + uni02B7
	- uni1E5B + uni0315

   [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary><div>
* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Radio Canada Condensed' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary><div>
* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary><div>
* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- two.pl
	- zero.pl
	- nine.pl
	- four.pl
	- eight.pl
	- six.pl
	- three.pl
	- five.pl
	- one.pl
	- ring_acute.cap 
	- And 5 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary><div>
* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: ohorn	Contours detected: 3	Expected: 2
	- Glyph name: Uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uni01EA	Contours detected: 3	Expected: 2
	- Glyph name: uni01EB	Contours detected: 3	Expected: 2
	- Glyph name: uni02BA	Contours detected: 1	Expected: 2 
	- And 38 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks.</summary><div>
* [com.google.fonts/check/dotted_circle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle)

* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary><div>
* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* six (U+0036): X=442.5,Y=690.5 (should be at cap-height 690?)
	* nine (U+0039): X=84.5,Y=-0.5 (should be at baseline 0?)
	* g (U+0067): X=156.0,Y=-1.0 (should be at baseline 0?)
	* braceright (U+007D): X=40.5,Y=2.0 (should be at baseline 0?)
	* braceright (U+007D): X=122.5,Y=-1.5 (should be at baseline 0?)
	* Aring (U+00C5): X=420.0,Y=691.5 (should be at cap-height 690?)
	* Aring (U+00C5): X=268.5,Y=691.5 (should be at cap-height 690?)
	* atilde (U+00E3): X=329.0,Y=691.5 (should be at cap-height 690?)
	* aring (U+00E5): X=238.0,Y=689.0 (should be at cap-height 690?)
	* aring (U+00E5): X=453.0,Y=689.0 (should be at cap-height 690?) and 90 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary><div>
* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* uni03BC.math (U+00B5) contains a short segment B<<425.0,63.0>-<431.0,63.0>-<435.5,64.5>>
	* uni03BC.math (U+00B5) contains a short segment B<<435.5,64.5>-<440.0,66.0>-<444.0,67.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<428.0,0.0>-<421.0,-4.0>-<411.5,-7.0>>
	* uni0190 (U+0190) contains a short segment L<<424.0,395.0>--<421.0,380.0>>
	* uni0190 (U+0190) contains a short segment L<<421.0,380.0>--<421.0,380.0>>
	* uni026C (U+026C) contains a short segment L<<205.0,402.0>--<205.0,402.0>>
	* uni03BC (U+03BC) contains a short segment B<<425.0,63.0>-<431.0,63.0>-<435.5,64.5>>
	* uni03BC (U+03BC) contains a short segment B<<435.5,64.5>-<440.0,66.0>-<444.0,67.0>>
	* uni03BC (U+03BC) contains a short segment B<<428.0,0.0>-<421.0,-4.0>-<411.5,-7.0>>
	* pi (U+03C0) contains a short segment B<<393.0,66.0>-<398.0,66.0>-<403.5,67.5>> and 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary><div>
* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<273.0,690.0>--<235.0,514.0>> -> L<<235.0,514.0>--<153.0,204.0>>
	* exclam (U+0021): L<<90.0,204.0>--<140.0,514.0>> -> L<<140.0,514.0>--<176.0,690.0>>
	* exclamdown (U+00A1): L<<-9.0,-185.0>--<30.0,0.0>> -> L<<30.0,0.0>--<112.0,310.0>> and exclamdown (U+00A1): L<<175.0,310.0>--<125.0,0.0>> -> L<<125.0,0.0>--<86.0,-185.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary><div>
* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni023A (U+023A): L<<311.0,556.0>--<181.0,282.0>>/L<<181.0,282.0>--<315.0,482.0>> = 8.439964625612225
	* uni20A9 (U+20A9): L<<160.0,322.0>--<145.0,198.0>>/L<<145.0,198.0>--<185.0,322.0>> = 10.98126903808958
	* uni20A9 (U+20A9): L<<290.0,399.0>--<301.0,497.0>>/L<<301.0,497.0>--<270.0,399.0>> = 11.149192099955716 and uni20A9 (U+20A9): L<<343.0,322.0>--<329.0,198.0>>/L<<329.0,198.0>--<368.0,322.0>> = 11.017602536292145 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[10] RadioCanada-BoldItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary><div>
* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary><div>
* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary><div>
* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l
	- uni0295 + uni0315
	- uni0315 + uni02B7
	- uni1E5B + uni0315

   [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary><div>
* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary><div>
* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- two.pl
	- zero.pl
	- nine.pl
	- four.pl
	- eight.pl
	- six.pl
	- three.pl
	- five.pl
	- one.pl
	- ring_acute.cap 
	- And 5 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary><div>
* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: ohorn	Contours detected: 3	Expected: 2
	- Glyph name: Uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uni01EA	Contours detected: 3	Expected: 2
	- Glyph name: uni01EB	Contours detected: 3	Expected: 2
	- Glyph name: uni02BA	Contours detected: 1	Expected: 2 
	- And 42 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks.</summary><div>
* [com.google.fonts/check/dotted_circle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle)

* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary><div>
* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* at (U+0040) contains a short segment B<<696.5,115.5>-<707.0,98.0>-<726.0,98.0>>
	* R (U+0052) contains a short segment L<<299.0,240.0>--<298.0,240.0>>
	* bracketright (U+005D) contains a short segment L<<321.0,710.0>--<321.0,710.0>>
	* bracketright (U+005D) contains a short segment L<<132.0,-175.0>--<133.0,-175.0>>
	* e (U+0065) contains a short segment B<<175.0,214.0>-<175.0,210.0>-<175.0,205.0>>
	* f (U+0066) contains a short segment L<<153.0,525.0>--<156.0,538.0>>
	* m (U+006D) contains a short segment B<<702.0,315.0>-<704.0,324.0>-<705.0,332.0>>
	* m (U+006D) contains a short segment B<<705.0,332.0>-<706.0,340.0>-<706.0,347.0>>
	* m (U+006D) contains a short segment B<<387.0,315.0>-<389.0,324.0>-<390.0,332.0>>
	* m (U+006D) contains a short segment B<<390.0,332.0>-<391.0,340.0>-<391.0,347.0>> and 80 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary><div>
* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)

* ⚠ **WARN** The following glyphs have colinear vectors:
	* R (U+0052): L<<299.0,240.0>--<298.0,240.0>> -> L<<298.0,240.0>--<223.0,240.0>>
	* Racute (U+0154): L<<299.0,240.0>--<298.0,240.0>> -> L<<298.0,240.0>--<223.0,240.0>>
	* Rcaron (U+0158): L<<299.0,240.0>--<298.0,240.0>> -> L<<298.0,240.0>--<223.0,240.0>>
	* Upsilonlatin (U+01B1): L<<361.0,630.0>--<361.0,630.0>> -> L<<361.0,630.0>--<361.0,630.0>>
	* Upsilonlatin (U+01B1): L<<501.0,630.0>--<501.0,630.0>> -> L<<501.0,630.0>--<501.0,630.0>>
	* exclam (U+0021): L<<108.0,260.0>--<143.0,525.0>> -> L<<143.0,525.0>--<178.0,690.0>>
	* exclamdown (U+00A1): L<<229.0,265.0>--<196.0,0.0>> -> L<<196.0,0.0>--<157.0,-185.0>>
	* greater (U+003E): L<<544.0,349.0>--<533.0,299.0>> -> L<<533.0,299.0>--<518.0,227.0>>
	* greaterequal (U+2265): L<<41.0,60.0>--<66.0,179.0>> -> L<<66.0,179.0>--<97.0,317.0>>
	* less (U+003C): L<<58.0,227.0>--<71.0,285.0>> -> L<<71.0,285.0>--<84.0,349.0>> and 12 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary><div>
* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni01E5 (U+01E5): L<<345.0,121.0>--<350.0,128.0>>/B<<350.0,128.0>-<320.0,91.0>-<279.5,71.5>> = 3.4978351067723796
	* uni023A (U+023A): L<<373.0,479.0>--<276.0,301.0>>/L<<276.0,301.0>--<379.0,427.0>> = 10.676733393053745
	* uni026C (U+026C): B<<178.0,534.0>-<241.0,534.0>-<243.0,461.0>>/L<<243.0,461.0>--<297.0,715.0>> = 13.571649703532666
	* uni20A9 (U+20A9): L<<192.0,298.0>--<173.0,175.0>>/L<<173.0,175.0>--<208.0,298.0>> = 7.102690999535652
	* uni20A9 (U+20A9): L<<336.0,403.0>--<347.0,490.0>>/L<<347.0,490.0>--<322.0,403.0>> = 8.826282352552697
	* uni20A9 (U+20A9): L<<406.0,298.0>--<389.0,169.0>>/L<<389.0,169.0>--<424.0,298.0>> = 7.672580767576534 and uniA7AD (U+A7AD): B<<162.0,565.0>-<225.0,565.0>-<227.0,493.0>>/L<<227.0,493.0>--<269.0,690.0>> = 13.626297044274049 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[11] RadioCanada-Bold.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary><div>
* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary><div>
* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary><div>
* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + ij
	- ij + f
	- f + l
	- l + f
	- i + ij
	- ij + l
	- uni0295 + uni0315
	- uni0315 + uni02B7
	- uni1E5B + uni0315

   [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary><div>
* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary><div>
* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- nine.lf
	- breve.cap
	- ring.cap
	- one.lf
	- dotbelow
	- zero.lf
	- uni030C.alt
	- eight.lf
	- six.lf
	- dollar.BRACKET.100 
	- And 15 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary><div>
* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: ohorn	Contours detected: 3	Expected: 2
	- Glyph name: Uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uhorn	Contours detected: 2	Expected: 1
	- Glyph name: uni01EA	Contours detected: 3	Expected: 2
	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3
	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3 
	- And 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks.</summary><div>
* [com.google.fonts/check/dotted_circle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle)

* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary><div>
* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* parenleft (U+0028): X=278.0,Y=-256.0 (should be at descender -255?)
	* parenright (U+0029): X=22.0,Y=-256.0 (should be at descender -255?)
	* six (U+0036): X=452.5,Y=690.5 (should be at cap-height 690?)
	* a (U+0061): X=144.0,Y=523.5 (should be at x-height 525?)
	* s (U+0073): X=113.5,Y=1.5 (should be at baseline 0?)
	* germandbls (U+00DF): X=308.5,Y=1.5 (should be at baseline 0?)
	* atilde (U+00E3): X=137.5,Y=688.5 (should be at cap-height 690?)
	* atilde (U+00E3): X=289.0,Y=692.0 (should be at cap-height 690?)
	* atilde (U+00E3): X=339.0,Y=689.5 (should be at cap-height 690?)
	* ntilde (U+00F1): X=198.5,Y=688.5 (should be at cap-height 690?) and 81 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary><div>
* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* at (U+0040) contains a short segment B<<722.0,446.0>-<718.0,424.0>-<716.5,407.5>>
	* at (U+0040) contains a short segment B<<716.5,407.5>-<715.0,391.0>-<715.0,370.0>>
	* at (U+0040) contains a short segment B<<763.0,98.0>-<782.0,98.0>-<798.5,113.5>>
	* a (U+0061) contains a short segment L<<337.0,314.0>--<337.0,318.0>>
	* sterling (U+00A3) contains a short segment B<<156.0,260.0>-<156.0,269.0>-<155.0,278.0>>
	* sterling (U+00A3) contains a short segment B<<310.0,278.0>-<311.0,269.0>-<311.0,260.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<576.0,118.0>-<585.0,118.0>-<594.0,121.0>>
	* agrave (U+00E0) contains a short segment L<<337.0,314.0>--<337.0,318.0>>
	* aacute (U+00E1) contains a short segment L<<337.0,314.0>--<337.0,318.0>>
	* acircumflex (U+00E2) contains a short segment L<<337.0,314.0>--<337.0,318.0>> and 38 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary><div>
* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<122.0,260.0>--<96.0,525.0>> -> L<<96.0,525.0>--<96.0,690.0>>
	* exclam (U+0021): L<<262.0,690.0>--<262.0,525.0>> -> L<<262.0,525.0>--<236.0,260.0>>
	* exclamdown (U+00A1): L<<236.0,265.0>--<262.0,0.0>> -> L<<262.0,0.0>--<262.0,-185.0>>
	* exclamdown (U+00A1): L<<96.0,-185.0>--<96.0,0.0>> -> L<<96.0,0.0>--<122.0,265.0>> and uni01E5 (U+01E5): L<<385.0,36.0>--<385.0,42.0>> -> L<<385.0,42.0>--<385.0,112.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary><div>
* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)

* ⚠ **WARN** The following glyphs have jaggy segments:
	* estimated (U+212E): B<<509.0,577.0>-<503.0,584.0>-<495.0,591.0>>/L<<495.0,591.0>--<509.0,577.0>> = 3.814074834290474
	* estimated (U+212E): L<<495.0,591.0>--<509.0,577.0>>/B<<509.0,577.0>-<503.0,584.0>-<495.0,591.0>> = 4.398705354995591
	* uni026C (U+026C): B<<111.0,534.0>-<174.0,534.0>-<191.0,463.0>>/L<<191.0,463.0>--<191.0,715.0>> = 13.465208094811695
	* uni20A9 (U+20A9): L<<184.0,298.0>--<191.0,175.0>>/L<<191.0,175.0>--<200.0,298.0>> = 7.44213806578537
	* uni20A9 (U+20A9): L<<306.0,403.0>--<299.0,490.0>>/L<<299.0,490.0>--<292.0,403.0>> = 9.200191332526574
	* uni20A9 (U+20A9): L<<398.0,298.0>--<408.0,169.0>>/L<<408.0,169.0>--<416.0,298.0>> = 7.981350442594271 and uniA7AD (U+A7AD): B<<98.0,565.0>-<161.0,565.0>-<178.0,494.0>>/L<<178.0,494.0>--<178.0,690.0>> = 13.465208094811695 [code: found-jaggy-segments]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 2 | 166 | 1558 | 91 | 1304 | 0 |
| 0% | 0% | 5% | 50% | 3% | 42% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
