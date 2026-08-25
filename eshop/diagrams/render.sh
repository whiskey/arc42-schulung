#!/bin/sh
# Rendert alle Diagramme dieses Verzeichnisses neu.
#
#   ./eshop/diagrams/render.sh
#
# Voraussetzung: d2 <https://d2lang.com>, unter macOS  brew install d2

set -eu
cd "$(dirname "$0")"

for f in *.d2; do
  d2 --theme 0 --pad 20 "$f" "${f%.d2}.svg"
done

chmod 644 ./*.svg
echo "Diagramme neu gerendert."
