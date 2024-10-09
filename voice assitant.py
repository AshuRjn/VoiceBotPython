import listener
import speech_recognition as sr
import datetime
import pywhatkit
import pyttsx3
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0])  # Use voices[0] or another index that corresponds to the desired voice
recognizer = sr.Recognizer()

def cmd():
    command = ""
    with sr.Microphone() as origin:
        print("clearing background noises...please wait")
        recognizer.adjust_for_ambient_noise(origin, duration=0.5)
        print("ask me anything....")
        speech = listener.recognize(origin)

        try:
            command = listener.recognize_google(speech)
            command = command.lower()
            if "shin" in command:
                print(command)
            print(command)
        except:
            pass

    if 'google' in command:
        engine.say('opening google')
        webbrowser.open('https://www.google.com/')
    if 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        print(time)
        engine.say('time')
        webbrowser.open('https://time.is/')
    if 'play' in command:
        engine.say('opening youtube')
        webbrowser.open("https://www.youtube.com/")
    engine.runAndWait()
    pywhatkit.playonyt(command)
    if 'youtube' in command:
        engine.say('opening youtube')
        webbrowser.open("https://www.youtube.com/")
        engine.runAndWait()

if __name__ == "main":
    cmd()