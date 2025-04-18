#!/bin/bash

# This script executes system commands based on voice input.
echo "Command executor received: '$1'"
echo "Running command..."

# Check if this is a privileged command that needs sudo
if [[ "$1" == "sudo "* ]]; then
    # Extract the command without sudo
    CMD=${1#sudo }
    
    # For system commands, use pkexec instead which can be configured for passwordless access
    case "$CMD" in
        "shutdown now"|"reboot"|"systemctl suspend")
            echo "Executing privileged command using pkexec: $CMD"
            pkexec $CMD
            ;;
        *)
            # Other sudo commands - try to use sudo with NOPASSWD if configured
            eval "$1" || echo "Command failed with exit code: $?"
            ;;
    esac
else
    # Regular non-privileged command
    eval "$1" || echo "Command failed with exit code: $?"
fi