import tkinter as tk
import requests
import json
import pyttsx3

def get_weather_and_speak(speak_on):
    """Fetches weather data, updates GUI, and optionally speaks it aloud."""

    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Invalid Input", "Please enter a valid city name.")
        return

    try:
        response = requests.get(f"https://api.weatherapi.com/v1/current.json?key=04d89cdeeb7f4d4a9b7104136241802&q={city}")
        response.raise_for_status()  # Raise an exception for non-200 status codes
        weather_data = json.loads(response.text)
        update_display(weather_data)
        if speak_on:
            speak_weather(weather_data)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred while fetching weather data: {e}")
    except json.JSONDecodeError:
        messagebox.showerror("Invalid Response", "API response could not be parsed.")

def update_display(weather_data):
    """Updates the text labels in the GUI with the weather information."""

    if not weather_data:
        return

    city_label.config(text=f"City: {weather_data['location']['name']}")
    temperature_label.config(text=f"Temperature: {weather_data['current']['temp_f']}°F")
    last_updated_label.config(text=f"Last Updated: {weather_data['current']['last_updated']}")

def speak_weather(weather_data):
    """Reads the weather data aloud using pyttsx3."""

    if not weather_data:
        return

    city = weather_data["location"]["name"]
    temperature = weather_data["current"]["temp_f"]
    last_updated = weather_data["current"]["last_updated"]

    text = f"The current temperature in {city} is {temperature} degrees Fahrenheit. Last updated: {last_updated}."

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Optionally set a preferred voice (choose an index from the list of voices)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

# Create the Tkinter window
root = tk.Tk()
root.title("Weather App")

# Create input field for city name
city_label = tk.Label(root, text="Enter City:")
city_label.grid(row=0, column=0, sticky=tk.W)
city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=5)

# Create two buttons: "Get Weather" and "Speak Weather"
get_weather_button = tk.Button(root, text="Get Weather", command=lambda: get_weather_and_speak(False))
get_weather_button.grid(row=1, column=0, pady=10)

speak_weather_button = tk.Button(root, text="Speak Weather", command=lambda: get_weather_and_speak(True))
speak_weather_button.grid(row=1, column=1, pady=10)

# Create labels to display weather information
city_label = tk.Label(root, text="-")
city_label.grid(row=2, column=0, sticky=tk.W)
temperature_label = tk.Label(root, text="-")
temperature_label.grid(row=3, column=0, sticky=tk.W)
last_updated_label = tk.Label(root, text="-")
last_updated_label.grid(row=4, column=0, sticky=tk.W)

# Start the Tkinter event loop
root.mainloop()
