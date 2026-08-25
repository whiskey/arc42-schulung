# Querschnittliche Konzepte {#section-concepts}

Querschnittliche Konzepte gelten über Bausteingrenzen hinweg. Sie stehen hier und
nicht in der Bausteinsicht, weil sie sonst in jedem Baustein wiederholt — und mit
der Zeit unterschiedlich — beantwortet würden.

Jedes Konzept folgt derselben Gliederung: **Warum** brauchen wir es, **Was** legt
es fest, **Wie** ist es umgesetzt, **Was noch** ist offen oder außerhalb.

## Logging und Tracing {#_logging_und_tracing}

### Warum {#_logging_warum}

Eine Bestellung im eShop berührt vier eigene Bausteine und drei fremde Systeme.
Wenn sie scheitert, ist die erste Frage nie „was ist kaputt", sondern **„wo ist es
passiert"** — in der Bestandsverwaltung, beim Bezahldienst, oder dazwischen. Ohne
durchgehende Nachvollziehbarkeit lässt sich das nach der Tatsache nicht mehr
beantworten.

Drei Punkte aus den vorigen Kapiteln machen das konkret:

* **Der offene Timeout-Fall.** Antwortet der Bezahldienst mit einer
  Zeitüberschreitung, ist der Ausgang der Zahlung *unbekannt* (siehe
  [Kapitel 6](06_runtime_view.md)). Ob der Kunde belastet wurde und ob die
  Reservierung noch steht, muss sich im Nachhinein aus Aufzeichnungen klären
  lassen — sonst bleibt nur, den Kunden zu fragen.
* **10.000 gleichzeitige Benutzer.** In dieser Größenordnung gibt es kein
  Nachstellen im Debugger. Die Aufzeichnung ist das einzige Beweismittel.
* **Drei Entwickler, sechs Monate.** Es ist keine Kapazität da, um Betrieb und
  Fehlersuche später nachzurüsten. Das Konzept muss billig sein und von Anfang an
  mitlaufen.

### Was {#_logging_was}

Zwei Begriffe, die oft vermischt werden:

* **Logging** hält fest, was *ein Baustein* getan hat. Ein Ereignis, ein Zeitpunkt,
  ein Ergebnis.
* **Tracing** hält den Weg *einer fachlichen Anfrage* über Bausteingrenzen hinweg
  zusammen. Ohne Tracing hat man bei 10.000 Benutzern zwar alle Ereignisse, kann
  aber nicht sagen, welche zusammengehören.

Festgelegt wird:

| Was | Festlegung |
|-----|------------|
| Vorgangskennung | Jede Anfrage von außen bekommt am Eintritt ins Backend eine Kennung, die durch alle Bausteine mitläuft und in jedem Log-Eintrag steht |
| Pflichtereignisse | Jeder Zustandsübergang einer Bestellung; jeder Aufruf an ein Nachbarsystem mit Dauer und Ergebnis; jede fachliche Ablehnung; jeder technische Fehler |
| Stufen | `ERROR` nur, wenn ein Mensch handeln muss · `WARN` bei Auffälligkeiten ohne Handlungsbedarf · `INFO` für fachliche Ereignisse · `DEBUG` bleibt der Entwicklung vorbehalten |
| Zeit | UTC, ISO-8601, damit Aufzeichnungen mehrerer Systeme zusammenpassen |
| Sprache | Meldungen auf Englisch, damit sie nicht von der Spracheinstellung abhängen |

**Was nicht protokolliert wird**, ist der wichtigere Teil der Festlegung:

* **Keine Zahlungsdaten.** Kartennummern, Prüfziffern, Gültigkeitsdaten tauchen in
  keiner Aufzeichnung auf — auch nicht gekürzt, auch nicht in `DEBUG`. Das ist
  keine Vorsicht, sondern eine Bedingung des Entwurfs: laut
  [Kapitel 2](02_architecture_constraints.md) unterliegt der eShop **kein**
  PCI-DSS, weil der Bezahldienstleister die Zahlungsdaten hält. Ein einziger
  Log-Eintrag mit einer Kartennummer holt den Standard mit seinem gesamten
  Prüfaufwand ins Haus zurück.
