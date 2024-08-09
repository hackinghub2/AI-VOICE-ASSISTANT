import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import password
import random
import sys
import openai
import time
from pywikihow import search_wikihow
from PyQt5.QtCore import pyqtSlot
import subprocess
import os
import os.path
import numpy as np
from forex_python.converter import CurrencyRates
from googletrans import Translator
import cv2
from requests import get 
#from features import convert_currency, translate_text
import pywhatkit as kit
import requests
from config import apikey
import smtplib
import pyjokes
from googletrans import Translator
import pyautogui
import pywikihow
from playsound import playsound
import pywhatkit
import wikipedia as googleScrap
import wolframalpha
import PyPDF2
import secure_smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import instaloader 
import operator
from features import translate_text
from requests import get 
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
#88 print(voices[1].id)   
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

# text to speech
def speak(audio):
    engine.say(audio)
    #print(audio)
    engine.runAndWait()



#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("I am  jarvis ,  your personal assistant , Please tell me how may I help you")   

# for news updates
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=make you api key here'

    main_page= requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day=["first", "second", "third", "fourth", "fifth","sixth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        print(f"today's {day[i]} news is: ", {head[i]}) 
        speak(f"today's {day[i]} news is: {head[i]})")

# chatStr = ""
#  https://youtu.be/Z3ZAJoi4x6Q
# def chat(query):
#     global chatStr
#     print(chatStr)
#     openai.api_key = apikey
#     chatStr += f"jatin: {query}\n Jarvis: "
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt= chatStr,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
    # todo: Wrap this inside of a  try catch block
    #speak  (response["choices"][0]["text"])
    #chatStr += f"{response['choices'][0]['text']}\n"
    #return response["choices"][0]["text"]
    # response_text = response["choices"][0]["text"]
    # chatStr += f"{response_text}\n"
    # return response_text



def track_asteroids():
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    api_key = "paste your api key here"  # Get an API key from NASA

    params = {
        "api_key": api_key,
        "detailed": "false",
        "page": "1",
        "size": "5"
    }

    response = requests.get(url, params=params)
    data = response.json()

    try:
        asteroids = data["near_earth_objects"]
        for date in asteroids:
            for asteroid in asteroids[date]:
                name = asteroid["name"]
                diameter = asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"]
                miss_distance = asteroid["close_approach_data"][0]["miss_distance"]["kilometers"]
                velocity = asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]

                info = f"Asteroid {name} is approaching. It has an estimated diameter of {diameter} kilometers. It will pass by at a distance of {miss_distance} kilometers with a velocity of {velocity} kilometers per hour."
                speak(info)
                print (info)

    except Exception as e:
        return "Sorry, I couldn't retrieve asteroid data at the moment."


def get_space_news():
    url = "https://api.nasa.gov/planetary/apod"

    api_key = "Paste your api key"  # Get an API key from NASA
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    data = response.json()
    
    if "title" in data and "explanation" in data:
        title = data["title"]
        explanation = data["explanation"]
        return f"Title: {title}\n\n{explanation}"
    else:
        return "Unable to fetch space news at the moment."

# def get_weather(city):
#     api_key = "paste your api key"  # Replace with your actual API key
#     base_url = "http://api.openweathermap.org/data/2.5/weather?"

#     complete_url = f"{base_url}q={city}&appid={api_key}"
#     response = requests.get(complete_url)
#     data = response.json()





def TEMPE():
            search = "temperature in mumbai"
            url = f"https://www.google.com/search?q=+{search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div", class_="BNeawe").text
            speak(f"the temperature outside is {temperature} calcius")

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

        
        # To read PDF



