# Managementprogrammet - Teknisk Dokumentation

## PÅMINNELSE TILL ALBIN

När carma1337 har pushat ändringar från Lovable, kör detta på servern:
```bash
cd /home/albin/managementprogrammet && git pull origin main
```

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

---

## DuckDNS

- **Domän:** managementprogrammet.duckdns.org
- **Token:** e76a23ec-3edf-4736-968a-e05913fe2e1e
- **Script:** /home/albin/duckdns/duck.sh (uppdateras var 5:e minut via cron)

---

## TODO

- [x] Lägg till carma1337 som collaborator på GitHub
- [ ] carma1337 accepterar inbjudan
- [ ] carma1337 kopplar Lovable till repot
- [ ] carma1337 bygger hemsidan i Lovable
- [ ] Kör `git pull` på servern för att deploya

---

## Fjärråtkomst

Från annan dator (t.ex. Stockholm):
```bash
ssh -p 2222 albin@managementprogrammet.duckdns.org
cd /home/albin/managementprogrammet
```

---

**Senast uppdaterad:** 2026-02-02
