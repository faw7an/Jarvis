# Voice Command System

This project allows users to control their PC using voice commands. It provides functionalities to shut down, restart, or suspend/lock the computer through simple voice interactions.

## Project Structure

```
voice-command-system
├── scripts
│   ├── voice_listener.py       # Captures audio input and recognizes voice commands
│   ├── command_executor.sh      # Executes system commands based on recognized voice commands
│   └── startup.sh               # Sets up the environment and runs the voice_listener.py script on startup
├── config
│   └── commands.json            # Stores voice commands and their corresponding actions
├── utils
│   ├── speech_recognition.py    # Contains functions for speech recognition
│   └── system_actions.py        # Defines functions for executing system-level actions
├── requirements.txt             # Lists Python dependencies required for the project
├── install.sh                   # Automates the installation of dependencies and project setup
└── README.md                    # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd voice-command-system
   ```

2. Run the installation script to set up the environment:
   ```
   ./install.sh
   ```

3. Configure the voice commands in `config/commands.json` as needed.

4. To run the voice command system, execute the startup script:
   ```
   ./scripts/startup.sh
   ```

## Usage Guidelines

- Ensure your microphone is set up and working properly.
- Use the following voice commands to control your PC:
  - "Shut down"
  - "Restart"
  - "Suspend" or "Lock"

## Script Descriptions

- **voice_listener.py**: Listens for voice commands and converts them to text.
- **command_executor.sh**: Executes the appropriate system command based on the recognized voice command.
- **startup.sh**: Initializes the environment and starts the voice listener on system startup.
- **commands.json**: Defines the voice commands and their corresponding actions.
- **speech_recognition.py**: Contains the logic for processing audio input and recognizing speech.
- **system_actions.py**: Provides functions for performing system-level actions like shutdown and restart.

## Dependencies

Make sure to install the required dependencies listed in `requirements.txt` to ensure the project functions correctly.