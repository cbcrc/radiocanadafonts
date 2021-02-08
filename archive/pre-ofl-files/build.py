from fontmake.font_project import FontProject
import os

SRC_DIR = "src"

romans = [
	os.path.join(SRC_DIR, "Radio-Canada-Light.ufo"),
	os.path.join(SRC_DIR, "Radio-Canada-Regular.ufo"),
	os.path.join(SRC_DIR, "Radio-Canada-Medium.ufo"),
	os.path.join(SRC_DIR, "Radio-Canada-Bold.ufo"),
	os.path.join(SRC_DIR, "Radio-Canada-Condensed-Regular.ufo"),
	os.path.join(SRC_DIR, "Radio-Canada-Condensed-Bold.ufo"),
]
italics = [
	os.path.join(SRC_DIR, "Radio-Canada-LightItalic.ufo"),
	os.path.join(SRC_DIR, "Radio-Canada-Italic.ufo"),
	os.path.join(SRC_DIR, "Radio-Canada-MediumItalic.ufo"),
	os.path.join(SRC_DIR, "Radio-Canada-BoldItalic.ufo"),
	os.path.join(SRC_DIR, "Radio-Canada-Condensed-Italic.ufo"),
	os.path.join(SRC_DIR, "Radio-Canada-Condensed-BoldItalic.ufo"),
]

for ufos in [romans, italics]:
	project = FontProject()
	project.run_from_ufos(ufos, output=("otf", "ttf", "ttf-interpolatable"), use_production_names=False, feature_writers=[])
