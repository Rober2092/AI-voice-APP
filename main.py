import datetime
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")
    if "hello" in text:
        speak("Hello I am luna! How can I help you today?")
    elif "time" in text:
        speak("The current time is " + str(datetime.datetime.now().time()))
    else:
        speak("I'm sorry, I didn't understand what you said.")      
except:
    print("Sorry, I didn't understand that.")

