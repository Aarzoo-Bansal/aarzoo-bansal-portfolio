#!/bin/bash
set -e

# 1. cd into the project folder
cd ~/aarzoo-bansal-portfolio

# 2. Get the latest changes from main
git fetch && git reset origin/main --hard

# 3. Remove the existing containers to avoid out of memory issue
docker compose -f docker-compose.prod.yml down

# 4. Spin up new containers
docker compose -f docker-compose.prod.yml up -d --build