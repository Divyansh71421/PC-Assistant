# 🎙️ Friday - Voice Controlled Desktop Assistant

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-green)
![License](https://img.shields.io/badge/License-MIT-orange)

## 📖 Overview

**Friday** is a Python-based voice-controlled desktop assistant designed for Windows systems. It listens to voice commands through the microphone, converts speech into text, and performs desktop automation tasks such as opening applications, closing running programs, locking the computer, shutting down the system, and more.

The assistant uses Google's Speech Recognition service for voice input and Text-to-Speech (TTS) to provide spoken responses, creating a hands-free interaction experience.

---

# ✨ Features

- 🎤 Voice Recognition
- 🔊 Female Voice Responses
- 🖥️ Open Windows Applications
- ❌ Close Running Applications
- 🔒 Lock Computer
- 😴 Put Computer to Sleep
- 🔄 Restart Computer
- ⛔ Shutdown Computer
- 👋 Wake Word Detection
- ❤️ Custom Voice Responses

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python 3.11 | Programming Language |
| SpeechRecognition | Convert speech into text |
| PyAudio | Capture microphone input |
| pyttsx3 | Offline Text-to-Speech |
| subprocess | Launch applications |
| os | Windows system operations |

---

# 🏗 Project Architecture

```
User Speech
      │
      ▼
Microphone Input
      │
      ▼
SpeechRecognition
      │
      ▼
Command Processing
      │
      ▼
Execute Windows Commands
      │
      ▼
Voice Response using pyttsx3
```

---

# 📂 Project Structure

```
Friday/
│
├── friday.py
├── README.md
└── requirements.txt
```

---

# ⚙ Requirements

- Windows 10 / Windows 11
- Python 3.11
- Git Bash (Optional)
- Working Microphone

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/Divyansh71421/PC-Assistant.git
```

Move inside project

```bash
cd PC-Assistant
```

Install dependencies

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
```

Or

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

```bash
python friday.py
```

Assistant will respond

```
Friday assistant started
```

Now simply speak your commands.

---

# 🎤 Supported Voice Commands

## Open Applications

```
Open Chrome
Open Calculator
Open Notepad
Open Paint
Open PowerShell
Open Command Prompt
Open File Explorer
Open Git Bash
```

---

## Close Applications

```
Close Chrome
Close Calculator
Close Notepad
Close Paint
Close PowerShell
Close Command Prompt
Close Git Bash
```

---

## System Commands

```
Lock Screen
Sleep Computer
Restart Computer
Shutdown Computer
Exit Friday
```

---

## Wake Commands

```
Hello Friday
Hey Friday
```

After the wake word, Friday waits for your next command.

---

# 💡 How It Works

1. Initializes the speech recognizer.
2. Activates the microphone.
3. Listens for user speech.
4. Converts speech to text using Google Speech Recognition.
5. Identifies the requested command.
6. Executes the corresponding Windows operation.
7. Responds with voice feedback.

---

# 📌 Current Applications Supported

- Google Chrome
- Calculator
- Notepad
- Paint
- File Explorer
- Command Prompt
- PowerShell
- Git Bash

Additional applications can easily be added by updating the application dictionary.

---

# 🚀 Applications

This project can be used for:

- Personal Desktop Automation
- Voice Controlled PC
- Accessibility Assistance
- Productivity Automation
- Learning Speech Recognition
- Python Automation Projects
- AI Assistant Prototype

---

# 🔒 Limitations

- Windows Only
- Requires Internet for Google Speech Recognition
- Limited to predefined commands
- English voice commands only

---

# 🔮 Future Improvements

- Offline Speech Recognition
- ChatGPT Integration
- Open Any Installed Software Automatically
- Web Search Support
- File Management Commands
- Volume & Brightness Control
- Weather Updates
- Music Control
- Smart Home Integration
- Custom Wake Word
- GUI Dashboard

---

# 🤝 Contributing

Contributions are welcome.

Feel free to:

- Fork the repository
- Create a feature branch
- Commit your changes
- Submit a Pull Request

---

# 👨‍💻 Author

**Divyansh Singh**

GitHub:
https://github.com/Divyansh71421

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
