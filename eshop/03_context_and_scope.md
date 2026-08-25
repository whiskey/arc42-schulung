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

### Fachliche Schnittstellen {#_fachliche_schnittstellen}

| Nachbar | Richtung | Fachlicher Inhalt |
|---------|----------|-------------------|
| Kunde | Kunde → eShop | Konfiguration eines Rechners, Bestellung, Zahlungsdaten |
| Kunde | eShop → Kunde | Preis und Machbarkeit der Konfiguration, Bestellbestätigung, Bestellstatus |
| Kundenverwaltung | eShop → Kundenverwaltung | Anlage eines Neukunden, Änderung von Stammdaten |
| Kundenverwaltung | Kundenverwaltung → eShop | Kundenstammdaten zu einer bestehenden Kundennummer |
| Bestandsverwaltung | eShop → Bestandsverwaltung | Anfrage auf Verfügbarkeit, Reservierung der Komponenten einer Bestellung |
| Bestandsverwaltung | Bestandsverwaltung → eShop | Verfügbare Mengen, Bestätigung oder Ablehnung der Reservierung |
| Bezahldienst | eShop → Bezahldienst | Zahlungsauftrag über den Bestellbetrag |
| Bezahldienst | Bezahldienst → eShop | Autorisierung, Ablehnung oder Zeitüberschreitung |

Die Tabelle nennt bewusst nur den fachlichen Inhalt. Über welches Protokoll und
welches Format der Austausch läuft, steht im technischen Kontext — dieselbe
fachliche Schnittstelle kann technisch sehr unterschiedlich umgesetzt sein.

Zwei Punkte sind für den Entwurf wesentlich:

* Die Reservierung in der Bestandsverwaltung und die Autorisierung beim
  Bezahldienst müssen zusammen betrachtet werden. Schlägt die Zahlung fehl,
  darf die Reservierung nicht bestehen bleiben.
* Der Bezahldienst kann mit einer Zeitüberschreitung antworten. Damit ist der
  Ausgang der Zahlung zunächst unbekannt, nicht negativ — der eShop braucht
  dafür einen definierten Zustand.

## Technischer Kontext {#_technischer_kontext}

**\<Diagramm oder Tabelle\>**

**\<optional: Erläuterung der externen technischen Schnittstellen\>**

**\<Mapping fachliche auf technische Schnittstellen\>**
