# !/bin/bash

set -e

fontmake \
    -m sources/Radio-Canada.designspace \
    -o variable \
    --no-production-names \
    --output-path fonts/variable/Radio-Canada-Test-Build.ttf
#    --verbose DEBUG 

echo "\n**** Done ****\n"
