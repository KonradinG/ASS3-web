# Flask + MySQL Webapp

## Starten (lokal mit Docker Compose)
```bash
docker-compose up --build
```

## API-Endpunkte

- `GET /data` – Alle gespeicherten Einträge abrufen
- `POST /data` – Neuen Eintrag speichern (`{ "name": "Beispiel" }`)

## Eigene Anpassungen

- 📦 Webcode: `web/app.py`
- 🐬 Datenbankstruktur: `db/init.sql`
- 🐙 GitHub Actions: `.github/workflows/build.yml` – ersetzt `web` ggf. durch eigenen Namen