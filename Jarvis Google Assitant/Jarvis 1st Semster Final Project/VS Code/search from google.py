import speech_recognition as sr
import webbrowser
sr.Microphone(device_index=1)
r = sr.Recognizer()
r.energy_threshold=5000
audio = r.listen(source)
with sr.Microphone() as source:
             
             print("Speak The word you want to search:----")


try:
             
             text = r.recognize_google(audio)
             print(("You said:",format(text)))
             url="https://www.google.com/search?q="
             search_url=url+text 
             webbrowser.open(search_url)
except:
                print("Can't Recognize")