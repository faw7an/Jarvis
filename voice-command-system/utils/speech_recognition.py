import speech_recognition as sr

def initialize_recognizer():
    recognizer = sr.Recognizer()
    return recognizer

def listen_for_commands(recognizer):
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for commands...")
        audio = recognizer.listen(source)
    return audio

def recognize_command(recognizer, audio):
    try:
        command = recognizer.recognize_google(audio)
        print(f"Recognized command: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def main():
    recognizer = initialize_recognizer()
    audio = listen_for_commands(recognizer)
    command = recognize_command(recognizer, audio)
    return command

if __name__ == "__main__":
    main()