import subprocess as sp
import datetime
import webbrowser

def main():
    while True:
        name = input("Enter your command: ").lower()
        if name == "time":
            print("The current time is " + datetime.datetime.now().strftime("%H:%M"))
        elif name == "search":
            query = input("Enter search query: ")
            url = f"https://google.com/search?q={query}"
            webbrowser.get().open(url)
            print(f'Here is what I found for {query} on Google')
        elif name == "whatsapp":
            sp.Popen(['start', 'https://web.whatsapp.com'], shell=True)
        elif name == "google":
            sp.Popen(['start', 'https://google.com'], shell=True)
        elif name == "hi":
            sp.Popen(['start', 'https://chat.openai.com'], shell=True)
        elif name == "youtube":
            sp.Popen(['start', 'https://youtube.com'], shell=True)
        elif name == "teams":
            teams_path = r'"C:\Users\user\AppData\Local\Microsoft\Teams\current\teams.exe"'
            sp.Popen(teams_path, shell=True)
        elif name == "stop":
            print("Goodbye!")
            break
        elif name == "notepad":
            sp.Popen(['start', 'notepad.exe'], shell=True)
        elif name == "calculator":
            sp.Popen(['start', 'calc.exe'], shell=True)
        elif name == "camera":
            sp.Popen(['start', 'microsoft.windows.camera:'], shell=True)
        elif name == "vscode":
            sp.Popen(['start', 'code'], shell=True)
        elif name == "git":
            webbrowser.get().open("https://github.com")

if __name__ == "__main__":
    main()
