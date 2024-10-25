import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return ""

def main():
    speak("Hello, I am your voice assistant. How can I help you?")
    
    while True:
        command = listen()

        if 'hello' in command:
            speak("Hello! How can I assist you today?")
        elif 'what is your name' in command:
            speak("I am your voice assistant.")
        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break
        else:
            speak("I am not sure how to help with that.")

if __name__ == "__main__":
    main()
