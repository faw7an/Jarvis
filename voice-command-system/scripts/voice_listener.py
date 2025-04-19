import speech_recognition as sr
import subprocess
import json
import os
import sys

def load_commands():
    with open(os.path.join(os.path.dirname(__file__), '../config/commands.json')) as f:
        return json.load(f)

def recognize_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for wake word 'Jarvis'...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Heard: {command}")
        
        # Check if wake word "Jarvis" is in the command
        if "jarvis" in command:
            print("Wake word detected! Listening for command...")
            # Listen for the actual command
            with sr.Microphone() as command_source:
                recognizer.adjust_for_ambient_noise(command_source, duration=0.5)
                audio = recognizer.listen(command_source)
            
            try:
                command = recognizer.recognize_google(audio).lower()
                print(f"Recognized command: {command}")
                return command
            except sr.UnknownValueError:
                print("Could not understand command")
                return None
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return None
        else:
            print("Wake word not detected")
            return None
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def execute_command(command):
    # Debug output of the text command
    print(f"Debug - Text command received: '{command}'")
    
    commands = load_commands()
    if isinstance(commands, dict):
        command_dict = commands.get('commands', {})  # Get the commands dictionary
        for cmd_key, cmd_value in command_dict.items():
            if cmd_value.get('phrase', '') in command:
                action = cmd_value['action']
                print(f"Executing command: {action}")
                
                # Use direct command without sudo prefix - our command_executor.sh will handle privileges
                subprocess.call(['bash', os.path.join(os.path.dirname(__file__), 'command_executor.sh'), action])
                return
    print("No valid command recognized.")

if __name__ == "__main__":
    # Check if a command line argument was provided for testing
    if len(sys.argv) > 1 and sys.argv[1] == "--text-input":
        while True:
            print("\nEnter a command (or 'exit' to quit):")
            text_command = input("> ").lower()
            if text_command == "exit":
                break
            execute_command(text_command)
    else:
        # Normal voice recognition mode with wake word detection
        print("Voice Command System started")
        print("Say 'Jarvis' followed by your command...")
        while True:
            voice_command = recognize_voice_command()
            if voice_command:
                execute_command(voice_command)