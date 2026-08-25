#!/usr/bin/env python3
"""Erzeugt docs/index.html aus den arc42-Kapiteln in eshop/.

    python3 docs/build.py

Voraussetzung: pandoc <https://pandoc.org>, unter macOS  brew install pandoc

Die Diagramme werden als Data-URI eingebettet, damit die Seite eine einzelne,
eigenstaendige Datei bleibt und auch ohne Webserver funktioniert.
"""

import base64
import json
import pathlib
import re
import subprocess
import sys

HIER = pathlib.Path(__file__).resolve().parent
REPO = HIER.parent
ESHOP = REPO / "eshop"
ZIEL = HIER / "index.html"
GH = "https://github.com/whiskey/arc42-schulung/blob/main/eshop/"

# Bearbeitungsstand je Kapitel. Beim Ausfuellen eines Kapitels hier mitpflegen.
STATUS = {1: "fertig", 2: "fertig", 3: "teilweise", 4: "Gerüst",
          5: "teilweise", 6: "teilweise", 7: "Gerüst", 8: "Gerüst",
          9: "Gerüst", 10: "Gerüst", 11: "Gerüst", 12: "Gerüst"}

KLASSE = {"fertig": "fertig", "teilweise": "teilweise", "Gerüst": "geruest"}


def datauri(pfad):
    return "data:image/svg+xml;base64," + base64.b64encode(pfad.read_bytes()).decode()


def stand():
    """Datum des letzten Commits, damit der Stand nicht von Hand gepflegt wird."""
    try:
        iso = subprocess.run(["git", "-C", str(REPO), "log", "-1", "--format=%cs"],
                             capture_output=True, text=True, check=True).stdout.strip()
        j, m, t = iso.split("-")
        return f"{t}.{m}.{j}"
    except Exception:
        return "ohne Angabe"


def kapitel():
    dateien = sorted(ESHOP.glob("[0-9][0-9]_*.md"))
    if len(dateien) != 12:
        raise SystemExit(f"12 Kapitel erwartet, {len(dateien)} gefunden")

    out = []
    for datei in dateien:
        nr = int(datei.name[:2])
        frag = subprocess.run(
            ["pandoc", "-f", "markdown-smart", "-t", "html5", "--wrap=none",
             "--shift-heading-level-by=1", str(datei)],
            capture_output=True, text=True, check=True).stdout

        titel = re.search(r"<h2[^>]*>(.*?)</h2>", frag, re.S).group(1).strip()
        frag = re.sub(r"<h2[^>]*>.*?</h2>", "", frag, count=1, flags=re.S)

        def bild(m):
            src, alt = m.group("src"), m.group("alt")
            pfad = ESHOP / src
            if not pfad.exists():
                return m.group(0)
            return f'<img class="diagramm" src="{datauri(pfad)}" alt="{alt}">'

        frag = re.sub(r'<img src="(?P<src>[^"]+)" alt="(?P<alt>[^"]*)"\s*/?>', bild, frag)
        frag = re.sub(r"<figcaption[^>]*>.*?</figcaption>", "", frag, flags=re.S)

        def link(m):
            href = m.group(1)
            if href.startswith(("http://", "https://", "#")):
                return m.group(0)
            treffer = re.match(r"(\d\d)_[a-z_]+\.md$", href)
            if treffer:
                return f'<a href="#kapitel-{treffer.group(1)}">'
            return f'<a href="{GH}{href}" target="_blank" rel="noopener">'

        frag = re.sub(r'<a href="([^"]+)">', link, frag)
        frag = re.sub(r"<p>TODO — Übung:\s*(.*?)</p>",
                      r'<aside class="uebung"><span class="uebung-marke">Übung</span>'
                      r"<p>\1</p></aside>", frag, flags=re.S)
        frag = re.sub(r"<(strong|em)>(&lt;[^<]*?&gt;)</\1>",
                      r'<span class="platzhalter">\2</span>', frag)
        frag = re.sub(r'<em><span class="platzhalter">(.*?)</span></em>',
                      r'<span class="platzhalter">\1</span>', frag)

        frag = frag.replace("<figure>", '<figure><div class="diagramm-rahmen">')
        frag = frag.replace("</figure>", "</div></figure>")
        frag = frag.replace("<table>", '<div class="tabellenrahmen"><table>')
        frag = frag.replace("</table>", "</table></div>")

        out.append({"nr": nr, "titel": titel, "frag": frag, "status": STATUS[nr]})
    return out


def main():
    kap = kapitel()
    fertig = sum(1 for k in kap if k["status"] == "fertig")
    begonnen = sum(1 for k in kap if k["status"] == "teilweise")

    toc, abschnitte = [], []
    for k in kap:
        nr = f"{k['nr']:02d}"
        kl = KLASSE[k["status"]]
        toc.append(f'<li><a href="#kapitel-{nr}"><span class="nr">{nr}</span>'
                   f'<span>{k["titel"]}'
                   f'<span class="toc-punkt {kl}" aria-hidden="true"></span></span></a></li>')
        abschnitte.append(f"""<section class="kapitel" id="kapitel-{nr}">
  <div class="kapitel-kopf">
    <span class="kapitel-nr">Kapitel {nr}</span>
    <span class="chip {kl}">{k["status"]}</span>
  </div>
  <h2>{k["titel"]}</h2>
  <div class="inhalt">{k["frag"]}</div>
</section>""")

    vorlage = (HIER / "seite.template.html").read_text(encoding="utf-8")
    seite = (vorlage
             .replace("{{STAND}}", stand())
             .replace("{{FORTSCHRITT}}", f"{fertig} von 12 Kapiteln fertig, {begonnen} begonnen")
             .replace("{{TOC}}", "".join(toc))
             .replace("{{KAPITEL}}", "".join(abschnitte)))

    # Die Vorlage trennt Kopf- von Koerperteil, damit aus derselben Quelle beides
    # entstehen kann: ein vollstaendiges HTML-Dokument fuer das Repo und GitHub
    # Pages, und ein Rumpf ohne <html>/<head> fuer Umgebungen, die selbst umhuellen.
    kopf, koerper = seite.split("<!-- KOPF-ENDE -->", 1)
    dokument = ("<!doctype html>\n<html lang=\"de\">\n<head>\n"
                "<meta charset=\"utf-8\">\n"
                "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
                + kopf.strip() + "\n</head>\n<body>\n"
                + koerper.strip() + "\n</body>\n</html>\n")

    ZIEL.write_text(dokument, encoding="utf-8")
    print(f"{ZIEL.relative_to(REPO)} geschrieben, {round(len(dokument.encode()) / 1024)} KiB")

    if len(sys.argv) > 2 and sys.argv[1] == "--rumpf":
        rumpf = pathlib.Path(sys.argv[2])
        rumpf.write_text(seite.replace("<!-- KOPF-ENDE -->\n", ""), encoding="utf-8")
        print(f"{rumpf} geschrieben (Rumpf ohne <html>/<head>)")


if __name__ == "__main__":
    main()
