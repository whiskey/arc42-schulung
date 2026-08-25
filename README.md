# arc42 Schulung

Übungs- und Beispielrepository für die **arc42**-Schulung.

Betrachtungsgegenstand ist der **eShop** — eine Online-Anwendung, mit der Kunden
Computer konfigurieren und bestellen können. Die Architekturdokumentation dazu
entsteht im Lauf der Schulung Kapitel für Kapitel in [`eshop/`](eshop/).

## Aufbau

Ein Markdown-File pro arc42-Kapitel, benannt nach dem offiziellen arc42-Template:

| # | Datei | Kapitel | Status |
|----|-------|---------|--------|
| 1 | `01_introduction_and_goals.md` | Einführung und Ziele | ✅ |
| 2 | `02_architecture_constraints.md` | Randbedingungen | ✅ |
| 3 | `03_system_scope_and_context.md` | Kontextabgrenzung | offen |
| 4 | `04_solution_strategy.md` | Lösungsstrategie | offen |
| 5 | `05_building_block_view.md` | Bausteinsicht | offen |
| 6 | `06_runtime_view.md` | Laufzeitsicht | offen |
| 7 | `07_deployment_view.md` | Verteilungssicht | offen |
| 8 | `08_concepts.md` | Querschnittliche Konzepte | offen |
| 9 | `09_architecture_decisions.md` | Architekturentscheidungen | offen |
| 10 | `10_quality_requirements.md` | Qualitätsanforderungen | offen |
| 11 | `11_technical_risks.md` | Risiken und technische Schulden | offen |
| 12 | `12_glossary.md` | Glossar | offen |

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
* arc42 steht unter [Creative Commons Attribution-ShareAlike 4.0](https://creativecommons.org/licenses/by-sa/4.0/),
  erstellt von Dr. Peter Hruschka und Dr. Gernot Starke.
