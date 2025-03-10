#!/bin/bash

# Uninstall previous dependencies 
pip uninstall py-cord
pip uninstall discord.py

# Install dependencies
pip install -r requirements.txt

# Start the bot
python3 mockbot.py