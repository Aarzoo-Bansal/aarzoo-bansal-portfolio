#!/bin/bash
set -e

# 1. cd into the project folder
cd ~/aarzoo-bansal-portfolio

# 2. Get the latest changes from main
git fetch && git reset origin/main --hard

# 3. Enter venv and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# 4. Restart the myportfolio service
systemctl restart myportfolio

