## Fontbakery report

Fontbakery version: 0.8.4

<details>
<summary><b>[12] RadioCanada-SemiBold.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

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

</details>
<details>
<summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
<pre>--- Rationale ---
According to a GlyphsApp tutorial [1], in order to make sure all versions of
Windows recognize it as a valid font file, we must make sure that the
concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style
(NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20
characters.
After discussing the problem in more detail at `FontBakery issue #2179 [2] we
decided that allowing up to 27 chars would still be on the safe side, though.
[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances
[2] https://github.com/googlefonts/fontbakery/issues/2179</pre>

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Radio Canada SemiBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - grave.cap
 - one.lf
 - hungarumlaut.cap
 - uni030C.alt
 - dotaccent.cap
 - ring.cap
 - caron.cap
 - zero.lf
 - seven.lf
 - five.lf
 - dotbelow
 - two.lf
 - uni20B2.BRACKET.100
 - acute.cap
 - ring_acute.cap
 - dieresis.cap
 - circumflex.cap
 - four.lf
 - uni20A6.BRACKET.100
 - uni0313.short
 - three.lf
 - eight.lf
 - dollar.BRACKET.100
 - six.lf
 - breve.cap
 - tilde.cap
 - caron.alt
 - uni0326
 - cent.BRACKET.100
 - macron.cap
 - uni0326.alt 
 - nine.lf
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

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
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: lessequal	Contours detected: 1	Expected: 2
 - Glyph name: greaterequal	Contours detected: 1	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: greaterequal	Contours detected: 1	Expected: 2
 - Glyph name: lessequal	Contours detected: 1	Expected: 2
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

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
	* aring (U+00E5): X=153.0,Y=689.0 (should be at cap-height 690?) and 86 more. [code: found-misalignments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

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
	* adieresis (U+00E4) contains a short segment L<<346.0,312.0>--<346.0,317.0>> and 43 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<123.0,244.0>--<101.0,522.0>> -> L<<101.0,522.0>--<101.0,690.0>>
	* exclam (U+0021): L<<246.0,690.0>--<246.0,522.0>> -> L<<246.0,522.0>--<223.0,244.0>>
	* exclamdown (U+00A1): L<<101.0,-185.0>--<101.0,0.0>> -> L<<101.0,0.0>--<123.0,278.0>> and exclamdown (U+00A1): L<<223.0,278.0>--<246.0,0.0>> -> L<<246.0,0.0>--<246.0,-185.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni20A9 (U+20A9): L<<173.0,306.0>--<185.0,170.0>>/L<<185.0,170.0>--<199.0,306.0>> = 10.919843675814004
	* uni20A9 (U+20A9): L<<310.0,402.0>--<298.0,515.0>>/L<<298.0,515.0>--<287.0,402.0>> = 11.621736052038148 and uni20A9 (U+20A9): L<<399.0,306.0>--<413.0,167.0>>/L<<413.0,167.0>--<426.0,306.0>> = 11.094457848941124 [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[12] RadioCanadaCondensed-Medium.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

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

</details>
<details>
<summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
<pre>--- Rationale ---
According to a GlyphsApp tutorial [1], in order to make sure all versions of
Windows recognize it as a valid font file, we must make sure that the
concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style
(NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20
characters.
After discussing the problem in more detail at `FontBakery issue #2179 [2] we
decided that allowing up to 27 chars would still be on the safe side, though.
[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances
[2] https://github.com/googlefonts/fontbakery/issues/2179</pre>

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Radio Canada Condensed Medium' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - grave.cap
 - one.lf
 - hungarumlaut.cap
 - uni030C.alt
 - dotaccent.cap
 - ring.cap
 - caron.cap
 - zero.lf
 - seven.lf
 - five.lf
 - dotbelow
 - two.lf
 - uni20B2.BRACKET.100
 - acute.cap
 - ring_acute.cap
 - dieresis.cap
 - circumflex.cap
 - four.lf
 - uni20A6.BRACKET.100
 - uni0313.short
 - three.lf
 - eight.lf
 - dollar.BRACKET.100
 - six.lf
 - breve.cap
 - tilde.cap
 - caron.alt
 - uni0326
 - cent.BRACKET.100
 - macron.cap
 - uni0326.alt 
 - nine.lf
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

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
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* six (U+0036): X=373.5,Y=691.0 (should be at cap-height 690?)
	* d (U+0064): X=284.0,Y=517.0 (should be at x-height 519?)
	* f (U+0066): X=15.0,Y=518.0 (should be at x-height 519?)
	* f (U+0066): X=90.0,Y=518.0 (should be at x-height 519?)
	* f (U+0066): X=196.0,Y=518.0 (should be at x-height 519?)
	* f (U+0066): X=316.0,Y=518.0 (should be at x-height 519?)
	* p (U+0070): X=221.5,Y=1.5 (should be at baseline 0?)
	* ordfeminine (U+00AA): X=109.0,Y=690.5 (should be at cap-height 690?)
	* uni03BC.math (U+00B5): X=492.0,Y=-1.0 (should be at baseline 0?)
	* germandbls (U+00DF): X=259.0,Y=-1.0 (should be at baseline 0?) and 52 more. [code: found-misalignments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* at (U+0040) contains a short segment B<<603.5,94.0>-<615.0,77.0>-<634.0,77.0>>
	* R (U+0052) contains a short segment L<<259.0,255.0>--<259.0,255.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<478.0,88.0>-<483.0,88.0>-<492.0,91.0>>
	* ae (U+00E6) contains a short segment L<<295.0,311.0>--<295.0,315.0>>
	* Eng (U+014A) contains a short segment B<<339.0,-92.0>-<351.0,-96.0>-<360.5,-98.5>>
	* Eng (U+014A) contains a short segment B<<360.5,-98.5>-<370.0,-101.0>-<381.0,-101.0>>
	* Racute (U+0154) contains a short segment L<<259.0,255.0>--<259.0,255.0>>
	* uni0156 (U+0156) contains a short segment L<<259.0,255.0>--<259.0,255.0>>
	* Rcaron (U+0158) contains a short segment L<<259.0,255.0>--<259.0,255.0>>
	* uni019D (U+019D) contains a short segment B<<-25.0,-92.0>-<-13.0,-96.0>-<-3.5,-98.5>> and 15 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<105.0,227.0>--<87.0,518.0>> -> L<<87.0,518.0>--<87.0,690.0>>
	* exclam (U+0021): L<<202.0,690.0>--<202.0,518.0>> -> L<<202.0,518.0>--<184.0,227.0>>
	* exclamdown (U+00A1): L<<184.0,291.0>--<202.0,0.0>> -> L<<202.0,0.0>--<202.0,-185.0>> and exclamdown (U+00A1): L<<87.0,-185.0>--<87.0,0.0>> -> L<<87.0,0.0>--<105.0,291.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni023A (U+023A): L<<266.0,552.0>--<188.0,259.0>>/L<<188.0,259.0>--<287.0,473.0>> = 9.918982796213937
	* uni20A9 (U+20A9): L<<149.0,313.0>--<159.0,189.0>>/L<<159.0,189.0>--<171.0,313.0>> = 10.138189470316771
	* uni20A9 (U+20A9): L<<258.0,400.0>--<250.0,500.0>>/L<<250.0,500.0>--<241.0,400.0>> = 9.716685817785075 and uni20A9 (U+20A9): L<<329.0,313.0>--<340.0,187.0>>/L<<340.0,187.0>--<351.0,313.0>> = 9.978725139284375 [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[11] RadioCanadaCondensed-LightItalic.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l

   [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
<pre>--- Rationale ---
According to a GlyphsApp tutorial [1], in order to make sure all versions of
Windows recognize it as a valid font file, we must make sure that the
concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style
(NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20
characters.
After discussing the problem in more detail at `FontBakery issue #2179 [2] we
decided that allowing up to 27 chars would still be on the safe side, though.
[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances
[2] https://github.com/googlefonts/fontbakery/issues/2179</pre>

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Radio Canada Condensed Light' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - six.pl
 - five.pl
 - uni20A6.BRACKET.100
 - dollar.BRACKET.100
 - four.pl
 - one.pl
 - eight.pl
 - uni030C.alt
 - nine.pl
 - two.pl
 - cent.BRACKET.100
 - uni20B2.BRACKET.100
 - three.pl
 - seven.pl 
 - zero.pl
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: Gammalatin	Contours detected: 0	Expected: 2
 - Glyph name: Iotalatin	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Upsilonlatin	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni01EA	Contours detected: 3	Expected: 2
 - Glyph name: uni01EB	Contours detected: 3	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

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
	* ae (U+00E6) contains a short segment B<<322.0,342.0>-<323.0,351.0>-<323.5,357.0>> and 42 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<103.0,180.0>--<164.0,510.0>> -> L<<164.0,510.0>--<203.0,690.0>>
	* exclam (U+0021): L<<265.0,690.0>--<226.0,510.0>> -> L<<226.0,510.0>--<147.0,180.0>>
	* exclamdown (U+00A1): L<<18.0,-185.0>--<58.0,0.0>> -> L<<58.0,0.0>--<137.0,330.0>>
	* exclamdown (U+00A1): L<<181.0,330.0>--<120.0,0.0>> -> L<<120.0,0.0>--<80.0,-185.0>> and less (U+003C): L<<80.0,264.0>--<88.0,300.0>> -> L<<88.0,300.0>--<91.0,316.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni20A9 (U+20A9): L<<150.0,345.0>--<131.0,152.0>>/L<<131.0,152.0>--<198.0,345.0>> = 13.522057184106938 and uni20A9 (U+20A9): L<<339.0,345.0>--<324.0,152.0>>/L<<324.0,152.0>--<386.0,345.0>> = 13.36517263202207 [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[11] RadioCanada-Light.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

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

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - grave.cap
 - one.lf
 - hungarumlaut.cap
 - uni030C.alt
 - dotaccent.cap
 - ring.cap
 - caron.cap
 - zero.lf
 - seven.lf
 - five.lf
 - dotbelow
 - two.lf
 - uni20B2.BRACKET.100
 - acute.cap
 - ring_acute.cap
 - dieresis.cap
 - circumflex.cap
 - four.lf
 - uni20A6.BRACKET.100
 - uni0313.short
 - three.lf
 - eight.lf
 - dollar.BRACKET.100
 - six.lf
 - breve.cap
 - tilde.cap
 - caron.alt
 - uni0326
 - cent.BRACKET.100
 - macron.cap
 - uni0326.alt 
 - nine.lf
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

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
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni023A	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

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
	* Lcaron (U+013D): X=382.0,Y=692.0 (should be at cap-height 690?) and 42 more. [code: found-misalignments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

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
	* uni018F (U+018F) contains a short segment B<<70.0,325.0>-<70.0,333.0>-<70.5,343.0>> and 13 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<131.0,180.0>--<122.0,510.0>> -> L<<122.0,510.0>--<122.0,690.0>>
	* exclam (U+0021): L<<184.0,690.0>--<184.0,510.0>> -> L<<184.0,510.0>--<175.0,180.0>>
	* exclamdown (U+00A1): L<<122.0,-185.0>--<122.0,0.0>> -> L<<122.0,0.0>--<131.0,330.0>> and exclamdown (U+00A1): L<<175.0,330.0>--<184.0,0.0>> -> L<<184.0,0.0>--<184.0,-185.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni023A (U+023A): L<<162.0,226.0>--<119.0,105.0>>/L<<119.0,105.0>--<186.0,226.0>> = 9.410348931967583 [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[12] RadioCanadaCondensed-Regular.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

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

</details>
<details>
<summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
<pre>--- Rationale ---
According to a GlyphsApp tutorial [1], in order to make sure all versions of
Windows recognize it as a valid font file, we must make sure that the
concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style
(NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20
characters.
After discussing the problem in more detail at `FontBakery issue #2179 [2] we
decided that allowing up to 27 chars would still be on the safe side, though.
[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances
[2] https://github.com/googlefonts/fontbakery/issues/2179</pre>

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Radio Canada Condensed' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - grave.cap
 - one.lf
 - hungarumlaut.cap
 - uni030C.alt
 - dotaccent.cap
 - ring.cap
 - caron.cap
 - zero.lf
 - seven.lf
 - five.lf
 - dotbelow
 - two.lf
 - uni20B2.BRACKET.100
 - acute.cap
 - ring_acute.cap
 - dieresis.cap
 - circumflex.cap
 - four.lf
 - uni20A6.BRACKET.100
 - uni0313.short
 - three.lf
 - eight.lf
 - dollar.BRACKET.100
 - six.lf
 - breve.cap
 - tilde.cap
 - caron.alt
 - uni0326
 - cent.BRACKET.100
 - macron.cap
 - uni0326.alt 
 - nine.lf
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

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
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* nine (U+0039): X=134.5,Y=1.5 (should be at baseline 0?)
	* f (U+0066): X=16.0,Y=514.0 (should be at x-height 515?)
	* f (U+0066): X=92.0,Y=514.0 (should be at x-height 515?)
	* f (U+0066): X=180.0,Y=514.0 (should be at x-height 515?)
	* f (U+0066): X=305.0,Y=514.0 (should be at x-height 515?)
	* dieresis (U+00A8): X=-83.0,Y=688.0 (should be at cap-height 690?)
	* dieresis (U+00A8): X=85.0,Y=688.0 (should be at cap-height 690?)
	* ordfeminine (U+00AA): X=111.5,Y=689.0 (should be at cap-height 690?)
	* uni03BC.math (U+00B5): X=476.0,Y=-2.0 (should be at baseline 0?)
	* uni03BC.math (U+00B5): X=184.5,Y=-1.0 (should be at baseline 0?) and 56 more. [code: found-misalignments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* R (U+0052) contains a short segment B<<252.0,261.0>-<246.0,261.0>-<240.0,261.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<465.0,69.0>-<468.0,69.0>-<470.5,69.5>>
	* uni03BC.math (U+00B5) contains a short segment B<<470.5,69.5>-<473.0,70.0>-<476.0,71.0>>
	* ae (U+00E6) contains a short segment L<<304.0,307.0>--<304.0,314.0>>
	* ae (U+00E6) contains a short segment B<<677.0,266.0>-<677.0,258.0>-<676.5,249.0>>
	* ae (U+00E6) contains a short segment B<<676.5,249.0>-<676.0,240.0>-<675.0,231.0>>
	* Eng (U+014A) contains a short segment B<<337.0,-108.0>-<348.0,-112.0>-<358.0,-114.5>>
	* Eng (U+014A) contains a short segment B<<358.0,-114.5>-<368.0,-117.0>-<379.0,-117.0>>
	* Racute (U+0154) contains a short segment B<<252.0,261.0>-<246.0,261.0>-<240.0,261.0>>
	* uni0156 (U+0156) contains a short segment B<<252.0,261.0>-<246.0,261.0>-<240.0,261.0>> and 18 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* at (U+0040): L<<495.0,139.0>--<494.0,152.0>> -> L<<494.0,152.0>--<494.0,298.0>>
	* exclam (U+0021): L<<106.0,206.0>--<92.0,514.0>> -> L<<92.0,514.0>--<92.0,690.0>>
	* exclam (U+0021): L<<186.0,690.0>--<186.0,514.0>> -> L<<186.0,514.0>--<172.0,206.0>>
	* exclamdown (U+00A1): L<<172.0,308.0>--<186.0,0.0>> -> L<<186.0,0.0>--<186.0,-185.0>> and exclamdown (U+00A1): L<<92.0,-185.0>--<92.0,0.0>> -> L<<92.0,0.0>--<106.0,308.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni023A (U+023A): L<<261.0,575.0>--<184.0,291.0>>/L<<184.0,291.0>--<281.0,503.0>> = 9.416599393151033
	* uni20A9 (U+20A9): L<<146.0,322.0>--<158.0,198.0>>/L<<158.0,198.0>--<171.0,322.0>> = 11.51249246677156
	* uni20A9 (U+20A9): L<<260.0,399.0>--<250.0,497.0>>/L<<250.0,497.0>--<240.0,399.0>> = 11.652684059111523 and uni20A9 (U+20A9): L<<329.0,322.0>--<342.0,198.0>>/L<<342.0,198.0>--<354.0,322.0>> = 11.51249246677156 [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[12] RadioCanadaCondensed-SemiBold.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

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

</details>
<details>
<summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
<pre>--- Rationale ---
According to a GlyphsApp tutorial [1], in order to make sure all versions of
Windows recognize it as a valid font file, we must make sure that the
concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style
(NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20
characters.
After discussing the problem in more detail at `FontBakery issue #2179 [2] we
decided that allowing up to 27 chars would still be on the safe side, though.
[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances
[2] https://github.com/googlefonts/fontbakery/issues/2179</pre>

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Radio Canada Condensed SemiBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - grave.cap
 - one.lf
 - hungarumlaut.cap
 - uni030C.alt
 - dotaccent.cap
 - ring.cap
 - caron.cap
 - zero.lf
 - seven.lf
 - five.lf
 - dotbelow
 - two.lf
 - uni20B2.BRACKET.100
 - acute.cap
 - ring_acute.cap
 - dieresis.cap
 - circumflex.cap
 - four.lf
 - uni20A6.BRACKET.100
 - uni0313.short
 - three.lf
 - eight.lf
 - dollar.BRACKET.100
 - six.lf
 - breve.cap
 - tilde.cap
 - caron.alt
 - uni0326
 - cent.BRACKET.100
 - macron.cap
 - uni0326.alt 
 - nine.lf
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

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
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: lessequal	Contours detected: 1	Expected: 2
 - Glyph name: greaterequal	Contours detected: 1	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: greaterequal	Contours detected: 1	Expected: 2
 - Glyph name: lessequal	Contours detected: 1	Expected: 2
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* a (U+0061) contains a short segment L<<286.0,314.0>--<286.0,323.0>>
	* f (U+0066) contains a short segment L<<89.0,521.0>--<89.0,532.0>>
	* sterling (U+00A3) contains a short segment B<<258.0,286.0>-<259.0,277.0>-<259.0,268.0>>
	* ordfeminine (U+00AA) contains a short segment L<<227.0,533.0>--<227.0,539.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<490.0,106.0>-<497.0,106.0>-<506.0,108.0>>
	* agrave (U+00E0) contains a short segment L<<286.0,314.0>--<286.0,323.0>>
	* aacute (U+00E1) contains a short segment L<<286.0,314.0>--<286.0,323.0>>
	* acircumflex (U+00E2) contains a short segment L<<286.0,314.0>--<286.0,323.0>>
	* atilde (U+00E3) contains a short segment L<<286.0,314.0>--<286.0,323.0>>
	* adieresis (U+00E4) contains a short segment L<<286.0,314.0>--<286.0,323.0>> and 44 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<103.0,246.0>--<83.0,522.0>> -> L<<83.0,522.0>--<83.0,690.0>>
	* exclam (U+0021): L<<216.0,690.0>--<216.0,522.0>> -> L<<216.0,522.0>--<195.0,246.0>>
	* exclamdown (U+00A1): L<<195.0,276.0>--<216.0,0.0>> -> L<<216.0,0.0>--<216.0,-185.0>>
	* exclamdown (U+00A1): L<<83.0,-185.0>--<83.0,0.0>> -> L<<83.0,0.0>--<103.0,276.0>> and uni01E5 (U+01E5): L<<325.0,19.0>--<325.0,25.0>> -> L<<325.0,25.0>--<325.0,89.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni023A (U+023A): L<<270.0,530.0>--<192.0,233.0>>/L<<192.0,233.0>--<292.0,446.0>> = 10.434212353277005
	* uni20A9 (U+20A9): L<<152.0,306.0>--<161.0,182.0>>/L<<161.0,182.0>--<171.0,306.0>> = 8.761934585082285
	* uni20A9 (U+20A9): L<<257.0,402.0>--<249.0,500.0>>/L<<249.0,500.0>--<242.0,402.0>> = 8.752475151413872 and uni20A9 (U+20A9): L<<329.0,306.0>--<339.0,179.0>>/L<<339.0,179.0>--<348.0,306.0>> = 8.555743723872405 [code: found-jaggy-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines?</summary>

* [com.google.fonts/check/outline_semi_vertical](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical)
<pre>--- Rationale ---
This check detects line segments which are nearly, but not quite, exactly
horizontal or vertical. Sometimes such lines are created by design, but often
they are indicative of a design error.
This check is disabled for italic styles, which often contain nearly-upright
lines.</pre>

* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * greater (U+003E): L<<75.0,399.0>--<74.0,533.0>> and greater (U+003E): L<<75.0,43.0>--<74.0,181.0>> [code: found-semi-vertical]

</details>
<br>
</details>
<details>
<summary><b>[10] RadioCanadaCondensed-Bold.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

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

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - grave.cap
 - one.lf
 - hungarumlaut.cap
 - uni030C.alt
 - dotaccent.cap
 - ring.cap
 - caron.cap
 - zero.lf
 - seven.lf
 - five.lf
 - dotbelow
 - two.lf
 - uni20B2.BRACKET.100
 - acute.cap
 - ring_acute.cap
 - dieresis.cap
 - circumflex.cap
 - four.lf
 - uni20A6.BRACKET.100
 - uni0313.short
 - three.lf
 - eight.lf
 - dollar.BRACKET.100
 - six.lf
 - breve.cap
 - tilde.cap
 - caron.alt
 - uni0326
 - cent.BRACKET.100
 - macron.cap
 - uni0326.alt 
 - nine.lf
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

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
 - Glyph name: uni023E	Contours detected: 1	Expected: 2
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: estimated	Contours detected: 3	Expected: 2
 - Glyph name: lessequal	Contours detected: 1	Expected: 2
 - Glyph name: greaterequal	Contours detected: 1	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: estimated	Contours detected: 3	Expected: 2
 - Glyph name: greaterequal	Contours detected: 1	Expected: 2
 - Glyph name: lessequal	Contours detected: 1	Expected: 2
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 1	Expected: 2
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* at (U+0040) contains a short segment B<<648.0,101.0>-<663.0,101.0>-<676.0,116.5>>
	* a (U+0061) contains a short segment L<<278.0,317.0>--<278.0,318.0>>
	* sterling (U+00A3) contains a short segment B<<269.0,282.0>-<269.0,277.0>-<269.0,271.0>>
	* agrave (U+00E0) contains a short segment L<<278.0,317.0>--<278.0,318.0>>
	* aacute (U+00E1) contains a short segment L<<278.0,317.0>--<278.0,318.0>>
	* acircumflex (U+00E2) contains a short segment L<<278.0,317.0>--<278.0,318.0>>
	* atilde (U+00E3) contains a short segment L<<278.0,317.0>--<278.0,318.0>>
	* adieresis (U+00E4) contains a short segment L<<278.0,317.0>--<278.0,318.0>>
	* aring (U+00E5) contains a short segment L<<278.0,317.0>--<278.0,318.0>>
	* ae (U+00E6) contains a short segment L<<279.0,317.0>--<279.0,318.0>> and 42 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<102.0,265.0>--<78.0,526.0>> -> L<<78.0,526.0>--<78.0,690.0>>
	* exclam (U+0021): L<<230.0,690.0>--<230.0,526.0>> -> L<<230.0,526.0>--<206.0,265.0>>
	* exclamdown (U+00A1): L<<206.0,261.0>--<230.0,0.0>> -> L<<230.0,0.0>--<230.0,-185.0>> and exclamdown (U+00A1): L<<78.0,-185.0>--<78.0,0.0>> -> L<<78.0,0.0>--<102.0,261.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* estimated (U+212E): B<<509.0,577.0>-<503.0,584.0>-<495.0,591.0>>/L<<495.0,591.0>--<509.0,577.0>> = 3.814074834290474
	* estimated (U+212E): L<<495.0,591.0>--<509.0,577.0>>/B<<509.0,577.0>-<503.0,584.0>-<495.0,591.0>> = 4.398705354995591
	* uni026C (U+026C): B<<84.0,534.0>-<139.0,534.0>-<155.0,469.0>>/L<<155.0,469.0>--<155.0,715.0>> = 13.828650972280153
	* uni20A9 (U+20A9): L<<154.0,298.0>--<162.0,177.0>>/L<<162.0,177.0>--<170.0,298.0>> = 7.5652908931925795
	* uni20A9 (U+20A9): L<<255.0,403.0>--<249.0,496.0>>/L<<249.0,496.0>--<243.0,403.0>> = 7.382771972902524
	* uni20A9 (U+20A9): L<<328.0,298.0>--<338.0,172.0>>/L<<338.0,172.0>--<346.0,298.0>> = 8.170723247394802 and uniA7AD (U+A7AD): B<<82.0,565.0>-<137.0,565.0>-<153.0,500.0>>/L<<153.0,500.0>--<153.0,690.0>> = 13.828650972280153 [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[12] RadioCanadaCondensed-MediumItalic.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l

   [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
<pre>--- Rationale ---
According to a GlyphsApp tutorial [1], in order to make sure all versions of
Windows recognize it as a valid font file, we must make sure that the
concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style
(NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20
characters.
After discussing the problem in more detail at `FontBakery issue #2179 [2] we
decided that allowing up to 27 chars would still be on the safe side, though.
[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances
[2] https://github.com/googlefonts/fontbakery/issues/2179</pre>

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Radio Canada Condensed Medium' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - six.pl
 - five.pl
 - uni20A6.BRACKET.100
 - dollar.BRACKET.100
 - four.pl
 - one.pl
 - eight.pl
 - uni030C.alt
 - nine.pl
 - two.pl
 - cent.BRACKET.100
 - uni20B2.BRACKET.100
 - three.pl
 - seven.pl 
 - zero.pl
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: Gammalatin	Contours detected: 0	Expected: 2
 - Glyph name: Iotalatin	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Upsilonlatin	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni01EA	Contours detected: 3	Expected: 2
 - Glyph name: uni01EB	Contours detected: 3	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=388.0,Y=691.0 (should be at cap-height 690?)
	* dollar (U+0024): X=148.0,Y=-2.0 (should be at baseline 0?)
	* six (U+0036): X=452.5,Y=690.5 (should be at cap-height 690?)
	* nine (U+0039): X=74.5,Y=-0.5 (should be at baseline 0?)
	* at (U+0040): X=326.0,Y=-1.0 (should be at baseline 0?)
	* g (U+0067): X=328.0,Y=517.5 (should be at x-height 519?)
	* dieresis (U+00A8): X=305.0,Y=688.0 (should be at cap-height 690?)
	* dieresis (U+00A8): X=480.0,Y=688.0 (should be at cap-height 690?)
	* uni03BC.math (U+00B5): X=436.0,Y=-1.0 (should be at baseline 0?)
	* onequarter (U+00BC): X=295.0,Y=691.0 (should be at cap-height 690?) and 45 more. [code: found-misalignments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* uni03BC.math (U+00B5) contains a short segment B<<440.0,84.0>-<445.0,84.0>-<449.0,85.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<449.0,85.0>-<453.0,86.0>-<456.0,87.0>>
	* oe (U+0153) contains a short segment B<<437.0,225.0>-<430.0,225.0>-<423.0,225.0>>
	* uni03BC (U+03BC) contains a short segment B<<440.0,84.0>-<445.0,84.0>-<449.0,85.0>>
	* uni03BC (U+03BC) contains a short segment B<<449.0,85.0>-<453.0,86.0>-<456.0,87.0>>
	* colonmonetary (U+20A1) contains a short segment B<<482.0,536.0>-<480.0,538.0>-<479.0,540.0>>
	* lira (U+20A4) contains a short segment B<<256.0,495.0>-<254.0,485.0>-<253.0,474.0>>
	* peseta (U+20A7) contains a short segment B<<481.0,506.0>-<481.0,502.0>-<481.0,499.0>>
	* uni20AD (U+20AD) contains a short segment L<<320.0,389.0>--<323.0,382.0>> and uni20AD (U+20AD) contains a short segment L<<245.0,295.0>--<236.0,295.0>> [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<289.0,690.0>--<252.0,518.0>> -> L<<252.0,518.0>--<170.0,226.0>>
	* exclam (U+0021): L<<93.0,226.0>--<136.0,518.0>> -> L<<136.0,518.0>--<172.0,690.0>>
	* exclamdown (U+00A1): L<<-13.0,-185.0>--<26.0,0.0>> -> L<<26.0,0.0>--<107.0,292.0>> and exclamdown (U+00A1): L<<185.0,292.0>--<141.0,0.0>> -> L<<141.0,0.0>--<102.0,-185.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni20A9 (U+20A9): L<<161.0,313.0>--<145.0,189.0>>/L<<145.0,189.0>--<182.0,313.0>> = 9.262045129234014
	* uni20A9 (U+20A9): L<<289.0,400.0>--<301.0,500.0>>/L<<301.0,500.0>--<271.0,400.0>> = 9.856470821362652 and uni20A9 (U+20A9): L<<340.0,313.0>--<325.0,187.0>>/L<<325.0,187.0>--<363.0,313.0>> = 9.993669570831868 [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[10] RadioCanadaCondensed-BoldItalic.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l

   [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
<pre>--- Rationale ---
According to a GlyphsApp tutorial [1], in order to make sure all versions of
Windows recognize it as a valid font file, we must make sure that the
concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style
(NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20
characters.
After discussing the problem in more detail at `FontBakery issue #2179 [2] we
decided that allowing up to 27 chars would still be on the safe side, though.
[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances
[2] https://github.com/googlefonts/fontbakery/issues/2179</pre>

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Radio Canada Condensed' / SUBFAMILY_NAME = 'Bold Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - six.pl
 - five.pl
 - uni20A6.BRACKET.100
 - dollar.BRACKET.100
 - four.pl
 - one.pl
 - eight.pl
 - uni030C.alt
 - nine.pl
 - two.pl
 - cent.BRACKET.100
 - uni20B2.BRACKET.100
 - three.pl
 - seven.pl 
 - zero.pl
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: Gammalatin	Contours detected: 0	Expected: 2
 - Glyph name: Iotalatin	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Upsilonlatin	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni01EA	Contours detected: 3	Expected: 2
 - Glyph name: uni01EB	Contours detected: 3	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1
 - Glyph name: lessequal	Contours detected: 1	Expected: 2
 - Glyph name: greaterequal	Contours detected: 1	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: greaterequal	Contours detected: 1	Expected: 2
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: lessequal	Contours detected: 1	Expected: 2
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<317.0,690.0>--<282.0,526.0>> -> L<<282.0,526.0>--<202.0,265.0>>
	* exclam (U+0021): L<<98.0,265.0>--<130.0,526.0>> -> L<<130.0,526.0>--<165.0,690.0>>
	* exclamdown (U+00A1): L<<-21.0,-185.0>--<18.0,-1.0>> -> L<<18.0,-1.0>--<98.0,260.0>>
	* exclamdown (U+00A1): L<<202.0,260.0>--<170.0,-1.0>> -> L<<170.0,-1.0>--<131.0,-185.0>>
	* greaterequal (U+2265): L<<26.0,59.0>--<51.0,180.0>> -> L<<51.0,180.0>--<83.0,329.0>> and lessequal (U+2264): L<<436.0,317.0>--<407.0,180.0>> -> L<<407.0,180.0>--<382.0,59.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* currency (U+00A4): L<<461.0,447.0>--<461.0,448.0>>/B<<461.0,448.0>-<466.0,421.0>-<466.0,391.0>> = 10.491477012331599
	* trademark (U+2122): L<<650.0,290.0>--<714.0,590.0>>/L<<714.0,590.0>--<605.0,369.0>> = 14.210523874331708
	* uni20A9 (U+20A9): L<<162.0,298.0>--<144.0,177.0>>/L<<144.0,177.0>--<178.0,298.0>> = 7.233636000848635
	* uni20A9 (U+20A9): L<<285.0,403.0>--<299.0,496.0>>/L<<299.0,496.0>--<274.0,403.0>> = 6.485502261033817 and uni20A9 (U+20A9): L<<336.0,298.0>--<319.0,172.0>>/L<<319.0,172.0>--<353.0,298.0>> = 7.417116331651419 [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[11] RadioCanada-SemiBoldItalic.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l

   [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - six.pl
 - five.pl
 - uni20A6.BRACKET.100
 - dollar.BRACKET.100
 - four.pl
 - one.pl
 - eight.pl
 - uni030C.alt
 - nine.pl
 - two.pl
 - cent.BRACKET.100
 - uni20B2.BRACKET.100
 - three.pl
 - seven.pl 
 - zero.pl
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: Gammalatin	Contours detected: 0	Expected: 2
 - Glyph name: Iotalatin	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Upsilonlatin	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni01EA	Contours detected: 3	Expected: 2
 - Glyph name: uni01EB	Contours detected: 3	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1
 - Glyph name: lessequal	Contours detected: 1	Expected: 2
 - Glyph name: greaterequal	Contours detected: 1	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: greaterequal	Contours detected: 1	Expected: 2
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: lessequal	Contours detected: 1	Expected: 2
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=446.0,Y=689.0 (should be at cap-height 690?)
	* parenright (U+0029): X=-95.0,Y=-253.0 (should be at descender -255?)
	* six (U+0036): X=539.5,Y=689.5 (should be at cap-height 690?)
	* nine (U+0039): X=93.0,Y=1.0 (should be at baseline 0?)
	* i (U+0069): X=303.0,Y=688.0 (should be at cap-height 690?)
	* j (U+006A): X=303.0,Y=688.0 (should be at cap-height 690?)
	* braceright (U+007D): X=180.0,Y=691.5 (should be at cap-height 690?)
	* uni03BC.math (U+00B5): X=169.0,Y=1.5 (should be at baseline 0?)
	* onequarter (U+00BC): X=862.0,Y=-1.0 (should be at baseline 0?)
	* onequarter (U+00BC): X=758.0,Y=-1.0 (should be at baseline 0?) and 74 more. [code: found-misalignments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* R (U+0052) contains a short segment B<<305.0,247.0>-<301.0,247.0>-<297.0,247.0>>
	* h (U+0068) contains a short segment B<<419.0,333.5>-<420.0,342.0>-<420.0,351.0>>
	* m (U+006D) contains a short segment B<<705.0,314.0>-<707.0,325.0>-<708.0,333.5>>
	* m (U+006D) contains a short segment B<<708.0,333.5>-<709.0,342.0>-<709.0,351.0>>
	* m (U+006D) contains a short segment B<<392.0,314.0>-<394.0,325.0>-<395.0,333.5>>
	* m (U+006D) contains a short segment B<<395.0,333.5>-<396.0,342.0>-<396.0,351.0>>
	* Oslash (U+00D8) contains a short segment B<<195.0,265.0>-<195.0,265.0>-<195.0,263.0>>
	* ae (U+00E6) contains a short segment B<<357.0,336.0>-<358.0,344.0>-<358.0,349.0>>
	* ae (U+00E6) contains a short segment B<<482.0,219.0>-<476.0,219.0>-<470.0,219.0>>
	* ae (U+00E6) contains a short segment B<<470.0,219.0>-<469.0,209.0>-<469.0,199.0>> and 37 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<107.0,243.0>--<148.0,522.0>> -> L<<148.0,522.0>--<183.0,690.0>>
	* exclam (U+0021): L<<328.0,690.0>--<292.0,522.0>> -> L<<292.0,522.0>--<207.0,243.0>>
	* exclamdown (U+00A1): L<<-3.0,-185.0>--<36.0,0.0>> -> L<<36.0,0.0>--<120.0,279.0>>
	* exclamdown (U+00A1): L<<220.0,279.0>--<181.0,0.0>> -> L<<181.0,0.0>--<142.0,-185.0>>
	* greater (U+003E): L<<539.0,342.0>--<527.0,284.0>> -> L<<527.0,284.0>--<517.0,235.0>>
	* less (U+003C): L<<63.0,235.0>--<72.0,276.0>> -> L<<72.0,276.0>--<86.0,342.0>>
	* trademark (U+2122): L<<776.0,689.0>--<839.0,690.0>> -> L<<839.0,690.0>--<839.0,690.0>> and trademark (U+2122): L<<839.0,690.0>--<839.0,690.0>> -> L<<839.0,690.0>--<929.0,690.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni20A9 (U+20A9): L<<184.0,306.0>--<167.0,170.0>>/L<<167.0,170.0>--<209.0,306.0>> = 10.036902453963481
	* uni20A9 (U+20A9): L<<341.0,402.0>--<353.0,515.0>>/L<<353.0,515.0>--<318.0,402.0>> = 11.147768731819275 and uni20A9 (U+20A9): L<<409.0,306.0>--<394.0,167.0>>/L<<394.0,167.0>--<436.0,306.0>> = 10.653463206281126 [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[11] RadioCanada-Medium.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

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

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - grave.cap
 - one.lf
 - hungarumlaut.cap
 - uni030C.alt
 - dotaccent.cap
 - ring.cap
 - caron.cap
 - zero.lf
 - seven.lf
 - five.lf
 - dotbelow
 - two.lf
 - uni20B2.BRACKET.100
 - acute.cap
 - ring_acute.cap
 - dieresis.cap
 - circumflex.cap
 - four.lf
 - uni20A6.BRACKET.100
 - uni0313.short
 - three.lf
 - eight.lf
 - dollar.BRACKET.100
 - six.lf
 - breve.cap
 - tilde.cap
 - caron.alt
 - uni0326
 - cent.BRACKET.100
 - macron.cap
 - uni0326.alt 
 - nine.lf
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

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
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* six (U+0036): X=443.5,Y=688.5 (should be at cap-height 690?)
	* nine (U+0039): X=156.5,Y=1.5 (should be at baseline 0?)
	* aring (U+00E5): X=151.0,Y=691.0 (should be at cap-height 690?)
	* aring (U+00E5): X=380.0,Y=691.0 (should be at cap-height 690?)
	* aring (U+00E5): X=151.0,Y=691.0 (should be at cap-height 690?)
	* aring (U+00E5): X=219.0,Y=691.0 (should be at cap-height 690?)
	* aring (U+00E5): X=311.0,Y=691.0 (should be at cap-height 690?)
	* aring (U+00E5): X=219.0,Y=691.0 (should be at cap-height 690?)
	* uni0123 (U+0123): X=313.0,Y=692.0 (should be at cap-height 690?)
	* Uring (U+016E): X=276.0,Y=943.5 (should be at ascender 945?) and 53 more. [code: found-misalignments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

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
	* adieresis (U+00E4) contains a short segment L<<356.0,310.0>--<356.0,315.0>> and 40 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<125.0,228.0>--<105.0,519.0>> -> L<<105.0,519.0>--<105.0,690.0>>
	* exclam (U+0021): L<<230.0,690.0>--<230.0,519.0>> -> L<<230.0,519.0>--<210.0,228.0>>
	* exclamdown (U+00A1): L<<105.0,-185.0>--<105.0,0.0>> -> L<<105.0,0.0>--<125.0,291.0>>
	* exclamdown (U+00A1): L<<210.0,291.0>--<230.0,0.0>> -> L<<230.0,0.0>--<230.0,-185.0>> and uni2C65 (U+2C65): L<<356.0,310.0>--<356.0,310.0>> -> L<<356.0,310.0>--<356.0,310.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni20A9 (U+20A9): L<<163.0,313.0>--<180.0,171.0>>/L<<180.0,171.0>--<198.0,313.0>> = 14.05117803251903 and uni20A9 (U+20A9): L<<314.0,400.0>--<298.0,524.0>>/L<<298.0,524.0>--<283.0,400.0>> = 14.249806917644122 [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[11] RadioCanada-Bold.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

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

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - grave.cap
 - one.lf
 - hungarumlaut.cap
 - uni030C.alt
 - dotaccent.cap
 - ring.cap
 - caron.cap
 - zero.lf
 - seven.lf
 - five.lf
 - dotbelow
 - two.lf
 - uni20B2.BRACKET.100
 - acute.cap
 - ring_acute.cap
 - dieresis.cap
 - circumflex.cap
 - four.lf
 - uni20A6.BRACKET.100
 - uni0313.short
 - three.lf
 - eight.lf
 - dollar.BRACKET.100
 - six.lf
 - breve.cap
 - tilde.cap
 - caron.alt
 - uni0326
 - cent.BRACKET.100
 - macron.cap
 - uni0326.alt 
 - nine.lf
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

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
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: estimated	Contours detected: 3	Expected: 2
 - Glyph name: lessequal	Contours detected: 1	Expected: 2
 - Glyph name: greaterequal	Contours detected: 1	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: estimated	Contours detected: 3	Expected: 2
 - Glyph name: greaterequal	Contours detected: 1	Expected: 2
 - Glyph name: lessequal	Contours detected: 1	Expected: 2
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

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
	* ntilde (U+00F1): X=198.5,Y=688.5 (should be at cap-height 690?) and 81 more. [code: found-misalignments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

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
	* acircumflex (U+00E2) contains a short segment L<<337.0,314.0>--<337.0,318.0>> and 41 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<122.0,260.0>--<96.0,525.0>> -> L<<96.0,525.0>--<96.0,690.0>>
	* exclam (U+0021): L<<262.0,690.0>--<262.0,525.0>> -> L<<262.0,525.0>--<236.0,260.0>>
	* exclamdown (U+00A1): L<<236.0,265.0>--<262.0,0.0>> -> L<<262.0,0.0>--<262.0,-185.0>>
	* exclamdown (U+00A1): L<<96.0,-185.0>--<96.0,0.0>> -> L<<96.0,0.0>--<122.0,265.0>> and uni01E5 (U+01E5): L<<385.0,36.0>--<385.0,42.0>> -> L<<385.0,42.0>--<385.0,112.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* estimated (U+212E): B<<509.0,577.0>-<503.0,584.0>-<495.0,591.0>>/L<<495.0,591.0>--<509.0,577.0>> = 3.814074834290474
	* estimated (U+212E): L<<495.0,591.0>--<509.0,577.0>>/B<<509.0,577.0>-<503.0,584.0>-<495.0,591.0>> = 4.398705354995591
	* uni026C (U+026C): B<<111.0,534.0>-<174.0,534.0>-<191.0,463.0>>/L<<191.0,463.0>--<191.0,715.0>> = 13.465208094811695
	* uni20A9 (U+20A9): L<<184.0,298.0>--<191.0,175.0>>/L<<191.0,175.0>--<200.0,298.0>> = 7.44213806578537
	* uni20A9 (U+20A9): L<<306.0,403.0>--<299.0,490.0>>/L<<299.0,490.0>--<292.0,403.0>> = 9.200191332526574
	* uni20A9 (U+20A9): L<<398.0,298.0>--<408.0,169.0>>/L<<408.0,169.0>--<416.0,298.0>> = 7.981350442594271 and uniA7AD (U+A7AD): B<<83.0,565.0>-<146.0,565.0>-<163.0,494.0>>/L<<163.0,494.0>--<163.0,690.0>> = 13.465208094811695 [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[12] RadioCanadaCondensed-Italic.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l

   [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
<pre>--- Rationale ---
According to a GlyphsApp tutorial [1], in order to make sure all versions of
Windows recognize it as a valid font file, we must make sure that the
concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style
(NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20
characters.
After discussing the problem in more detail at `FontBakery issue #2179 [2] we
decided that allowing up to 27 chars would still be on the safe side, though.
[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances
[2] https://github.com/googlefonts/fontbakery/issues/2179</pre>

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Radio Canada Condensed' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - six.pl
 - five.pl
 - uni20A6.BRACKET.100
 - dollar.BRACKET.100
 - four.pl
 - one.pl
 - eight.pl
 - uni030C.alt
 - nine.pl
 - two.pl
 - cent.BRACKET.100
 - uni20B2.BRACKET.100
 - three.pl
 - seven.pl 
 - zero.pl
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: Gammalatin	Contours detected: 0	Expected: 2
 - Glyph name: Iotalatin	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Upsilonlatin	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni01EA	Contours detected: 3	Expected: 2
 - Glyph name: uni01EB	Contours detected: 3	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* six (U+0036): X=442.5,Y=690.5 (should be at cap-height 690?)
	* nine (U+0039): X=84.5,Y=-0.5 (should be at baseline 0?)
	* g (U+0067): X=156.0,Y=-1.0 (should be at baseline 0?)
	* braceright (U+007D): X=40.5,Y=2.0 (should be at baseline 0?)
	* braceright (U+007D): X=122.5,Y=-1.5 (should be at baseline 0?)
	* dieresis (U+00A8): X=300.0,Y=691.0 (should be at cap-height 690?)
	* dieresis (U+00A8): X=468.0,Y=691.0 (should be at cap-height 690?)
	* Aring (U+00C5): X=310.0,Y=943.0 (should be at ascender 945?)
	* idieresis (U+00EF): X=165.0,Y=691.0 (should be at cap-height 690?)
	* idieresis (U+00EF): X=333.0,Y=691.0 (should be at cap-height 690?) and 40 more. [code: found-misalignments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* uni03BC.math (U+00B5) contains a short segment B<<425.0,63.0>-<431.0,63.0>-<435.5,64.5>>
	* uni03BC.math (U+00B5) contains a short segment B<<435.5,64.5>-<440.0,66.0>-<444.0,67.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<428.0,0.0>-<421.0,-4.0>-<411.5,-7.0>>
	* uni03BC (U+03BC) contains a short segment B<<425.0,63.0>-<431.0,63.0>-<435.5,64.5>>
	* uni03BC (U+03BC) contains a short segment B<<435.5,64.5>-<440.0,66.0>-<444.0,67.0>>
	* uni03BC (U+03BC) contains a short segment B<<428.0,0.0>-<421.0,-4.0>-<411.5,-7.0>>
	* pi (U+03C0) contains a short segment B<<393.0,66.0>-<398.0,66.0>-<403.5,67.5>>
	* pi (U+03C0) contains a short segment B<<403.5,67.5>-<409.0,69.0>-<413.0,70.0>>
	* colonmonetary (U+20A1) contains a short segment L<<390.0,700.0>--<394.0,700.0>>
	* uni20AD (U+20AD) contains a short segment L<<195.0,377.0>--<197.0,377.0>>
	* uni20AD (U+20AD) contains a short segment L<<304.0,390.0>--<309.0,377.0>> and uni20B9 (U+20B9) contains a short segment B<<453.0,517.0>-<453.0,515.0>-<453.0,513.0>> [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<273.0,690.0>--<235.0,514.0>> -> L<<235.0,514.0>--<153.0,204.0>>
	* exclam (U+0021): L<<90.0,204.0>--<140.0,514.0>> -> L<<140.0,514.0>--<176.0,690.0>>
	* exclamdown (U+00A1): L<<-9.0,-185.0>--<30.0,0.0>> -> L<<30.0,0.0>--<112.0,310.0>> and exclamdown (U+00A1): L<<175.0,310.0>--<125.0,0.0>> -> L<<125.0,0.0>--<86.0,-185.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni20A9 (U+20A9): L<<160.0,322.0>--<145.0,198.0>>/L<<145.0,198.0>--<185.0,322.0>> = 10.98126903808958
	* uni20A9 (U+20A9): L<<290.0,399.0>--<301.0,497.0>>/L<<301.0,497.0>--<270.0,399.0>> = 11.149192099955716 and uni20A9 (U+20A9): L<<343.0,322.0>--<329.0,198.0>>/L<<329.0,198.0>--<368.0,322.0>> = 11.017602536292145 [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[12] RadioCanadaCondensed-SemiBoldItalic.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l

   [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
<pre>--- Rationale ---
According to a GlyphsApp tutorial [1], in order to make sure all versions of
Windows recognize it as a valid font file, we must make sure that the
concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style
(NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20
characters.
After discussing the problem in more detail at `FontBakery issue #2179 [2] we
decided that allowing up to 27 chars would still be on the safe side, though.
[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances
[2] https://github.com/googlefonts/fontbakery/issues/2179</pre>

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Radio Canada Condensed SemiBold' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - six.pl
 - five.pl
 - uni20A6.BRACKET.100
 - dollar.BRACKET.100
 - four.pl
 - one.pl
 - eight.pl
 - uni030C.alt
 - nine.pl
 - two.pl
 - cent.BRACKET.100
 - uni20B2.BRACKET.100
 - three.pl
 - seven.pl 
 - zero.pl
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: Gammalatin	Contours detected: 0	Expected: 2
 - Glyph name: Iotalatin	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Upsilonlatin	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni01EA	Contours detected: 3	Expected: 2
 - Glyph name: uni01EB	Contours detected: 3	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1
 - Glyph name: lessequal	Contours detected: 1	Expected: 2
 - Glyph name: greaterequal	Contours detected: 1	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: greaterequal	Contours detected: 1	Expected: 2
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: lessequal	Contours detected: 1	Expected: 2
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=393.0,Y=691.0 (should be at cap-height 690?)
	* dollar (U+0024): X=137.0,Y=-1.0 (should be at baseline 0?)
	* g (U+0067): X=326.0,Y=522.5 (should be at x-height 522?)
	* braceleft (U+007B): X=178.0,Y=689.0 (should be at cap-height 690?)
	* exclamdown (U+00A1): X=22.0,Y=-1.0 (should be at baseline 0?)
	* exclamdown (U+00A1): X=155.0,Y=-1.0 (should be at baseline 0?)
	* section (U+00A7): X=387.0,Y=-1.0 (should be at baseline 0?)
	* uni03BC.math (U+00B5): X=444.0,Y=-1.0 (should be at baseline 0?)
	* onequarter (U+00BC): X=278.0,Y=691.0 (should be at cap-height 690?)
	* onequarter (U+00BC): X=346.0,Y=691.0 (should be at cap-height 690?) and 59 more. [code: found-misalignments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* ampersand (U+0026) contains a short segment L<<282.0,433.0>--<282.0,433.0>>
	* at (U+0040) contains a short segment B<<582.0,109.0>-<590.0,88.0>-<607.0,88.0>>
	* R (U+0052) contains a short segment B<<257.0,250.0>-<253.0,249.0>-<249.0,249.0>>
	* sterling (U+00A3) contains a short segment B<<267.0,286.0>-<266.0,277.0>-<264.0,268.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<453.0,103.0>-<460.0,103.0>-<467.0,106.0>>
	* ae (U+00E6) contains a short segment B<<300.0,334.5>-<301.0,344.0>-<301.0,352.0>>
	* Ccaron (U+010C) contains a short segment L<<349.0,765.0>--<349.0,765.0>>
	* ccaron (U+010D) contains a short segment L<<262.0,597.0>--<262.0,597.0>>
	* Dcaron (U+010E) contains a short segment L<<316.0,765.0>--<316.0,765.0>>
	* Ecaron (U+011A) contains a short segment L<<314.0,765.0>--<314.0,765.0>> and 42 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<303.0,690.0>--<267.0,522.0>> -> L<<267.0,522.0>--<186.0,245.0>>
	* exclam (U+0021): L<<95.0,245.0>--<133.0,522.0>> -> L<<133.0,522.0>--<169.0,690.0>>
	* exclamdown (U+00A1): L<<-17.0,-185.0>--<22.0,-1.0>> -> L<<22.0,-1.0>--<103.0,276.0>> and exclamdown (U+00A1): L<<193.0,276.0>--<155.0,-1.0>> -> L<<155.0,-1.0>--<116.0,-185.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* greaterequal (U+2265): L<<53.0,170.0>--<71.0,182.0>>/L<<71.0,182.0>--<54.0,176.0>> = 14.250032697803595
	* uni20A9 (U+20A9): L<<161.0,306.0>--<144.0,182.0>>/L<<144.0,182.0>--<180.0,306.0>> = 8.382805427791155
	* uni20A9 (U+20A9): L<<287.0,402.0>--<300.0,500.0>>/L<<300.0,500.0>--<272.0,402.0>> = 8.389051844483356 and uni20A9 (U+20A9): L<<338.0,306.0>--<322.0,179.0>>/L<<322.0,179.0>--<358.0,306.0>> = 8.645618578452384 [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[9] RadioCanada-LightItalic.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l

   [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - six.pl
 - five.pl
 - uni20A6.BRACKET.100
 - dollar.BRACKET.100
 - four.pl
 - one.pl
 - eight.pl
 - uni030C.alt
 - nine.pl
 - two.pl
 - cent.BRACKET.100
 - uni20B2.BRACKET.100
 - three.pl
 - seven.pl 
 - zero.pl
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: Gammalatin	Contours detected: 0	Expected: 2
 - Glyph name: Iotalatin	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Upsilonlatin	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni01EA	Contours detected: 3	Expected: 2
 - Glyph name: uni01EB	Contours detected: 3	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

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
	* uni019D (U+019D) contains a short segment B<<-114.0,-127.0>-<-103.0,-132.0>-<-88.0,-136.0>> and 15 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<103.0,180.0>--<164.0,510.0>> -> L<<164.0,510.0>--<203.0,690.0>>
	* exclam (U+0021): L<<265.0,690.0>--<226.0,510.0>> -> L<<226.0,510.0>--<147.0,180.0>>
	* exclamdown (U+00A1): L<<18.0,-185.0>--<58.0,0.0>> -> L<<58.0,0.0>--<137.0,330.0>>
	* exclamdown (U+00A1): L<<181.0,330.0>--<120.0,0.0>> -> L<<120.0,0.0>--<80.0,-185.0>> and less (U+003C): L<<80.0,264.0>--<88.0,300.0>> -> L<<88.0,300.0>--<91.0,316.0>> [code: found-colinear-vectors]

</details>
<br>
</details>
<details>
<summary><b>[10] RadioCanada-Italic.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l

   [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - six.pl
 - five.pl
 - uni20A6.BRACKET.100
 - dollar.BRACKET.100
 - four.pl
 - one.pl
 - eight.pl
 - uni030C.alt
 - nine.pl
 - two.pl
 - cent.BRACKET.100
 - uni20B2.BRACKET.100
 - three.pl
 - seven.pl 
 - zero.pl
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: Gammalatin	Contours detected: 0	Expected: 2
 - Glyph name: Iotalatin	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Upsilonlatin	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni01EA	Contours detected: 3	Expected: 2
 - Glyph name: uni01EB	Contours detected: 3	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* six (U+0036): X=535.0,Y=688.5 (should be at cap-height 690?)
	* nine (U+0039): X=103.0,Y=2.0 (should be at baseline 0?)
	* d (U+0064): X=381.5,Y=514.0 (should be at x-height 515?)
	* g (U+0067): X=382.0,Y=513.5 (should be at x-height 515?)
	* p (U+0070): X=187.5,Y=1.5 (should be at baseline 0?)
	* braceleft (U+007B): X=187.0,Y=-254.0 (should be at descender -255?)
	* braceright (U+007D): X=197.5,Y=691.0 (should be at cap-height 690?)
	* uni03BC.math (U+00B5): X=158.5,Y=-1.5 (should be at baseline 0?)
	* Aring (U+00C5): X=344.0,Y=944.5 (should be at ascender 945?)
	* germandbls (U+00DF): X=491.5,Y=691.0 (should be at cap-height 690?) and 21 more. [code: found-misalignments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* m (U+006D) contains a short segment B<<711.0,313.0>-<713.0,326.0>-<714.5,337.0>>
	* m (U+006D) contains a short segment B<<714.5,337.0>-<716.0,348.0>-<716.0,358.0>>
	* logicalnot (U+00AC) contains a short segment L<<520.0,249.0>--<520.0,249.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<502.0,67.0>-<510.0,67.0>-<515.5,68.5>>
	* uni03BC.math (U+00B5) contains a short segment B<<515.5,68.5>-<521.0,70.0>-<526.0,71.0>>
	* uni03BC.math (U+00B5) contains a short segment B<<511.0,0.0>-<502.0,-4.0>-<493.5,-7.0>>
	* ae (U+00E6) contains a short segment B<<365.5,341.5>-<367.0,352.0>-<367.0,361.0>>
	* aeacute (U+01FD) contains a short segment B<<365.5,341.5>-<367.0,352.0>-<367.0,361.0>>
	* uni03A9 (U+03A9) contains a short segment L<<242.0,27.0>--<242.0,27.0>>
	* uni03A9 (U+03A9) contains a short segment L<<242.0,27.0>--<242.0,27.0>> and 12 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<106.0,208.0>--<158.0,515.0>> -> L<<158.0,515.0>--<195.0,690.0>>
	* exclam (U+0021): L<<294.0,690.0>--<257.0,515.0>> -> L<<257.0,515.0>--<175.0,208.0>>
	* exclamdown (U+00A1): L<<11.0,-185.0>--<50.0,0.0>> -> L<<50.0,0.0>--<131.0,307.0>>
	* exclamdown (U+00A1): L<<200.0,307.0>--<149.0,0.0>> -> L<<149.0,0.0>--<110.0,-185.0>>
	* ohm (U+2126): L<<242.0,27.0>--<242.0,27.0>> -> L<<242.0,27.0>--<242.0,27.0>> and uni03A9 (U+03A9): L<<242.0,27.0>--<242.0,27.0>> -> L<<242.0,27.0>--<242.0,27.0>> [code: found-colinear-vectors]

</details>
<br>
</details>
<details>
<summary><b>[11] RadioCanada-MediumItalic.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l

   [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - six.pl
 - five.pl
 - uni20A6.BRACKET.100
 - dollar.BRACKET.100
 - four.pl
 - one.pl
 - eight.pl
 - uni030C.alt
 - nine.pl
 - two.pl
 - cent.BRACKET.100
 - uni20B2.BRACKET.100
 - three.pl
 - seven.pl 
 - zero.pl
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: Gammalatin	Contours detected: 0	Expected: 2
 - Glyph name: Iotalatin	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Upsilonlatin	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni01EA	Contours detected: 3	Expected: 2
 - Glyph name: uni01EB	Contours detected: 3	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=437.0,Y=691.0 (should be at cap-height 690?)
	* six (U+0036): X=537.5,Y=689.5 (should be at cap-height 690?)
	* nine (U+0039): X=97.5,Y=1.0 (should be at baseline 0?)
	* at (U+0040): X=393.0,Y=-2.0 (should be at baseline 0?)
	* d (U+0064): X=379.5,Y=519.5 (should be at x-height 519?)
	* braceright (U+007D): X=188.5,Y=691.5 (should be at cap-height 690?)
	* braceright (U+007D): X=155.0,Y=-2.0 (should be at baseline 0?)
	* section (U+00A7): X=463.0,Y=-1.0 (should be at baseline 0?)
	* uni03BC.math (U+00B5): X=163.0,Y=1.0 (should be at baseline 0?)
	* germandbls (U+00DF): X=494.0,Y=689.5 (should be at cap-height 690?) and 13 more. [code: found-misalignments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

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
	* hbar (U+0127) contains a short segment B<<429.5,335.0>-<431.0,345.0>-<431.0,354.0>> and 28 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<107.0,226.0>--<153.0,519.0>> -> L<<153.0,519.0>--<189.0,690.0>>
	* exclam (U+0021): L<<312.0,690.0>--<275.0,519.0>> -> L<<275.0,519.0>--<192.0,226.0>>
	* exclamdown (U+00A1): L<<210.0,292.0>--<166.0,0.0>> -> L<<166.0,0.0>--<127.0,-185.0>>
	* exclamdown (U+00A1): L<<4.0,-185.0>--<43.0,0.0>> -> L<<43.0,0.0>--<125.0,292.0>>
	* greater (U+003E): L<<535.0,335.0>--<521.0,270.0>> -> L<<521.0,270.0>--<515.0,242.0>>
	* less (U+003C): L<<67.0,242.0>--<72.0,267.0>> -> L<<72.0,267.0>--<87.0,335.0>>
	* trademark (U+2122): L<<773.0,690.0>--<831.0,690.0>> -> L<<831.0,690.0>--<831.0,690.0>> and trademark (U+2122): L<<831.0,690.0>--<831.0,690.0>> -> L<<831.0,690.0>--<911.0,690.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* greaterequal (U+2265): L<<551.0,403.0>--<551.0,404.0>>/L<<551.0,404.0>--<532.0,317.0>> = 12.319445256636591
	* greaterequal (U+2265): L<<555.0,421.0>--<551.0,403.0>>/L<<551.0,403.0>--<551.0,404.0>> = 12.528807709151492
	* litre (U+2113): L<<91.0,166.0>--<91.0,166.0>>/B<<91.0,166.0>-<64.0,160.0>-<37.0,155.0>> = 12.528807709151492
	* uni20A9 (U+20A9): L<<175.0,313.0>--<162.0,171.0>>/L<<162.0,171.0>--<210.0,313.0>> = 13.445894556636892
	* uni20A9 (U+20A9): L<<346.0,400.0>--<356.0,524.0>>/L<<356.0,524.0>--<314.0,400.0>> = 14.101088556439166 and uni20A9 (U+20A9): L<<412.0,313.0>--<400.0,170.0>>/L<<400.0,170.0>--<448.0,313.0>> = 13.758266618296407 [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[12] RadioCanadaCondensed-Light.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

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

</details>
<details>
<summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
<pre>--- Rationale ---
According to a GlyphsApp tutorial [1], in order to make sure all versions of
Windows recognize it as a valid font file, we must make sure that the
concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style
(NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20
characters.
After discussing the problem in more detail at `FontBakery issue #2179 [2] we
decided that allowing up to 27 chars would still be on the safe side, though.
[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances
[2] https://github.com/googlefonts/fontbakery/issues/2179</pre>

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Radio Canada Condensed Light' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - grave.cap
 - one.lf
 - hungarumlaut.cap
 - uni030C.alt
 - dotaccent.cap
 - ring.cap
 - caron.cap
 - zero.lf
 - seven.lf
 - five.lf
 - dotbelow
 - two.lf
 - uni20B2.BRACKET.100
 - acute.cap
 - ring_acute.cap
 - dieresis.cap
 - circumflex.cap
 - four.lf
 - uni20A6.BRACKET.100
 - uni0313.short
 - three.lf
 - eight.lf
 - dollar.BRACKET.100
 - six.lf
 - breve.cap
 - tilde.cap
 - caron.alt
 - uni0326
 - cent.BRACKET.100
 - macron.cap
 - uni0326.alt 
 - nine.lf
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

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
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni023A	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* six (U+0036): X=352.5,Y=688.0 (should be at cap-height 690?)
	* nine (U+0039): X=148.5,Y=2.0 (should be at baseline 0?)
	* Q (U+0051): X=340.0,Y=2.0 (should be at baseline 0?)
	* f (U+0066): X=116.5,Y=692.0 (should be at cap-height 690?)
	* Oslash (U+00D8): X=75.0,Y=-1.0 (should be at baseline 0?)
	* acircumflex (U+00E2): X=214.0,Y=689.0 (should be at cap-height 690?)
	* ecircumflex (U+00EA): X=228.0,Y=689.0 (should be at cap-height 690?)
	* icircumflex (U+00EE): X=102.0,Y=689.0 (should be at cap-height 690?)
	* ocircumflex (U+00F4): X=225.0,Y=689.0 (should be at cap-height 690?)
	* ucircumflex (U+00FB): X=230.0,Y=689.0 (should be at cap-height 690?) and 48 more. [code: found-misalignments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* uni03BC.math (U+00B5) contains a short segment B<<445.0,44.0>-<452.0,44.0>-<459.0,45.5>>
	* uni03BC.math (U+00B5) contains a short segment B<<459.0,45.5>-<466.0,47.0>-<471.0,48.0>>
	* ae (U+00E6) contains a short segment B<<646.5,261.0>-<646.0,252.0>-<645.0,244.0>>
	* uni01EB (U+01EB) contains a short segment B<<296.0,-7.0>-<290.0,-8.0>-<284.0,-8.0>>
	* uni01EB (U+01EB) contains a short segment B<<284.0,-8.0>-<278.0,-8.0>-<272.0,-8.0>>
	* aeacute (U+01FD) contains a short segment B<<646.5,261.0>-<646.0,252.0>-<645.0,244.0>>
	* uni023B (U+023B) contains a short segment B<<384.0,589.0>-<379.0,595.0>-<374.0,599.0>>
	* uni023E (U+023E) contains a short segment L<<363.0,636.0>--<363.0,636.0>>
	* uni023E (U+023E) contains a short segment L<<363.0,636.0>--<363.0,636.0>>
	* uni03BC (U+03BC) contains a short segment B<<445.0,44.0>-<452.0,44.0>-<459.0,45.5>> and 8 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<131.0,180.0>--<122.0,510.0>> -> L<<122.0,510.0>--<122.0,690.0>>
	* exclam (U+0021): L<<184.0,690.0>--<184.0,510.0>> -> L<<184.0,510.0>--<175.0,180.0>>
	* exclamdown (U+00A1): L<<122.0,-185.0>--<122.0,0.0>> -> L<<122.0,0.0>--<131.0,330.0>>
	* exclamdown (U+00A1): L<<175.0,330.0>--<184.0,0.0>> -> L<<184.0,0.0>--<184.0,-185.0>> and uni023E (U+023E): L<<363.0,636.0>--<363.0,636.0>> -> L<<363.0,636.0>--<363.0,636.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni023A (U+023A): L<<139.0,226.0>--<120.0,156.0>>/L<<120.0,156.0>--<149.0,226.0>> = 7.317691237566079
	* uni20A9 (U+20A9): L<<132.0,345.0>--<154.0,152.0>>/L<<154.0,152.0>--<180.0,345.0>> = 14.17546754466121 and uni20A9 (U+20A9): L<<321.0,345.0>--<347.0,152.0>>/L<<347.0,152.0>--<369.0,345.0>> = 14.17546754466121 [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[11] RadioCanada-BoldItalic.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l

   [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - six.pl
 - five.pl
 - uni20A6.BRACKET.100
 - dollar.BRACKET.100
 - four.pl
 - one.pl
 - eight.pl
 - uni030C.alt
 - nine.pl
 - two.pl
 - cent.BRACKET.100
 - uni20B2.BRACKET.100
 - three.pl
 - seven.pl 
 - zero.pl
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: Gammalatin	Contours detected: 0	Expected: 2
 - Glyph name: Iotalatin	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Upsilonlatin	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni01EA	Contours detected: 3	Expected: 2
 - Glyph name: uni01EB	Contours detected: 3	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1
 - Glyph name: lessequal	Contours detected: 1	Expected: 2
 - Glyph name: greaterequal	Contours detected: 1	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: chi	Contours detected: 0	Expected: 1
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: greaterequal	Contours detected: 1	Expected: 2
 - Glyph name: iota	Contours detected: 0	Expected: 1
 - Glyph name: lessequal	Contours detected: 1	Expected: 2
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: theta	Contours detected: 0	Expected: 3
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni0186	Contours detected: 0	Expected: 1
 - Glyph name: uni018E	Contours detected: 0	Expected: 1
 - Glyph name: uni0190	Contours detected: 0	Expected: 1
 - Glyph name: uni019A	Contours detected: 0	Expected: 1
 - Glyph name: uni019B	Contours detected: 0	Expected: 1
 - Glyph name: uni01DD	Contours detected: 0	Expected: 2
 - Glyph name: uni01E4	Contours detected: 0	Expected: 1
 - Glyph name: uni01E5	Contours detected: 0	Expected: 2
 - Glyph name: uni023A	Contours detected: 0	Expected: 3
 - Glyph name: uni023B	Contours detected: 0	Expected: 2
 - Glyph name: uni023C	Contours detected: 0	Expected: 2
 - Glyph name: uni023D	Contours detected: 2	Expected: 1
 - Glyph name: uni023E	Contours detected: 0	Expected: 2
 - Glyph name: uni0251	Contours detected: 0	Expected: 2
 - Glyph name: uni0261	Contours detected: 0	Expected: 2
 - Glyph name: uni02BA	Contours detected: 1	Expected: 2
 - Glyph name: uni0313	Contours detected: 0	Expected: 1
 - Glyph name: uni0325	Contours detected: 0	Expected: 2
 - Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: uni203F	Contours detected: 0	Expected: 1 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* exclam (U+0021): X=165.0,Y=2.0 (should be at baseline 0?)
	* parenleft (U+0028): X=160.0,Y=-256.0 (should be at descender -255?)
	* period (U+002E): X=130.0,Y=2.0 (should be at baseline 0?)
	* six (U+0036): X=542.0,Y=690.5 (should be at cap-height 690?)
	* nine (U+0039): X=88.5,Y=0.5 (should be at baseline 0?)
	* colon (U+003A): X=130.0,Y=2.0 (should be at baseline 0?)
	* question (U+003F): X=250.0,Y=2.0 (should be at baseline 0?)
	* i (U+0069): X=316.0,Y=692.0 (should be at cap-height 690?)
	* j (U+006A): X=316.0,Y=692.0 (should be at cap-height 690?)
	* j (U+006A): X=5.0,Y=2.0 (should be at baseline 0?) and 74 more. [code: found-misalignments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* at (U+0040) contains a short segment B<<696.5,115.5>-<707.0,98.0>-<726.0,98.0>>
	* R (U+0052) contains a short segment L<<299.0,240.0>--<298.0,240.0>>
	* bracketright (U+005D) contains a short segment L<<321.0,710.0>--<321.0,710.0>>
	* bracketright (U+005D) contains a short segment L<<132.0,-175.0>--<133.0,-175.0>>
	* e (U+0065) contains a short segment B<<175.0,214.0>-<175.0,210.0>-<175.0,205.0>>
	* f (U+0066) contains a short segment L<<153.0,525.0>--<156.0,538.0>>
	* h (U+0068) contains a short segment B<<411.0,315.0>-<413.0,324.0>-<414.0,332.0>>
	* h (U+0068) contains a short segment B<<414.0,332.0>-<415.0,340.0>-<415.0,347.0>>
	* m (U+006D) contains a short segment B<<702.0,315.0>-<704.0,324.0>-<705.0,332.0>>
	* m (U+006D) contains a short segment B<<705.0,332.0>-<706.0,340.0>-<706.0,347.0>> and 70 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* R (U+0052): L<<299.0,240.0>--<298.0,240.0>> -> L<<298.0,240.0>--<223.0,240.0>>
	* Racute (U+0154): L<<299.0,240.0>--<298.0,240.0>> -> L<<298.0,240.0>--<223.0,240.0>>
	* Rcaron (U+0158): L<<299.0,240.0>--<298.0,240.0>> -> L<<298.0,240.0>--<223.0,240.0>>
	* exclam (U+0021): L<<108.0,260.0>--<143.0,525.0>> -> L<<143.0,525.0>--<178.0,690.0>>
	* exclamdown (U+00A1): L<<229.0,265.0>--<196.0,0.0>> -> L<<196.0,0.0>--<157.0,-185.0>>
	* greater (U+003E): L<<544.0,349.0>--<533.0,299.0>> -> L<<533.0,299.0>--<518.0,227.0>>
	* greaterequal (U+2265): L<<41.0,60.0>--<66.0,179.0>> -> L<<66.0,179.0>--<97.0,317.0>>
	* less (U+003C): L<<58.0,227.0>--<71.0,285.0>> -> L<<71.0,285.0>--<84.0,349.0>>
	* lessequal (U+2264): L<<520.0,316.0>--<489.0,179.0>> -> L<<489.0,179.0>--<464.0,60.0>>
	* ohm (U+2126): L<<241.0,60.0>--<241.0,60.0>> -> L<<241.0,60.0>--<241.0,60.0>> and 9 more. [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni20A9 (U+20A9): L<<192.0,298.0>--<173.0,175.0>>/L<<173.0,175.0>--<208.0,298.0>> = 7.102690999535652
	* uni20A9 (U+20A9): L<<336.0,403.0>--<347.0,490.0>>/L<<347.0,490.0>--<322.0,403.0>> = 8.826282352552697 and uni20A9 (U+20A9): L<<406.0,298.0>--<389.0,169.0>>/L<<389.0,169.0>--<424.0,298.0>> = 7.672580767576534 [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[10] RadioCanada-Regular.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

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

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - grave.cap
 - one.lf
 - hungarumlaut.cap
 - uni030C.alt
 - dotaccent.cap
 - ring.cap
 - caron.cap
 - zero.lf
 - seven.lf
 - five.lf
 - dotbelow
 - two.lf
 - uni20B2.BRACKET.100
 - acute.cap
 - ring_acute.cap
 - dieresis.cap
 - circumflex.cap
 - four.lf
 - uni20A6.BRACKET.100
 - uni0313.short
 - three.lf
 - eight.lf
 - dollar.BRACKET.100
 - six.lf
 - breve.cap
 - tilde.cap
 - caron.alt
 - uni0326
 - cent.BRACKET.100
 - macron.cap
 - uni0326.alt 
 - nine.lf
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

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
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 - Glyph name: Uhorn	Contours detected: 2	Expected: 1
 - Glyph name: Uogonek	Contours detected: 2	Expected: 1
 - Glyph name: aogonek	Contours detected: 3	Expected: 2
 - Glyph name: eogonek	Contours detected: 3	Expected: 2
 - Glyph name: ohorn	Contours detected: 3	Expected: 2
 - Glyph name: uhorn	Contours detected: 2	Expected: 1
 - Glyph name: uni1EDB	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDD	Contours detected: 4	Expected: 3
 - Glyph name: uni1EDF	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE1	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE3	Contours detected: 4	Expected: 3
 - Glyph name: uni1EE8	Contours detected: 3	Expected: 2
 - Glyph name: uni1EE9	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEA	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEB	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEC	Contours detected: 3	Expected: 2
 - Glyph name: uni1EED	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEE	Contours detected: 3	Expected: 2
 - Glyph name: uni1EEF	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF0	Contours detected: 3	Expected: 2
 - Glyph name: uni1EF1	Contours detected: 3	Expected: 2 
 - Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* uni03BC.math (U+00B5): X=213.5,Y=1.0 (should be at baseline 0?)
	* Aring (U+00C5): X=411.0,Y=691.5 (should be at cap-height 690?)
	* Aring (U+00C5): X=245.5,Y=691.5 (should be at cap-height 690?)
	* oe (U+0153): X=722.0,Y=1.5 (should be at baseline 0?)
	* Aringacute (U+01FA): X=411.0,Y=691.5 (should be at cap-height 690?)
	* Aringacute (U+01FA): X=245.5,Y=691.5 (should be at cap-height 690?)
	* uni02B8 (U+02B8): X=11.0,Y=691.0 (should be at cap-height 690?)
	* uni02B8 (U+02B8): X=77.0,Y=691.0 (should be at cap-height 690?)
	* uni02B8 (U+02B8): X=230.0,Y=691.0 (should be at cap-height 690?)
	* uni02B8 (U+02B8): X=294.0,Y=691.0 (should be at cap-height 690?) and 7 more. [code: found-misalignments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.6% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

* ⚠ **WARN** The following glyphs have segments which seem very short:
	* at (U+0040) contains a short segment B<<691.0,451.0>-<687.0,429.0>-<685.5,411.5>>
	* at (U+0040) contains a short segment B<<685.5,411.5>-<684.0,394.0>-<684.0,373.0>>
	* a (U+0061) contains a short segment L<<366.0,308.0>--<366.0,314.0>>
	* ordfeminine (U+00AA) contains a short segment L<<288.0,531.0>--<288.0,535.0>>
	* agrave (U+00E0) contains a short segment L<<366.0,308.0>--<366.0,314.0>>
	* aacute (U+00E1) contains a short segment L<<366.0,308.0>--<366.0,314.0>>
	* acircumflex (U+00E2) contains a short segment L<<366.0,308.0>--<366.0,314.0>>
	* atilde (U+00E3) contains a short segment L<<366.0,308.0>--<366.0,314.0>>
	* adieresis (U+00E4) contains a short segment L<<366.0,308.0>--<366.0,314.0>>
	* aring (U+00E5) contains a short segment L<<366.0,308.0>--<366.0,314.0>> and 37 more. [code: found-short-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* exclam (U+0021): L<<126.0,210.0>--<110.0,515.0>> -> L<<110.0,515.0>--<110.0,690.0>>
	* exclam (U+0021): L<<212.0,690.0>--<212.0,515.0>> -> L<<212.0,515.0>--<196.0,210.0>>
	* exclamdown (U+00A1): L<<110.0,-185.0>--<110.0,0.0>> -> L<<110.0,0.0>--<126.0,305.0>> and exclamdown (U+00A1): L<<196.0,305.0>--<212.0,0.0>> -> L<<212.0,0.0>--<212.0,-185.0>> [code: found-colinear-vectors]

</details>
<br>
</details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 0 | 222 | 2033 | 121 | 1720 | 0 |
| 0% | 0% | 5% | 50% | 3% | 42% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
