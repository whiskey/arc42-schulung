# Architekturentscheidungen {#section-design-decisions}

Hier stehen die Entscheidungen, deren **Begründung** man später nicht mehr
rekonstruieren kann. Nicht jede Festlegung gehört dazu: Was aus einer
Randbedingung folgt, ist keine Entscheidung, sondern eine Vorgabe — die steht in
[Kapitel 2](02_architecture_constraints.md).

Der Prüfstein ist einfach: Gab es eine ernstzunehmende Alternative, und würde
jemand in einem Jahr fragen „warum eigentlich so"? Dann hierher.

## Übersicht {#_uebersicht}

| Nr. | Entscheidung | Status | Betrifft |
|-----|--------------|--------|----------|
| [ADR-01](#_adr_01_reservierung_vor_zahlung) | Reservierung vor Zahlung | entschieden | Bestellung, Integration |
| ADR-02 | Integration als ein Baustein statt Adapter je Fachbaustein | entschieden | [Kapitel 5](05_building_block_view.md) |
| ADR-03 | Keine Zahlungsdaten im eShop, um PCI-DSS zu vermeiden | entschieden | [Kapitel 8](08_concepts.md) |
| ADR-04 | Verhalten bei Zeitüberschreitung des Bezahldienstes | **offen** | [Kapitel 6](06_runtime_view.md), [Kapitel 11](11_technical_risks.md) |
| ADR-05 | Zwischenspeicherung der Verfügbarkeitsabfrage | **offen** | Konfigurator, Integration |

Ausgearbeitet ist bisher nur ADR-01 — als Muster für die übrigen.

## ADR-01: Reservierung vor Zahlung {#_adr_01_reservierung_vor_zahlung}

**Status:** entschieden

### Kontext

Beim Bestellabschluss müssen zwei Dinge gelingen: Die Komponenten müssen in der
Bestandsverwaltung reserviert und der Betrag beim Bezahldienst autorisiert werden.
Beide Systeme sind eigenständig, wissen nichts voneinander und bieten keine
gemeinsame Transaktion. Eines von beidem muss zuerst geschehen.

### Entscheidung

Zuerst wird reserviert, danach bezahlt. Schlägt die Zahlung fehl, gibt der
Baustein *Bestellung* die Reservierung wieder frei.

### Begründung

Die umgekehrte Reihenfolge — erst kassieren, dann reservieren — kann dazu führen,
dass ein Kunde für etwas bezahlt hat, das nicht mehr lieferbar ist. Das ist
fachlich der schlechtere Fehlerfall: Geld zurückzugeben ist teurer, langsamer und
für den Kunden ärgerlicher als eine Bestellung, die vor der Zahlung abbricht.

### Konsequenzen

* Der Baustein *Bestellung* trägt die Klammer um beide Schritte, einschließlich
  der Rücknahme. Diese Verantwortung ist nicht delegierbar und begründet, warum
  *Bestellung* einen eigenen Zustand je Vorgang führt.
* Reservierungen können verwaisen, wenn die Rücknahme selbst scheitert. Es braucht
  eine Verfallszeit auf Seiten der Bestandsverwaltung — deren Zusage steht noch aus.
* Bei sehr knappem Bestand kann eine Reservierung einen anderen Kunden blockieren,
  dessen Zahlung durchgegangen wäre. Das wird in Kauf genommen.

### Alternativen

* **Erst Zahlung, dann Reservierung** — verworfen, siehe Begründung.
* **Beides parallel** — verworfen: verkürzt den Ablauf um wenige hundert
  Millisekunden und verdoppelt die Zahl der Fehlerkombinationen.
* **Verteilte Transaktion über beide Systeme** — nicht möglich, der Bezahldienst
  bietet keine.

## Weitere Entscheidungen {#_weitere_entscheidungen}

TODO — Übung: Arbeiten Sie ADR-02 und ADR-03 nach demselben Muster aus, und
entscheiden Sie ADR-04. Achten Sie darauf, welche Annahmen Sie dabei treffen —
eine Entscheidung ohne benannte Annahme lässt sich später nicht überprüfen.
