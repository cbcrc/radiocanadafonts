# Radio-Canada Typeface

![Nameplate image](documentation/images/nameplate.png)
CBC/Radio-Canada is a Canadian Crown corporation serving as the national public radio and television broadcaster. The English- and French-language service units of the corporation are commonly known as CBC and Radio-Canada, respectively. 

In early 2017, work started on a custom typeface for use by CBC/Radio-Canada. In 2021, this typeface was expanded to cover a wider range of weights and now includes roman and italic variable fonts, and in early 2023, the family was extended to include the [Unified Canadian Aboriginal Syllabics](https://en.wikipedia.org/wiki/Canadian_Aboriginal_syllabics) Unicode block.

This project has been selected as a winner at the 2018 Communication Arts Typography competition in the Typeface Design category.

The latest release is [available on Google Fonts](https://fonts.google.com/specimen/Radio+Canada).

## Variable Font Axes

Radio-canada has the following axes:

Axis | Tag | Range | Default | Static Instances
--- | --- | --- | --- | ---
Weight | wght | 300 to 700 | 400 | Light, Regular, Medium, Semibold, Bold
Width | wdth | 75 to 100 | 100 | Condensed, SemiCondensed, Regular

#### `wght` (Weight) Axis

The `wght` axis spans Light (300) to Bold (700).

![Weight axis example animation](documentation/images/weight-axis-example.gif)
![Weight axis italic example animation](documentation/images/weight-axis-example-italic.gif)

#### `wdth` (Width) Axis

The `wdth` axis spans Condensed (75) to Regular (700).

![Width axis example animation](documentation/images/width-axis-example.gif)
![Width axis italic example animation](documentation/images/width-axis-example-italic.gif)

## Building

Fonts are built automatically by GitHub Actions - take a look in the "Actions" tab for the latest build.

If you want to build fonts manually on your own computer, you will need to install the [`yq` utility](https://github.com/mikefarah/yq). On OS X with Homebrew, type `brew install yq`; on Linux, try `snap install yq`; if all else fails, try the instructions on the linked page.

Then:

* `make build` will produce font files.
* `make test` will run [FontBakery](https://github.com/googlefonts/fontbakery)'s quality assurance tests.
* `make proof` will generate HTML proof files.

## License

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at [http://scripts.sil.org/OFL](http://scripts.sil.org/OFL)

## Repository Layout

This font repository structure is inspired by [Unified Font Repository v0.3](https://github.com/unified-font-repository/Unified-Font-Repository), modified for the [Google Fonts workflow](https://github.com/googlefonts/Unified-Font-Repository).
