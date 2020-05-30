import pyttsx3 # pip install pyttsxx3
import datetime
import speech_recognition as sr #pip3 install speechrecognizition
import wikipedia # pip3 install wikipedia
import smtpd
import webbrowser as wb
import os
import pyautogui
import psutil

engine = pyttsx3.init()

def  speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!!")   
    #time()
    #date()

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning !!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening !!")
    else:
        speak("Goof Night ...Sweet dreams")

    speak("How can I help you!")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Sir..could you please repeat!!")
        return "None"
    return query


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aadityazade@gmail.com','12345')
    server.sendemail('aadityazade@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:\\Users\\adityaz\\Documents\\Aaditya\\Python Project\\ss.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak("your cpu is at.."+usage)
    battery = psutil.sensors_battery()
    speak('your battery is at.. ')
    speak(battery.percent)



if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif "send email" in query:
            try:
                speak("please give me content sir!!")
                content = takecommand()
                to = 'xyz@gmail.com'
              #  sendemail(to, content)
              #  speak("Email has been sent")
                speak(content)
            except Exception as e:
                print(e)
                speak("Sorry , I couldnt send the email!")

        elif 'search in chrome' in query:
            speak("What should I search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'logout' in query:
            os.system("shutdown -l")
            
        # elif 'shutdown' in query:
        #     os.system("shutdown /s /t)
        # elif 'restart' in query:
        #     os.system("restart /r /t 1")

        elif 'play songs' in query:
            songs_dir = 'D:\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'add a note' in query:
            speak("What should i remember?")
            data = takecommand()
            speak('Remembering........'+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'give me notes' in  query:
            remember = open('data.txt', 'r')
            speak('you said me to remember that ...'+ remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Screenshot Captured!")

        elif 'cpu' in query:
            cpu()


        elif 'offline' in query:
            speak("Going off!!")
            quit()










