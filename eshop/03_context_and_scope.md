# Kontextabgrenzung {#section-context-and-scope}

## Fachlicher Kontext {#_fachlicher_kontext}

### Kontextdiagramm {#_kontextdiagramm}

![Fachlicher Kontext des eShop: der Kunde bestellt beim eShop; der eShop nutzt die
In-house-Systeme Kundenverwaltung und Bestandsverwaltung und den externen Bezahldienst](diagrams/03-kontext.svg)

Der eShop ist das betrachtete System. Die Nachbarn zerfallen in zwei Gruppen,
und diese Trennung ist der eigentliche Punkt des Diagramms:

* **Kundenverwaltung und Bestandsverwaltung** (blauer Rahmen) gehören
  Sell-PC-Solutions selbst. Sie stammen aus dem Offline-Geschäft, laufen dort
  weiter und werden vom eShop mitbenutzt. Sie sind grundsätzlich änderbar — aber
  jede Änderung trifft auch das Offline-Geschäft, das an denselben Systemen hängt.
* **Der Bezahldienst** (gestrichelt) ist zugekauft. Seine Schnittstelle, sein
  Verhalten und seine Verfügbarkeit sind vorgegeben; der eShop muss sich daran
  anpassen und mit Ausfällen umgehen können.

Quelle des Diagramms: [`diagrams/03-kontext.d2`](diagrams/03-kontext.d2)
([D2](https://d2lang.com)). Nach einer Änderung neu rendern mit:

```sh
d2 --theme 0 --pad 20 eshop/diagrams/03-kontext.d2 eshop/diagrams/03-kontext.svg
```

**\<optional: Erläuterung der externen fachlichen Schnittstellen\>**

## Technischer Kontext {#_technischer_kontext}

**\<Diagramm oder Tabelle\>**

**\<optional: Erläuterung der externen technischen Schnittstellen\>**

**\<Mapping fachliche auf technische Schnittstellen\>**
