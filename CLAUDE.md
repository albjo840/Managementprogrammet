# Managementprogrammet - Teknisk Dokumentation

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
├── deploy.sh             # Auto-deploy script (cron)
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

**Automatisk deploy är aktiverad!**

När någon pushar till GitHub körs `git pull` automatiskt på servern (varje minut via cron).

### Manuellt (vid behov)
```bash
cd /home/albin/managementprogrammet
git pull origin main
```

### Kolla deploy-logg
```bash
cat /home/albin/managementprogrammet/deploy.log
```

### Cron-jobb
```
* * * * * /home/albin/managementprogrammet/deploy.sh
```

---

## Collaborators

GitHub-repot delas med:
- [x] Jonas (@carma1337) - inbjuden

---

## DuckDNS

- **Domän:** managementprogrammet.duckdns.org
- **Token:** e76a23ec-3edf-4736-968a-e05913fe2e1e
- **Script:** /home/albin/duckdns/duck.sh (uppdateras var 5:e minut via cron)

---

## TODO

- [x] Lägg till Jonas som collaborator på GitHub
- [ ] Jonas bygger hemsidan i Lovable
- [ ] Deploya färdig hemsida

---

## Fjärråtkomst

Från annan dator (t.ex. Stockholm):
```bash
ssh -p 2222 albin@managementprogrammet.duckdns.org
cd /home/albin/managementprogrammet
```

---

**Senast uppdaterad:** 2026-01-30
