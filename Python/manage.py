import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(f"Recognized: {said}")  # Print the recognized words
        except Exception:  # Print the exception
            pass
    return said.lower()


def main():
    while True:
        command = listen()
        if 'time' in command:
            speak("The current time is " + datetime.datetime.now().strftime("%H:%M"))
        elif 'search' in command:
            # Extracting the search query from the command
            query = command
            url = f"https://google.com/search?q={query}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {query} on Google')
        elif 'Whatsapp' in command:
            url = "https://web.whatsapp.com"
            webbrowser.get().open(url)
        elif 'stop' in command:
            speak("Goodbye!")
            break
        elif 'google' in command:
            url = "https://google.com"
            webbrowser.get().open(url)
        elif 'Hi' in command:
            url = "https://chat.openai.com"
            webbrowser.get().open(url)
        elif 'youtube' in command:
            url = "https://youtube.com"
            webbrowser.get().open(url)
if __name__ == "__main__":
    main()