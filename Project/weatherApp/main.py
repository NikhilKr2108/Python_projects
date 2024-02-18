import requests
import json
import pyttsx3      #import OS Module

# input command
city = input("Enter your city: ")

# https://www.weatherapi.com weather is according to this website
url  = f"https://api.weatherapi.com/v1/current.json?key=04d89cdeeb7f4d4a9b7104136241802&q={city}"

# Request from the weather api website
r    =  requests.get(url)

# Making a speak function what we need to told just write in speak argument
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# data read by jsom module
weatherDetails = json.loads(r.text)

# Data arange by in these variables
w   =   weatherDetails["current"]["temp_f"]
t   =   weatherDetails["current"]["last_updated"]

# using robospeaker function for speake a temprature
speak(f"{t} city is {city} and the temprature in faranhite is {w} degrees")