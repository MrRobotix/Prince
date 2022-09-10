import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from bs4 import BeautifulSoup
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir")

    speak("Wellcome back. please tell me how may i help you")

def takecommand():
    #it takes microphone input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        speak('''say that again please...
               or make sure you are connect with the internet''')
        return "None"
    return query


class Response:
    pass


def Temperature():
    city = query.split("in", 1)
    soup = BeautifulSoup(requests.get(f"https://www.google.com/search?q=weather+in+{city[1]}").text, "html.parser")
    region = soup.find("span", class_= "BNeawe tAd8d AP7Wnd")
    temp = soup.find("div", class_="BNeawe i8p4i AP7Wnd")
    day = soup.find("div", class_="BNeawe tAd8d AP7Wnd")
    weather = day.text.split("m", 1)
    temperature = temp.text.split("C",1)
    Response("Its Currently"+weather[1]+" and "+temperature[0]+"Celcius"+"in"+region.text)





if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wekipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'how are you' in query:
            speak("i am fine. sir whats about you")

        elif 'i am also fine' in query:
            speak("thats nice sir")

        elif 'prince start' in query:
            speak('''sure sir 
            your all systems and apps are ready in a few seconds''')

        elif 'tell me about yourself' in query:
            speak('''hello i am prince sir
             version 3.o 
             fully automatic virtual AI assistant
              of mr.yash jadhav
               made in inspiron
                3 thousand 5 hundread and ningty three
                 core i5
                  i was made and design by mr.yash jadhav''')

        elif 'who is your boss' in query:
            speak('''Mr. yash jadhav is my boss
                  he is programmer and a software enginner''')

        elif 'what are you doing' in query:
            speak("nothing special sir ready to help you 24*7. any order sir")

        elif 'no prince' in query:
            speak("ok sir")

        elif 'are you mad' in query:
            speak("sorry sir")

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("sir, the time is {strftime}")

        elif 'open notepad' in query:
            notepadpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories"
            os.startfile(notepadpath)
            speak("opening notepad")

        elif 'open movies' in query:
            moviespath = "D:\\MOVIES"
            os.startfile(moviespath)
            speak("opening movies")

        elif 'open ebooks' in query:
            ebookspath = "D:\\E.Books"
            os.startfile(ebookspath)
            speak("opening ebooks")

        elif 'open python projects' in query:
            pythonprojectspath = "E:\\Python Projects"
            os.startfile(pythonprojectspath)
            speak("opening python projects")

        elif 'please give me a glass of a water' in query:
            speak("sorry sir.can't do that")

        elif 'useless' in query:
            speak("sorry sir, but i can help you in technical works")

        elif 'what can you do for me' in query:
            speak("anything in your lapi sir.technical works")

        elif 'take a break' in query:
            speak('''sure sir
                  we will meet soon
                  catch you again sir 
                  please make sure that our all systems are in sleep mode
                  or it is in shutdown mode sir''')

        elif 'i am tired' in query:
            speak('''opssss
                  let me play some music for you sir
                  take a long breath and feel free''')

        elif 'wake up' in query:
            speak("yes sir i am ready")

        elif 'thanks' in query:
            speak("your most welcome sir")

        elif 'say hello to abhi' in query:
            speak("hello mr.abhi how are you")

        elif 'i am fine whats about you' in query:
            speak("i am also fine sir. thank you")

        elif 'hello Tejas' in query:
            speak("hello teju sir. how are you")

        elif 'who are you' in query:
            speak('''hello i am prince sir
             version 3.o 
             fully automatic virtual AI assistant
              of mr.yash jadhav
               made in inspiron 3 thousand 5 hundread and ningty three
                core i5
                 i was made and design by mr.yash jadhav''')

        elif 'Say Hello' in query:
            speak("Hello nice to meet you")

        elif 'temperature in' in query:
            Temperature()

        elif 'bye' in query:
            exit()






