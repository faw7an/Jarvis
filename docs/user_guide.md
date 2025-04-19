# User Guide for Voice Command System

## Introduction

The Voice Command System allows users to control their PC using voice commands. This guide provides instructions on how to set up and use the system effectively.

## Setup Instructions

1. **Clone the Repository**
   Open your terminal and run the following command to clone the repository:
   ```
   git clone <repository-url>
   cd voice-command-system
   ```

2. **Install Dependencies**
   Run the installation script to set up the environment:
   ```
   ./install.sh
   ```

3. **Configure Voice Commands**
   Edit the `config/commands.json` file to customize the voice commands and their corresponding actions as needed.

## Usage Instructions

1. **Start the Voice Command System**
   To run the voice command system, execute the startup script:
   ```
   ./scripts/startup.sh
   ```

2. **Voice Commands**
   Ensure your microphone is set up and working properly. You can use the following voice commands to control your PC:
   - "Shut down"
   - "Restart"
   - "Suspend" or "Lock"

## Troubleshooting Tips

- **Microphone Issues**: Ensure your microphone is properly connected and configured in your system settings.
- **Command Recognition**: If the system fails to recognize commands, try speaking clearly and at a moderate pace.
- **Dependencies**: If you encounter issues related to missing libraries, ensure that all dependencies listed in `requirements.txt` are installed correctly.

## Additional Resources

For more detailed information about the project structure and development guidelines, refer to the `docs/developer_guide.md` file.