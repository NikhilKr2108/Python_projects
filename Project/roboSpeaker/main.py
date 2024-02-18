import tkinter as tk
from tkinter import messagebox
import pyttsx3

# Function to speak the given text
def speak(text):
    try:
        engine = pyttsx3.init()  # Initialize Text-to-Speech engine
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # Set voice (optional)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred while speaking: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Text-to-Speech Application")

# Create a text entry field to enter the text to speak
text_entry = tk.Entry(root, width=50)
text_entry.grid(row=0, column=0, padx=10, pady=10)

# Create a button to trigger the speaking functionality
speak_button = tk.Button(root, text="Speak", command=lambda: speak(text_entry.get()))
speak_button.grid(row=0, column=1, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
