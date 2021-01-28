import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) #1 is for female voice
engine.setProperty('voice', voices[0].id)# 0 here is male voice


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()
    


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis,sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Say that again please...")  
        return "None"
    return query

#main loop

wishMe()
while True:
# if 1:
    query = takeCommand().lower()

    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")   


    elif 'play music' in query:
        music_dir = "" #paste your directories with music downloaded in it
        songs = os.listdir(music_dir)
        print(songs)
      
        os.startfile(os.path.join(music_dir, songs[random.randint(0,11)]))
        
    elif "what's the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")

    elif 'open python' in query:
        codePath = "C:\\Users\\pro20\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\idlelib\\idle.pyw"
        os.startfile(codePath)

    elif 'terminate' in query:
        speak("Thank You!")
        break
    