* **Personenbezogene Daten sparsam.** Kundennummer statt Name und Anschrift, sonst
  kollidiert die Aufzeichnung mit der DSGVO-Randbedingung.

### Wie {#_logging_wie}

* **Fassade statt Festlegung.** Im Java-Backend wird gegen SLF4J programmiert, nicht
  gegen eine konkrete Log-Bibliothek. Das ist dieselbe Überlegung wie beim Baustein
  *Integration*: die Entscheidung bleibt austauschbar.
* **Strukturiert, ein Ereignis je Zeile.** JSON statt Fließtext. Fehlersuche über
  10.000 Benutzer ist Filterung, und Filterung braucht Felder.
* **Die Vorgangskennung wandert mit.** Sie entsteht am REST-Eingang, liegt im MDC
  und wird an ausgehende Aufrufe als HTTP-Header weitergereicht. Die Web-UI zeigt
  sie im Fehlerfall an — damit kann ein Kunde beim Support eine Nummer nennen,
  unter der sich der Vorgang wiederfinden lässt.
* **Der Baustein Integration protokolliert den Außenkontakt.** Er ist die einzige
  Stelle mit Verbindung zu Fremdsystemen (siehe [Kapitel 5](05_building_block_view.md)),
  also der natürliche Ort, um Zielsystem, Dauer und Ergebnis jedes Aufrufs
  festzuhalten. Das ist zugleich die Datengrundlage, um die Nachbarsysteme als
  Ursache auszuschließen oder zu benennen.
* **Keine eigene Log-Infrastruktur.** Ausgabe nach `stdout`; das Einsammeln ist
  Sache des Betriebs auf der Linux-Plattform. Ein selbstgebautes Log-System wäre
  bei 360 Personentagen Gesamtaufwand nicht zu rechtfertigen.
* **Das Frontend meldet mit.** Angular schickt Fehler mit derselben
  Vorgangskennung an einen Backend-Endpunkt, sonst endet die Spur an der
  Browsergrenze.

### Was noch {#_logging_was_noch}

Offene Punkte, bewusst als offen dokumentiert:

* **Aufbewahrungsdauer ist nicht entschieden.** Die DSGVO verlangt eine Festlegung;
  sie fehlt und muss mit dem Auftraggeber geklärt werden.
* **Ob ein zentrales Auswertungssystem betrieben wird**, ist eine Betriebs- und
  Budgetentscheidung, keine Entwurfsentscheidung. Das Konzept funktioniert auch
  ohne, nur mühsamer.
* **Die Spur endet an der Unternehmensgrenze.** Ob Kunden- und Bestandsverwaltung
  die Vorgangskennung annehmen und weiterführen, ist ungeklärt — sie sind zwar
  in-house, aber bestehende Systeme. Beim Bezahldienst besteht diese Möglichkeit
  gar nicht; dort bleibt nur, dessen eigene Referenznummer aus der Antwort
  mitzuschreiben und beide Nummern nebeneinanderzulegen.
* **Verwandte Konzepte**, die separat zu beschreiben sind: Fehlerbehandlung
  (was tut ein Baustein, wenn ein Nachbarsystem schweigt) und Sicherheit
  (wer darf Aufzeichnungen lesen — sie enthalten Kundennummern).

## Weitere Konzepte {#_weitere_konzepte}

TODO — Übung: Beschreiben Sie ein zweites querschnittliches Konzept nach derselben
Gliederung. Naheliegend sind *Sicherheit*, *Fehlerbehandlung bei nicht erreichbaren
Nachbarsystemen* und *Lokalisierung* — Letzteres, weil das Qualitätsziel „neue
Sprachversion in unter fünf Tagen" ohne ein tragendes Konzept nicht zu halten ist.
