from assistant import speak, take_command
from commands import execute_command

def main():
    speak("Hello! I am Jarvis. How can I help you?")

    while True:
        command = take_command()

        if command == "":
            continue

        result = execute_command(command)

        if result == "exit":
            speak("Goodbye! Have a nice day.")
            break

        speak(result)

if __name__ == "__main__":
    main()
