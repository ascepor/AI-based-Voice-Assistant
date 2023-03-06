from ast import Try
from http import server
from posixpath import splitdrive
import smtplib
from threading import main_thread
from pip import main
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import ctypes
import pyjokes
import spotify
import subprocess


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
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

    speak("I am Jarvis Sire. Please tell me how may i help you sire!!!")

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)

        print("say that again please....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gamil.com', '587')
    server.ehlo()
    server.starttls()
    server.login('skgondake@gmail.com', 'saiKIRAN786')
    server.sendmail('skgondake@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        #logic for executing tasks based n query
        if 'wikipedia'in query:
            speak('Searching Wkikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speak("here we go with music")
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir) 
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to sahi' in query:
            try:
                speak("what should I say sire?")
                content = takeCommand()
                to = "skgondake@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my sire , i am not able to send this email at the moment")
        
        elif 'how are you' in query:
            speak("i am fine , Thank you sire")
            speak("how are you sire?")

        elif 'fine' in query or "good" in query:
            speak("it's good to know about you sire ")
        
        elif 'lock screen' in query:
            speak("locking the device ")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
        
        elif 'exit' in query:
            speak("Thanks giving me your Time")
            exit()
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(query)

        elif 'play' in query:
            query = query.replace("play", "")
            webbrowser.open(query)

        elif 'power point presentation' in query:
            speak("opening power point presentation")
            power = r"C:\\Users\\HP\\OneDrive\\Desktop\\Virtual assistant.pptx"
            os.startfile(power)

        elif "write note" in query:
            speak("what should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("sir, should i includde date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "view note" in query:
            speak("showing notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
        
        elif "story" in query:
            speak("reading story")
            file = open("myself.txt", "C:\\Users\\HP\\OneDrive\\Desktop\\myself.txt")
            print(file.read())
            speak(file.read(6))



