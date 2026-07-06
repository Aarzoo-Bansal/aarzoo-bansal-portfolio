#!/bin/bash
set -e

# 1. Kill all existing tmux sessions
tmux kill-server 2>/dev/null || true

# 2. cd into the project folder
cd ~/aarzoo-bansal-portfolio

# 3. Get the latest changes from main
git fetch && git reset origin/main --hard

# 4. Enter venv and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# 5. Start a new detached tmux session: cd, activate venv, start Flask
tmux new-session -d -s flask "cd ~/aarzoo-bansal-portfolio && source python3-virtualenv/bin/activate && flask run --host=0.0.0.0"