class MainThread(QThread):
        update_output = pyqtSignal(str)
        def __init__(self):
            super(MainThread,self).__init__()

        def run(self):
            self.TaskExecution()


        def takecommand(self):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("listening...")
                r.pause_threshold = 1
                r.energy_threshold = 400
                r.adjust_for_ambient_noise (source)
                audio = r.listen(source)
            try:
                print("Recognizing...")
                self.query = r.recognize_google (audio, language='en-in') 
                print (f"user said: {self.query}")

            except Exception as e:
            # speak("Say that again please...")
                return "none"
            self.query= self.query.lower()
            return self.query
        
        def TakeHindi(self):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("listening...")
                r.pause_threshold = 1
                r.energy_threshold = 400
                r.adjust_for_ambient_noise (source)
                audio = r.listen(source)
            try:
                print("Recognizing...")
                self.query = r.recognize_google (audio, language='hi') 
                print (f"user said: {self.query}")

            except Exception as e:
            # speak("Say that again please...")
                return "none"
            self.query= self.query.lower()
            return self.query
        
       

        
      

       

        
        

        def TaskExecution(self):
            
            wish()  
            is_awake= True
            while True:
                if is_awake:
                    self.query = self.takecommand()
                else:
                    # If Jarvis is asleep, don't listen for commands until wake up command is received
                    self.query = input("Press any key to wake up Jarvis: ")
                    speak("I'm awake now. How can I assist you?")
                    is_awake = True
                    continue

                if "you can sleep" in self.query:
                    speak("Thank you for using my services. Going to sleep now.")
                    is_awake = False  # Put Jarvis to sleep
                    continue  # Go back to the beginning of the loop

                if "wake up" in self.query:
                    speak("I'm already awake. How can I assist you?")
                    continue  # Continue listening for further commands
                    
                        #logic building for tasks

                
                elif "open notepad" in self.query:
                    npath = "C:\\Windows\\SysWOW64" 
                    os.startfile(npath)

                
                

                elif "close notepad" in self.query:
                    speak("okay sir closing notepad")
                    os.system("taskkill /f /im notepad.exe")



                elif "track asteroids" in self.query:
                    track_asteroids()

                elif "Using artificial intelligence".lower() in self.query.lower():
                    ai(prompt=self.query)

                


                

                elif "get weather" in self.query:
                    speak("Sure, please tell me the city name.")
                    city = self.takecommand()
                    weather_info = get_weather(city)
                    if weather_info is not None:
                        temperature, humidity, weather_desc = weather_info
                        speak(f"The temperature in {city} is {temperature} Kelvin. The humidity is {humidity}% and the weather is {weather_desc}.")
                    else:
                        speak(f"Sorry, I couldn't find weather information for {city}. Please check the city name.")

                

            
                

                elif "open command prompt" in self.query: 
                    os.system("start cmd")

                # Inside your TaskExecution method
                # elif "convert currency" in self.query:
                #     try:
                #         parts = self.query.split(" ")
                #         amount = float(parts[2])
                #         from_currency = parts[3]
                #         to_currency = parts[5]
                #         conversion_result = convert_currency(amount, from_currency, to_currency)
                #         speak(conversion_result)
                #     except (ValueError, IndexError):
                #         speak("Sorry, I couldn't understand the currency conversion request. Please try again.")


                elif "temperature" in self.query:
                    TEMPE()

                if "translate" in self.query:
                     parts = self.query.split(" ")
                     text = " ".join(parts[1:-1])
                     target_language = parts[-1]

                     translation_result = translate_text(text, target_language)
                     speak(translation_result)

                elif 'how to' in self.query:
                    speak("getting data from internet ")
                    op = self.query.replace("jarvis", "")
                    max_result = 1
                    how_to_func = search_wikihow(op,max_result)
                    assert len(how_to_func) == 1
                    how_to_func[0].print()
                    speak(how_to_func[0].summary)
                

                elif "explain the project" in self.query:
                    speak('This is a Python script that defines several functions and imports various libraries for creating a virtual assistant named Jarvis. The script imports libraries like pyttsx3 for text to speech conversion, speech_recognition for voice recognition, datetime for time-based operations, wikipedia and webbrowser for fetching information from the internet, pywhatkit for sending messages using WhatsApp, smtplib for sending emails, PyPDF2 for reading PDFs, instaloader for Instagram-related operations, cv2 for capturing images from the camera, pyjokes for telling jokes, pyautogui for taking screenshots, and wolframalpha for performing mathematical operations. The code also defines several functions like speak for text-to-speech conversion, wish for greeting the user, news for getting the latest news, pdf_reader for reading PDFs, and takecommand for recognizing the users voice commands.The code creates an object of the MainThread class, which inherits from the QThread class in the PyQt5 library. The MainThread object defines a TaskExecution method that listens to the users voice commands and performs the corresponding tasks using conditional statements. The MainThread object also defines a run method that executes the TaskExecution method.Finally, the code creates an object of the Ui_MainWindow class, which is defined in a separate file named jarvis.py. This class defines the user interface for the Jarvis virtual assistant, using the PyQt5 library')

                elif "open camera" in self.query: 
                    cap = cv2.VideoCapture(0)
                    while True: 
                        ret, img = cap.read() 
                        cv2.imshow('webcam', img) 
                        k = cv2.waitKey(50)
                        if k==27:
                            break
                    cap.release()
                    cv2.destroyAllWindows()

                elif "greet  invigilators" in self.query:
                    speak("good morning respected sir /madam and external examinar, am i sure you would like me")

                elif 'the time' in self.query:
                    time = datetime.datetime.now().strftime("%I:%M %p") 
                    print(time)   
                    speak(f"Sir, the time is {time}")

               # elif "are you single" in self.query:
                    #speak("no,i am in relationship with python")

                elif "ip addres" in self.query:
                    ip = get('https//api.ipfy.org').text
                    speak(f"your ip address is {ip}") 

                # Inside your TaskExecution method
                elif "space news" in self.query:
                    space_news = get_space_news()
                    speak(space_news)
                    get_space_news()


                elif 'joke' in self.query:
                    speak(pyjokes.get_joke())

                elif 'alarm' in self.query:
                    speak("tell me the time")
                    time = input(":enter the time:")

                    while True:
                        Time_Ac = datetime.datetime.now()
                        now = Time_Ac.strftime("%H:%M:%S")

                        if now == time:
                            speak("time to wake up sir")
                            playsound('Death-Bed-Powfu.mp3')
                            speak("alarm closed")

                        elif now>time:
                            break

               
            
                elif 'wikipedia' in self.query:
                    speak('Searching Wikipedia...')
                    self.query = self.query.replace("wikipedia", "")
                    results = wikipedia.summary(self.query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'google search' in self.query:
                    query = self.query.replace("jarvis","")
                    query = self.query.replace("google search","")
                    query = self.query.replace("google","")
                    speak("this is what i found for you")
                    pywhatkit.search(self.query)

                    try:
                        
                        result = googleScrap.summary(self.query,3)
                        speak(result)

                    except:
                        speak("no speakable data availabe")

                elif "youtube" in self.query: 
                    speak("opening youtube sir")
                    self.query = self.query.replace("jarvis","")
                    self.query = self.query.replace("youtube","")
                    web = "https://www.youtube.com/results?search_query=" +self.query
                    webbrowser.open(web)

                elif "open facebook" in self.query: 
                    webbrowser.open("www.facebook.com")

                elif "open stackoverflow" in self.query: 
                    webbrowser.open("www.stackoverflow.com")

                elif "open google" in self.query:
                    speak("sir, what should i search on google")
                    cm = self.takecommand()
                    webbrowser.open(f" {cm}")

                elif "thank you" in self.query or "thanks" in self.query: 
                    speak("it's my pleasure sir.")

                elif 'send message ' in self.query:
                    kit.sendwhatmsg("+918928611248", "hii" ,8,34)

                elif 'switch the window' in self.query: 
                    pyautogui.keyDown("alt") 
                    pyautogui.press("tab") 
                    time.sleep(1) 
                    pyautogui.keyUp("alt")

                
                
                elif 'remember that ' in self.query:
                    rememberMsg = self.query.replace("remember that","")
                    rememberMsg = rememberMsg.replace("jarvis", "")
                    speak("you tell me to remind you that: " + rememberMsg)
                    remember = open('data.txt', 'w')
                    remember.write(rememberMsg)
                    remember.close()

                elif 'what do you remember' in self.query:
                    remember = open('data.txt', 'r')
                    speak("you told me to remember " + remember.read())
                    remember.close()

                    

                elif "tell me news" in self.query: 
                    speak ("please wait sir, fetching the latest news") 
                    news()

                elif 'play' in self.query:
                    song = self.query.replace('play', '')
                    speak('playing' +song)
                    pywhatkit.playonyt(song)

                #-------- To find my location using IP Address -------------

                elif "where i am" in self.query or "where we are" in self.query: 
                    speak("wait sir, let me check") 
                    try:
                            ipAdd = requests.get('https://api.ipify.org').text
                            print(ipAdd)
                            url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                            geo_requests = requests.get(url) 
                            geo_data = geo_requests.json() 
                            # print(geo_data) 
                            city= geo_data['city'] 
                            # state = geo_data['state'] 
                            country= geo_data['country'] 
                            speak(f"sir i am not sure, but i think we are in {city} city of {country} country")      
                    except  Exception as e:
                            speak("sorry sir, Due to network issue i am not able to find where we are.") 
                            pass
                        

                #-------- To check a instagram profile -----------
                elif "instagram profile" in self.query or "profile on instagram" in self.query: 
                    speak("sir please enter the user name correctly.") 
                    name = input("Enter username here: ")
                    webbrowser.open(f"www.instagram.com/{name}")
                    speak(f"Sir here is the profile of the user {name}")
                    time.sleep(5)
                    speak("sir would you like to download profile picture of this account.")
                    condition = self.takecommand()
                    if "yes" in condition:
                        mod =instaloader.Instaloader() #pip install instadownloader
                        mod.download_profile(name, profile_pic_only=True)
                        speak("i am done sir, profile picture is saved in our main folder.. now i am ready for next commaand")
                    else:
                        pass

                #-------- To take screenshot -----------
                elif "take screenshot" in self.query or "take a screenshot" in self.query: 
                    speak("sir, please tell me the name for this screenshot file")
                    name = self.takecommand()
                    speak("please sir hold the screen for few seconds, i am taking sreenshot")
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(f" (name).png") 
                    speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")


                # speak("sir, do you have any other work")

                # To Read PDF file
                elif "read pdf" in self.query: 
                    pdf_reader()

                #---------- To hide files and folder:----------
                elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                    speak("sir please tell me you want to hide this folder or make it visible for everyone") 
                    condition = self.takecommand() 
                    if "hide" in condition:
                        os.system("attrib +h /s /d") #os module                                                                                 
                        speak("sir, all the files in this folder are now hidden.")

                    elif "visible" in condition:
                        os.system("attrib -h /s /d")         
                        speak("sir, all the files in this folder are now visible to everyone. i wish you are taking")

                    elif "leave it" in condition or "leave for now" in condition: 
                        speak ("Ok sir")

                    else:
                            print("Chatting...")
                            chat(self.query)


if __name__ == "__main__":
    password.Speak("This Particular File Is Password Protected .")
    password.Speak("Kindly Provide The Password To Access .")
    pass_input = input("Provide the password: ")
    password.Pass(pass_input)       

   
        

            
startExecution = MainThread()  

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

        

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\Jatin\J\\ROTATE.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\Jatin\J\\INITIATE.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec())




















