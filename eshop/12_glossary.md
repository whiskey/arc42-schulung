# Glossar {#section-glossary}

Zweck dieses Kapitels ist, dass alle Beteiligten dasselbe meinen. Aufgenommen wird
ein Begriff dann, wenn er im Projekt anders benutzt wird als umgangssprachlich,
oder wenn er doppelt belegt ist.

## Fachbegriffe {#_fachbegriffe}

| Begriff | Bedeutung |
|---------|-----------|
| Autorisierung | Zusage des Bezahldienstes, dass der Betrag gedeckt ist und eingezogen werden kann. Nicht zu verwechseln mit der Buchung, die später erfolgt. |
| Bestandsverwaltung | Bestehendes In-house-System, das die verfügbaren Mengen aller Komponenten führt. Wird vom Offline-Geschäft mitbenutzt. |
| Bestellung | **Doppelt belegt.** Fachlich der Vorgang, mit dem ein Kunde eine Konfiguration verbindlich bestellt. Zugleich der Name eines Bausteins in [Kapitel 5](05_building_block_view.md). Im Text kursiv gesetzt, wenn der Baustein gemeint ist. |
| Bezahldienst | Zugekaufter externer Dienstleister, der die Zahlung abwickelt und die Zahlungsdaten hält. Kreditkarte, PayPal und Vergleichbares. |
| Komponente | **Doppelt belegt.** Fachlich ein Einzelteil eines Rechners, also Prozessor, Speicher, Netzteil. In UML-Diagrammen dagegen ein Baustein der Software. Im Zweifel steht im Text, welche Lesart gilt. |
| Konfiguration | Zusammenstellung von Komponenten zu einem lieferbaren Rechner. Eine Konfiguration ist entweder gültig oder nicht — Teilzustände gibt es nicht. |
| Kundenverwaltung | Bestehendes In-house-System mit den Kundenstammdaten. Wird vom Offline-Geschäft mitbenutzt. |
| Reservierung | Vormerkung von Komponenten in der Bestandsverwaltung für eine noch nicht abgeschlossene Bestellung. Siehe [ADR-01](09_architecture_decisions.md). |
| Sell-PC-Solutions GmbH | Der Auftraggeber. Computerhersteller, betreibt bisher nur das Offline-Geschäft. |
| Vorgangskennung | Kennung, die eine Anfrage durch alle Bausteine begleitet und in jedem Log-Eintrag steht. Siehe [Kapitel 8](08_concepts.md). |
| eShop | Das zu bauende System. Kleines „e", großes „S" — auch am Satzanfang. |

## Begriffe der Dokumentation {#_begriffe_der_dokumentation}

| Begriff | Bedeutung |
|---------|-----------|
| ADR | *Architecture Decision Record.* Eine festgehaltene Architekturentscheidung mit Kontext, Begründung und verworfenen Alternativen. Siehe [Kapitel 9](09_architecture_decisions.md). |
| Baustein | Abgegrenzter Teil des Systems mit eigener Verantwortung. Der Begriff sagt nichts über die technische Umsetzung — ein Baustein ist nicht zwingend ein eigener Prozess oder ein eigenes Deployment. |
| Blackbox | Beschreibung eines Bausteins von außen: was er leistet und über welche Schnittstellen, nicht wie er innen aufgebaut ist. |
| Nachbarsystem | System außerhalb des eShops, mit dem er fachlich austauscht. Siehe [Kapitel 3](03_context_and_scope.md). |
| Qualitätsszenario | Anforderung an eine Qualität, formuliert als konkreter Ablauf mit messbarer Reaktion — statt „das System soll schnell sein". |
| Stakeholder | Person oder Rolle mit berechtigtem Interesse an der Architektur. Siehe [Kapitel 1](01_introduction_and_goals.md). |
| Whitebox | Beschreibung eines Bausteins von innen: aus welchen Bausteinen er besteht und wie diese zusammenwirken. |
