import sys
import os
import subprocess

PYTHON311 = r"C:\Users\at376\AppData\Local\Programs\Python\Python311\python.exe"

if sys.executable.lower() != PYTHON311.lower():
    try:
        import pyaudio  # noqa: F401
    except ImportError:
        env = {**os.environ, "PYTHONUNBUFFERED": "1"}
        subprocess.run([PYTHON311, "-u", *sys.argv], check=True, env=env)
        sys.exit(0)

import speech_recognition as sr
import pyttsx3

# Initialize recognizer
recognizer = sr.Recognizer()

# Initialize voice engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # female voice
engine.setProperty('rate', 170)


def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You:", command)
            return command.lower()

        except:
            return ""


def extract_app_name(command, keyword):
    if keyword not in command:
        return ""
    name = command.split(keyword, 1)[-1].strip()
    for prefix in ("the ", "a ", "my "):
        if name.startswith(prefix):
            name = name[len(prefix):]
    return name


def open_app(start_cmd):
    if start_cmd == "explorer":
        os.startfile("explorer.exe")
    else:
        subprocess.Popen(f'start "" {start_cmd}', shell=True)


def resolve_app(name, apps):
    name = name.strip().lower()

    aliases = {
        "note pad": "notepad",
        "note": "notepad",
        "calc": "calculator",
        "ms paint": "paint",
        "file explorer": "explorer",
        "files explorer": "explorer",
        "windows explorer": "explorer",
        "explore": "explorer",
        "files": "explorer",
        "my computer": "explorer",
        "this pc": "explorer",
        "command prompt": "cmd",
        "terminal": "cmd",
        "google chrome": "chrome",
    }

    if name in aliases:
        name = aliases[name]

    if name in apps:
        return name

    for app_key in apps:
        if app_key in name or name in app_key:
            return app_key

    return name


def execute_command(command):

    apps = {
        "calculator": {"start": "calc", "process": "CalculatorApp.exe"},
        "chrome": {"start": "chrome", "process": "chrome.exe"},
        "notepad": {"start": "notepad", "process": "notepad.exe"},
        "paint": {"start": "mspaint", "process": "mspaint.exe"},
        "explorer": {"start": "explorer", "process": "explorer.exe"},
        "cmd": {"start": "cmd", "process": "cmd.exe"},
    }

    # OPEN APPLICATION
    if "open" in command:

        app = resolve_app(extract_app_name(command, "open"), apps)

        if app in apps:
            speak(f"Opening {app}")
            open_app(apps[app]["start"])
        else:
            speak(f"Sorry, I don't know how to open {app}")

    # CLOSE APPLICATION
    elif "close" in command:

        app = resolve_app(extract_app_name(command, "close"), apps)

        if app in apps:
            process = apps[app]["process"]
        elif app.endswith(".exe"):
            process = app
        else:
            process = f"{app}.exe"

        speak(f"Closing {app}")
        os.system(f'taskkill /f /im "{process}"')

    # LOCK SCREEN
    elif "lock screen" in command:

        speak("Locking your computer")
        os.system("rundll32.exe user32.dll,LockWorkStation")

    # SLEEP COMPUTER
    elif "sleep computer" in command:

        speak("Putting computer to sleep")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    # SHUTDOWN
    elif "shutdown computer" in command:

        speak("Shutting down computer")
        os.system("shutdown /s /t 1")

    # RESTART
    elif "restart computer" in command:

        speak("Restarting computer")
        os.system("shutdown /r /t 1")

    # EXIT
    elif "exit jarvis" in command:

        speak("Goodbye")
        exit()


# Start assistant
if __name__ == "__main__":
    speak("Jarvis assistant started")

    while True:

        command = listen()

        if not command:
            continue

        # WAKE WORD (optional — also accepts direct commands)
        if "hello jarvis" in command or "hey jarvis" in command:
            speak("Yes, I am listening")
            command = listen()
            if not command:
                continue

        execute_command(command)
