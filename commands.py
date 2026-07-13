import webbrowser
import wikipedia
import pywhatkit
from datetime import datetime

def execute_command(command):
    command = command.lower()

    if "google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    elif "play" in command:
        song = command.replace("play", "")
        pywhatkit.playonyt(song)
        return f"Playing {song} on YouTube."

    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "")

        try:
            result = wikipedia.summary(topic, sentences=2)
            return result
        except:
            return "Sorry, I couldn't find anything."

    elif "time" in command:
        now = datetime.now().strftime("%I:%M %p")
        return f"The time is {now}"

    elif "exit" in command or "bye" in command:
        return "exit"

    else:
        return "Sorry, I don't understand."