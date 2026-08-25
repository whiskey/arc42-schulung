# Randbedingungen {#section-architecture-constraints}

* Annahmen
  * Oracle ist im Unternehmen gesetzt und etabliert
    * Kunden- und Bestandsverwaltung
* Technisch
  * Die Oberfläche soll mittels REST/http mit dem Backend kommunizieren.
  * Hardware: Server von Oracle; Datenbanksystem Oracle DB
  * Betriebssystem: Linux 
  * Programmiersprache: 
    * Java 
      * Java Coding Conventions von Sun/Oracle
      * geprüft mit Hilfe von CheckStyle
    * TypeScript für Angular
* Organisatorische
  * Budget: 150k
  * Entwickerkapazität: 3 Devs; 360TP
  * Zeit: 6 Monate
  * Environments? Dev, Test, Prod?
* Rechtlich
  * kein PCI-DSS, wegen Bezahldienstleister!
  * DSGVO
  * Buchhaltung...
