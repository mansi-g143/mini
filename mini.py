'''sabse pehle hame ek speak function banana padega def speak(audio) pass taki jarvis hame sun sake for that we will use "sapi5"
ye microsoft ki taraf se ek api hai in windows jo speech ko recognize karta hai taki AI kuch bole and we can eaily
recognize what ai is speaking by sapi5 we can use inbuit voice that is in windows'''

import pyttsx3 
'''pyttsx3 is a text to speech library in python 2 amd python 3 works without internet
                  supports multiple TTs engine, sapi5 etc
                   works offline '''
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser #youtube wagera open karne ke liye hamne import kiya hai ye
import os # for playing music

engine=pyttsx3.init('sapi5') #init initialize a newly created object and is a method
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# print(voices[0]) we were just checking voices


def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour) # isse hour hame mil jaega
    if hour>=0 and hour<12:
        speak('good morning')
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak('good evening')

    speak(" I am jarvis sir,Please tell me how may i help you")

def takeCommand():
    #it takes microphone input from the user and returs string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print ("listening...")
        r.pause_threshold=1
        '''used to increase the time it is basically seconds of non speaking audio before phrase is considerd
              complete for example agar ham kuch bol rahe aur ek second pause ho gye to woh kahin consider na
              kar le ki phrase khatam ho gya''' 
        audio=r.listen(source)
#all these are used from speech recognition library
    try: 
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said: (query)\n")

    except Exception as e:
        # /print(e)

        print("say that again please...")
        return "None" #return karwa rahe ham none as string 
    return query



if __name__=="__main__":
    speak("hi,sir") #speak function is used to speak taki jarvis bol pae
    #wishMe() agar wish me laga diya toh jarvis baar baar wish karega hame 
    #while True:
    if 1:
        query=takeCommand().lower() #agar isko lower mai nhi karte to maan lo google mai g captital hota toh error ata
        if wikipedia in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2) # 2 sentence return karega wikipredia se
            speak("according to wikipedia")
            print(results)
            speak("results")  # pehle wikipedia bolega according to wikipedia phir 2 lines from wikipedia
    #logic for executing task based on query
    #whike loop isiliye chalega taki loop chalta rahe jabtak exception hai


        elif 'open youtube' in query: #ab agar query mai youtube hoga to usko open karega
            webbrowser.open("youtube.com")

        elif 'open google' in query: 
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query: 
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir="p//oo//" #basically ye music directory from computer jisme hamare songs hai
            # // isiliye use kar rahe taki ham characters ko escape kar pae
            songs=os.listdir(music_dir)# listdir sare songs ki list ko print kar dega jo hamare computer pae hai
            print(songs)#sare songs dikhenge
            os.startfile(os.path.join(music_dir,songs(0))) 
            #ham ek random module ko use karke len_1 karke koi bhi ek random song bhi play kara sakte


        elif 'the time' in query:
            strtime =datetime.datetime.now().strtime("%H:%M:%S")
            speak(f"sir, the time is {strtime}")

        

        