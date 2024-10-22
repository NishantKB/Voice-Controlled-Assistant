import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui as pai
import psutil
import pyjokes


engine = pyttsx3.init()

Lady_english="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

Male_english="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

Lady_spanish="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"

engine.setProperty('rate', 150)
engine.setProperty('volume',1)
engine.setProperty('voice',Lady_english)

def speak(content):
    engine.say(content)
    engine.runAndWait()

def wish():
    speak("Hi, I am your AI Assistant how can I help you?")

def screen():
    img = pai.screenshot()
    current_dir = os.getcwd()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'screenshot_{timestamp}.png'
    img.save(os.path.join(current_dir,filename))

def date_time():
    now = datetime.now()
    current_date = now.strftime("%B %d, %Y")  
    current_time = now.strftime("%I:%M:%S %p")
    speak(f"Today's date is {current_date}")
    speak(f"The current time is {current_time}")

def speak_date():
    now = datetime.now()
    current_date = now.strftime("%B %d, %Y")  
    speak(f"Today's date is {current_date}")

def speak_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")  
    speak(f"The current time is {current_time}")

def sendMail(to,content):
    server = smtplib.SMTP('smtp@gmail.com',587)
    server.ehlo
    server.starttls
    server.login('email','pass')
    server.sendmail('email',to,content)
def chrome():
    speak("What should i search in chrome?")
    path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    search = take_command().lower()
    wb.get(path).open_new_tab(search)

def cpu():
    usage = str(psutil.cpu_percent())
    speak("The CPU usage is" + usage) 

def battery():
    bat = psutil.sensors_battery()
    speak("The Battery percent is " + str(bat.percent))  

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language ="en")
        print(query)
    except Exception as e:
        print(e)
        speak("Cant understand, Say that again please")
        return "None"
    return query
def joke():
    speak(pyjokes.get_joke())
    
if __name__ == "__main__":
    wish()
    while True:
        query = take_command().lower()
        if 'time' in query:
            speak_time()

        elif 'date' in query:
            speak_date()

        elif 'wikipedia' in query:
            speak("Searching in wikipedia")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to ="abc@gmail.com"
                # sendMail(to,content)
                print(content)
                speak(content)
            except Exception as e:
                print(e)
                speak("Unable to send email")

        elif 'open chrome' in query:
            chrome()

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play song' in query:
            song_dir ="D:\\Music"
            songs = os.listdir(song_dir)
            os.startfile(os.path.join(song_dir,songs[0]))
        
        elif 'remember' in query:
            speak("What should I remeber")
            data = take_command()
            speak("I remembered that"+data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close
        
        elif 'do you know what i said' in query:
            remember = open("data.txt","r")
            speak("Yes I remembered you said that " + remember.read())
        
        elif 'screenshot' in query:
            screen()
            speak("Screenshot taken sucessfully!")

        elif 'cpu' in query:
            cpu()

        elif 'battery' in query:
            battery()
        
        elif 'joke' in query:
            joke()

        elif 'offline' in query:
            speak("Alright, Goodbye!")
            quit()
        else:
            speak("I cant do what you said me")
