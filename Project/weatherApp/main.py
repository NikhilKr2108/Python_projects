import requests
import json
import pyttsx3      #import OS Module

city = input("Enter your city: ")
url  = f"https://api.weatherapi.com/v1/current.json?key=04d89cdeeb7f4d4a9b7104136241802&q={city}"
r    =  requests.get(url)
# Making a speak function what we need to told just write in speak argument
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# print(r.text)
weatherDetails = json.loads(r.text)
w   =   weatherDetails["current"]["temp_f"]
t   =   weatherDetails["current"]["last_updated"]
speak(f"{t} city is {city} and the temprature in faranhite is {w} degrees")