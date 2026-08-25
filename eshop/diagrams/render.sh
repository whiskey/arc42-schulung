#!/bin/sh
# Rendert alle Diagramme dieses Verzeichnisses neu.
#
#   ./eshop/diagrams/render.sh
#
# Voraussetzung: d2 <https://d2lang.com>, unter macOS  brew install d2

set -eu
cd "$(dirname "$0")"

OPTS="--theme 0 --pad 20"

# Strukturdiagramme: eine Quelle, ein SVG.
for f in 03-kontext 05-bausteinsicht; do
  d2 $OPTS "$f.d2" "$f.svg"
done

# Laufzeitszenarien: die Quellen sind in Schritte (steps) zerlegt.
#
#   mit --animate-interval  -> eine animierte Fassung, die den Ablauf aufbaut
#   ohne --animate-interval -> ein Verzeichnis mit einem SVG je Schritt; das
#                              letzte davon zeigt den vollstaendigen Ablauf und
#                              wird als Standbild uebernommen
for f in 06-laufzeit-konfiguration 06-laufzeit-bestellung; do
  d2 $OPTS --animate-interval 1600 "$f.d2" "$f-animiert.svg"

  tmp=$(mktemp -d)
  d2 $OPTS "$f.d2" "$tmp/board.svg" >/dev/null
  last=$(ls "$tmp/board" | grep -v '^index\.svg$' | sort | tail -1)
  cp "$tmp/board/$last" "$f.svg"
  rm -rf "$tmp"
done

chmod 644 ./*.svg
echo "Diagramme neu gerendert."
