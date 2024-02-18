import pyttsx3      #import OS Module

# Making a speak function what we need to told just write in speak argument
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    print("Welcome to ROBOSPEAKER V1.1!\nCreated by Nik")
    while(True):
        user_input = input("What would you like me to say? ")
        if user_input == "q":
            speak("Bye Bye Master")
            break
        try:
            speak(user_input)
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again with a different text.")
