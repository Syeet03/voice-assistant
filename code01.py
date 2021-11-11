import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import code02

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('Voices')
engine.setProperty('Voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()