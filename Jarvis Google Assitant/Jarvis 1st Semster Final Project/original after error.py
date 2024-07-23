from atexit import register
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
import webbrowser as wb
wb.register('chrome', None)
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

    speak("I am your JARVIS Sir!. Please tell me how may I help you")
  
def takeCommand():
    #It takes microphone output from the user and return output in string form

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
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
    server.loginI('mehr68909@gmail.com', 'qwerty@7513')
    server.sendmail('mehr68909@gmail.com', to, content)
    server.close()

if __name__ == "_main_":
    wishMe()
    if 1:
   # while True: 
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
           wb.open('https://www.youtube.com')
           True 
       elif 'open google' in query:
           wb.open('https://www.google.com')
           True
       elif 'open chrome' in query:
            codePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)
       elif 'open stackoverflow' in query:
           wb.open('https://stackoverflow.com')
           True 
       elif 'play music' in query:
           music_dir = 'E:\\music'
           songs = os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[0]))
       elif  'tell me the the time' in query:
           strTime= datetime.datetime.now().strftime("%H:%M:%s") 
           speak(f"Sir, The time is {strTime}")   
       elif 'open code' in query:
           codePath = r"C:\Users\Mehr Kashif\AppData\Local\Programs\Microsoft VS Code\Code.exe"
           os.startfile(codePath)
       elif 'open idle' in query:
           codePath = r"C:\Users\Mehr Kashif\AppData\Local\Programs\Python\Python310\Lib\idlelib\idle.pyw"
           os.startfile(codePath)
       elif 'open powerpoint' in query:
           codePath = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
           os.startfile(codePath)
       elif 'open word' in query:
           codePath = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
           os.startfile(codePath)
       elif 'open excel' in query:
           codePath = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
           os.startfile(codePath)
       elif 'quit' in query:
           exit()
       elif 'email to kashif' in query:
           try:
               speak("What shouls I say?")
               content = takeCommand()
               to = "kashi.heart12@gmail.com"
               sendEmail(to, content)
               speak("Email has been sent!")
           except Exception as e: 
               print(e)
               print("Sorry Sir, Due to some Reasons I am not able to send the message!")