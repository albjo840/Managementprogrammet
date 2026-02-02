#!/bin/bash
# Auto-deploy script för Managementprogrammet
# Körs via cron, kollar efter nya commits och kör git pull

cd /home/albin/managementprogrammet

# Hämta senaste från remote utan att merga
git fetch origin main --quiet

# Kolla om det finns nya commits
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/main)

if [ "$LOCAL" != "$REMOTE" ]; then
    echo "$(date): Nya ändringar hittade, kör git pull..." >> /home/albin/managementprogrammet/deploy.log
    git pull origin main >> /home/albin/managementprogrammet/deploy.log 2>&1
    echo "$(date): Deploy klar!" >> /home/albin/managementprogrammet/deploy.log
fi
