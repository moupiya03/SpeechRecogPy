import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_voice():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening >>>")
        r.pause_threshold=1
        audio= r.listen(source)
    try:
        print("recognizing >>>")
        query=r.recognize_google(audio, language= 'en-in')
        print("user said :",query)
    except Exception as e:
        print("Sorry, Say that again please...")
        return "none"
    return query

def wish():
    speak("Loading boot menu,    all systems check,    analysing required files,    Ok I am Online")    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning User")
    elif hour>=0 and hour<16:
        speak("Good Afternoon User")
    else:
        speak("Good Evening User")
    speak("Hello welcome to this project, how may I help you")
        
def create():
    name=input("Enter a file name : ")
    speak("Enter our desired location to save the file")
    dir=input("Enter our desired location to save the file : ")
    file=open(f"{dir}:\\{name}",'a')
    speak("Sir please write your thoughts below")
    print("Write our thoughts below -> ")
    Str1=input("Enter lines : ")
    file.write(Str1)
    speak(f"Sir, the content has been saved in desired file in your {dir} Drive.")

if __name__ == "__main__":
    wish()
    while True:
        query= take_voice().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query, sentences=5)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'facebook' in query:
            webbrowser.open("facebook.com")
        elif 'according to google' in query:
            query1=query.replace("according to google","")
            webbrowser.open(f"www.google.com/{query1}")

        elif 'time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak('Sir, the current time is')
            speak(time)

        elif 'create' in query:
            create()
            
        elif 'exit'or'close'or'shut down' in query:
            exit()
