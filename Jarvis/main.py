import pyttsx3                     #pip install pyttsx3
import speech_recognition as sr    #pip install speechRecognition
import datetime
import wikipedia                   #pip install wikipedia
import webbrowser
import os
import smtplib
print("Initializing Jarvis")

MASTER = "Everyone"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()


#This function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    assname =("Jarvis 1 point o")
    speak("I am your Assistant")
    speak(assname)

    #speak("I am Jarvis. How may I help you?")


#this function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print("Unable to Recognize your voice")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shrutiswift@gmail.com','password')
    server.sendemail('swastik1706@gmail.com'. to, content)
    server.close()
#main program starts here
#speak("Initializing Jarvis...")
wishMe()
query = takeCommand()

#Logic for executing tasks as per the query
if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query = query.replace('wikipedia', "")
    results = wikipedia.summary(query, sentences = 2)
    speak("Accoding to wikipedia")
    print(results)
    speak(results)

elif 'How are you?' in query.lower():
    speak("I am fine, Thank you")
    speak("How are you? Sir")

elif 'open youtube' in query.lower():
    
    url = "youtube.com"
    webbrowser.open("https://www.youtube.com/")

elif 'open google' in query.lower():
    speak ("Here you go to google\n")
    webbrowser.open("google.com")

elif "camera" in query or "take a photo" in query:
    ec.capture(0, "Jarvis Camera ", "img.jpg")
 

elif 'the time' in query.lower():
    strTime = datetime.datetime.now(),strftime("%H:%M:%S")
    speak(f"[MASTER] the time is {strTime}")

elif 'open code' in query.lower():
    codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code"
    os.startfile(codePath)

