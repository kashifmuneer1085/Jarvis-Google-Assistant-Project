from http import server
from importlib.resources import path
from socket import if_nameindex
from this import s
from tkinter.tix import MAIN
from pip import main
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)  
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
     speak("Good Moring!")

    elif hour>=12 and hour<18:
      speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am your JARVIS. How may I help you")
  
def takeCommand():
    #It takes microphone output from the user and return output in string form

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio= r.listen(source)
    
    try:
        print("Recognozing...")
        query = r.recognoze_google(audio, langauge='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        #print(e)

        print("Say that again please...")
        return "None"
    return query 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.loginI('veerje12@gmail.com', 'qwerty@7496')
    server.sendmail('veerje12@gmail.com', to, content)
    server.close()

if __name__ == "_main_":
    wishMe()
    while True: 
       query = takeCommand().lower()

       #logic in executing tasks based in query
       if 'wikipedia' in query:
           speak("Searching Wikipedia...")
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           print(results)
           speak(results)
       elif 'open youtube' in query:
           webbrowser.open("youtube.com")   
       elif 'open google' in query:
           webbrowser.open("google.com") 
       elif 'open stackoverflow' in query:
           webbrowser.open("stackoverflow.com")  
       elif 'play music' in query:
           music_dir = 'D:\\Music\\songs'
           songs = os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[0]))
       elif  'the time' in query:
           strTime= datetime.datetime.now().strftime("%H:%M:%s") 
           speak(f"Sir, The time is {strTime}")   
       elif 'open code' in query:
           codePath = "C:\\Users\\Altamash Zaheer\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)
       elif 'email to altamash' in query:
           try:
               speak("What shouls I say?")
               content = takeCommand()
               to = "kashi.heart12@gmail.com"
               sendEmail(to, content)
               speak("Email has been sent!")
           except Exception as e: 
               print(e)
               print("Sorry Sir, Due to some Reasons I am not able to send the message!")
