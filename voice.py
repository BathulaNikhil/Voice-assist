import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
            return None

def respond(text):
    print(f"Responding: {text}")
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    command = listen()
    if command:
        if command.lower() == 'exit':  # Adding a way to exit the loop
            print("Exiting...")
            break
        respond(f"You said: {command}")
