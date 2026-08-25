# arc42 Schulung

Übungs- und Beispielrepository für die **arc42**-Schulung.

Betrachtungsgegenstand ist der **eShop** — eine Online-Anwendung, mit der Kunden
Computer konfigurieren und bestellen können. Die Architekturdokumentation dazu
entsteht im Lauf der Schulung Kapitel für Kapitel in [`eshop/`](eshop/).

## Aufbau

Ein Markdown-File pro arc42-Kapitel, benannt nach dem offiziellen arc42-Template.
„Gerüst" heißt: Überschriften und Platzhalter stehen, der Inhalt wird in der
Schulung erarbeitet.

| # | Datei | Kapitel | Status |
|----|-------|---------|--------|
| 1 | `01_introduction_and_goals.md` | Einführung und Ziele | ✅ |
| 2 | `02_architecture_constraints.md` | Randbedingungen | ✅ |
| 3 | `03_context_and_scope.md` | Kontextabgrenzung | teilweise |
| 4 | `04_solution_strategy.md` | Lösungsstrategie | Gerüst |
| 5 | `05_building_block_view.md` | Bausteinsicht | teilweise |
| 6 | `06_runtime_view.md` | Laufzeitsicht | teilweise |
| 7 | `07_deployment_view.md` | Verteilungssicht | Gerüst |
| 8 | `08_concepts.md` | Querschnittliche Konzepte | teilweise |
| 9 | `09_architecture_decisions.md` | Architekturentscheidungen | teilweise |
| 10 | `10_quality_requirements.md` | Qualitätsanforderungen | Gerüst |
| 11 | `11_technical_risks.md` | Risiken und technische Schulden | Gerüst |
| 12 | `12_glossary.md` | Glossar | fertig |

## Die Doku als eine Seite

**→ <https://whiskey.github.io/arc42-schulung/>**

[`docs/index.html`](docs/index.html) fasst alle zwölf Kapitel zu einer eigenständigen
HTML-Seite zusammen: Inhaltsverzeichnis, eingebettete Diagramme, und sichtbar
gemacht, was noch Template und was schon Inhalt ist. GitHub Pages veröffentlicht die
Datei aus dem Ordner `docs/`; sie lässt sich genauso gut lokal im Browser öffnen, ein
Webserver ist nicht nötig.

Nach Änderungen an den Kapiteln neu erzeugen:

```sh
python3 docs/build.py      # braucht pandoc
./eshop/diagrams/render.sh # nur nötig, wenn ein Diagramm geändert wurde; braucht d2
```

Den Bearbeitungsstand je Kapitel pflegt `STATUS` in [`docs/build.py`](docs/build.py) —
dieselben Angaben wie in der Tabelle oben. Das Datum in der Kopfzeile kommt aus dem
letzten Commit und muss nicht gepflegt werden.

## Arbeitsweise

* Dokumentation ist Teil des Repos — *docs as code*: Änderungen laufen über
  Commits, nicht über Dateianhänge.
* Ein Kapitel pro Datei, damit mehrere Gruppen parallel arbeiten können, ohne
  sich gegenseitig Merge-Konflikte zu bauen.
* Offene Punkte und bewusste Lücken direkt im Text markieren (`TODO:`), statt sie
  wegzulassen — arc42 dokumentiert auch, was noch nicht entschieden ist.

## Über arc42

arc42 ist ein Template zur Dokumentation von Software- und Systemarchitekturen:
zwölf Kapitel, die die typischen Fragen an eine Architektur strukturieren.

* Website: <https://arc42.org>
* Template-Downloads: <https://arc42.org/download>

## Lizenz

Die Inhalte dieses Repositories stehen unter
[Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)
(CC BY-SA 4.0) — siehe [LICENSE](LICENSE).

© 2026 Carsten Knoblich

Das zugrunde liegende arc42-Template stammt von Dr. Peter Hruschka und
Dr. Gernot Starke und steht ebenfalls unter CC BY-SA 4.0. Diese
Dokumentation ist eine davon abgeleitete Bearbeitung und wird daher unter
derselben Lizenz weitergegeben.
