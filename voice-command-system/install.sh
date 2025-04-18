#!/bin/bash

# Update package list and install required packages
sudo apt update
sudo apt install -y python3 python3-pip

# Install Python dependencies
pip3 install -r requirements.txt

# Set permissions for scripts
chmod +x scripts/*.sh
chmod +x scripts/voice_listener.py

echo "Installation complete. You can now run the voice command system."