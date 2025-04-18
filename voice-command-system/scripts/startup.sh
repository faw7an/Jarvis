#!/bin/bash

# Ensure the necessary permissions for the scripts
chmod +x /path/to/voice-command-system/scripts/voice_listener.py
chmod +x /path/to/voice-command-system/scripts/command_executor.sh

# Run the voice listener script in the background
python3 /path/to/voice-command-system/scripts/voice_listener.py &

# Optionally, you can redirect output to a log file
# python3 /path/to/voice-command-system/scripts/voice_listener.py >> /path/to/logfile.log 2>&1 &

# End of startup script