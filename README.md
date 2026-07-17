# TikTok-Video-Downloader
Ein kleines Skript von mir, um Videos von TikTok runterzuladen.

----------------------------------
Wenn man die beiden dateien in einen Ordner macht sollte man einen venv-Ordner anlegen.

Warum der venv-Ordner?
Ich hab das Skript in eine Virtual Environment (venv) gepackt, weil mein Mac nach der Installation von anderer Software (Odysseus) mit den globalen Python-Bibliotheken rumgezickt hat. So ist alles sauber isoliert und das Skript läuft stabil, egal was ich sonst noch auf dem Rechner installiert habe.

----------------------------------
Einrichtung
Im Terminal einfach in den Ordner navigieren und das hier ausführen:

Virtual Environment erstellen:
`python3 -m venv venv`

Aktivieren:
`source venv/bin/activate`

Bibliotheken installieren:
`pip install requests`

----------------------------------
Starten
Das Skript läuft am einfachsten über die start.command Datei.
Falls es sich nicht öffnen lässt, einmal kurz im Terminal ausführbar machen:
`chmod +x start.command`
