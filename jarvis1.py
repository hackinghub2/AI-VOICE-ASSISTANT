import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes
import wolframalpha
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvis import Ui_MainWindow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)   
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

    speak("I am Jarvis ,  your personal assistant , Please tell me how may I help you")       


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.taskexecution

    
        
    def takeCommand(self):
    #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            self.query = r.recognize_google(audio, language='en-in')
            print(f"User said: {self.query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")  
            return "None"
        return self.query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jtalekar2003@gmail.com', 'your-password')
    server.sendmail('jtalekar2003@gmail.com', to, content)
    server.close()


    if __name__ == "__main__":
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
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'play' in query:
                song = query.replace('play', '')
                speak('playing' +song)
                pywhatkit.playonyt(song)

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif "calculate" in query:
                
                app_id = "2R58LH-AJ8QYKTGEV"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")   
            
            elif 'joke' in query:
                speak(pyjokes.get_joke())

            elif 'play music' in query:
                music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                time = datetime.datetime.now().strftime("%I:%M %p") 
                print(time)   
                speak(f"Sir, the time is {time}")

            elif 'date' in query:
                speak('sorry,i have a headache')

            elif 'are you single' in query:
                speak('i am in a relationship with python')

            elif 'open code' in query:
                codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'email to harry' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "jtalekar2003@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend jatin bhai. I am not able to send this email")    
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushbutton.clicked.connect(self.starTtask)
        self.ui.pushbutton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\Jatin\J\\ROTATE.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\Jatin\J\\INITIATE.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
       