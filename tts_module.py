version = "1.0"
creator = "Fox2099"
date = "10/01/2024"

import pyttsx3
engine = pyttsx3.init()
engine.setProperty("voice", "brazil")

def speak(text):
    engine.say(text)
    engine.runAndWait()
