#!/bin/bash

# Ensure script execution path
cd "/home/fawzan/Documents/CS PROJECTS/Jarvis/voice-command-system"

# Set DISPLAY for GUI applications if needed
export DISPLAY=:0
export XDG_RUNTIME_DIR=/run/user/$(id -u)

# Ensure the necessary permissions for the scripts
chmod +x scripts/voice_listener.py
chmod +x scripts/command_executor.sh

# Start the voice listener
python3 scripts/voice_listener.py >> /tmp/jarvis_log.txt 2>&1

# End of startup script