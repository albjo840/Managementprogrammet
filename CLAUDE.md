# Managementprogrammet - Teknisk Dokumentation

## WEBHOOK AUTO-DEPLOY (ENGÅNGSSETUP)

För att sidan ska uppdateras automatiskt när carma1337 pushar från Lovable:

### Steg 1: Starta webhook-tjänsten (på servern)
```bash
cd /home/albin/managementprogrammet
git pull origin main
docker compose down
docker compose up -d --build
```

### Steg 2: Lägg till webhook på GitHub
1. Gå till: https://github.com/albjo840/Managementprogrammet/settings/hooks
2. Klicka "Add webhook"
3. Fyll i:
   - **Payload URL:** `http://managementprogrammet.duckdns.org:9000/webhook`
   - **Content type:** `application/json`
   - **Secret:** `managementprogrammet2026`
   - **Events:** Just the push event
4. Klicka "Add webhook"

### Klart!
Nu körs `git pull` automatiskt varje gång någon pushar till GitHub.

---

## Projektöversikt

Hemsida för Managementprogrammet. Tillfälligt projekt under utveckling.

**Skapad:** 2026-01-30
**Status:** Under konstruktion

---

## URLs

- **Live:** http://managementprogrammet.duckdns.org:3081
- **GitHub:** https://github.com/albjo840/Managementprogrammet
- **Lokalt:** http://localhost:3081

---

## Teknisk Stack

- **Webbserver:** Nginx (Docker)
- **Port:** 3081
- **DNS:** DuckDNS (managementprogrammet.duckdns.org)

---

## Projektstruktur

```
managementprogrammet/
├── docker-compose.yml    # Docker-konfiguration
├── public/
│   └── index.html        # Hemsidan
├── webhook/
│   ├── Dockerfile        # Webhook-container
│   └── server.py         # Auto-pull vid push
└── CLAUDE.md             # Detta dokument
```

---

## Kommandon

### Starta
```bash
cd /home/albin/managementprogrammet
docker compose up -d
```

### Stoppa
```bash
docker compose down
```

### Se loggar
```bash
docker compose logs -f
```

### Uppdatera från GitHub
```bash
git pull origin main
```

---

## Deployment

Hemsidan serveras direkt från `public/`-mappen. För att uppdatera:

1. Redigera filer i `public/`
2. Ändringar syns direkt (volymen är monterad)

Eller via GitHub:
1. Pusha ändringar till GitHub
2. På servern: `git pull origin main`

---

## Collaborators

GitHub-repot delas med:
- [x] carma1337 (inbjudan skickad, väntar på acceptans)
- [x] isakmolsson (inbjudan skickad, väntar på acceptans)

---

## DuckDNS

- **Domän:** managementprogrammet.duckdns.org
- **Token:** e76a23ec-3edf-4736-968a-e05913fe2e1e
- **Script:** /home/albin/duckdns/duck.sh (uppdateras var 5:e minut via cron)

---

## TODO

- [x] Lägg till carma1337 som collaborator på GitHub
- [ ] carma1337 accepterar inbjudan
- [ ] Sätt upp webhook (se instruktioner ovan)
- [ ] Lägg till webhook på GitHub
- [ ] carma1337 kopplar Lovable till repot
- [ ] carma1337 bygger hemsidan i Lovable
- [ ] Sidan uppdateras automatiskt via webhook!

---

## Fjärråtkomst

Från annan dator (t.ex. Stockholm):
```bash
ssh -p 2222 albin@managementprogrammet.duckdns.org
cd /home/albin/managementprogrammet
```

---

**Senast uppdaterad:** 2026-02-02
