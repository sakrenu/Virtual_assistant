
import speech_recognition as sr #to recognise speech
import playsound  #to play audio
import random
from gtts import gTTS #google text to speech
import webbrowser
import ssl
import certifi
import win32api
import os
import time
import subprocess
from PIL import Image
import pyautogui
import pyttsx3
import bs4 as bs
import datetime
import pythoncom
import pywintypes
from PIL import Image
from gtts import gTTS
#import parser
class person:
    name=''
    def setName(self,name):
        self.name=name
class asis:
    name=''
    def setName(self,name):
        self.name=name
def there_exists(terms):
    for  term in terms:
        if term in voice_data:
            return True

#def engine_speak(text):
 #   text=str(text)
  #  engine.say(text)
   # engine.runAndWait()

r=sr.Recognizer()
def record_audio(ask=""):
    with sr.Microphone() as source:
        if ask:
            #engine_speak(ask)
            speak(ask)
        audio=r.listen(source, 5, 5)
        print("done listening")
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:  # error: recognizer does not understand
            #engine_speak('I did not get that')
            speak("i did not get that")
        except sr.RequestError:
            #engine_speak('Sorry, the service is down')  # error: recognizer is not connected
            speak('sorry, the service is down')
        print(">>", voice_data.lower())  # print what user said
        return voice_data.lower()

def speak(audio):
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()
"""""
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(asis_obj.name + ":", audio_string) # print what app said
    os.remove(audio_file) # remove audio file
"""

def respond(voice_data, time=time):
    # 1: greeting

    if there_exists(['hey','hi','hello','whats up']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        #engine_speak(greet)
        speak(greet)

    if there_exists(["tell me a joke"]):
        jokes=["What do you call a bear with no feet?       a gummy bear.", " what so you do when you put a vest on an aligator?          An investigator"]
        jk=jokes[random.randint(0,len(jokes)-1)]
        speak(jk)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
           #engine_speak("whats with my name ")
            speak("whats with my name")
        else:
            #engine_speak("i dont know my name . what's your name?")
            speak("i dont know my name . what's your name?")
    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        #engine_speak("okay, i will remember that " + person_name)
        speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name) # remember name in person object

    if there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        speak("okay, i will remember that my name is " + asis_name)
        #engine_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name) # remember name in asis object

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        speak("I'm doing great , thanks for asking. hope you are good too " + person_obj.name)
        #engine_speak("I'm very well, thanks for asking " + person_obj.name)

    # 4: time

    if there_exists(["what's the time","tell me the time","what time is it","time"]):
        time = time.ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        #engine_speak(time)
        speak(time)
    #date
    if there_exists(["today's date", "Date","what is todays date"]):
        year = int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        date = int(datetime.datetime.now().day)
        speak(date)
        speak(month)
        speak(year)
        print(date)

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        speak("here is what i found for "+ search_term+"on google")
       # engine_speak("Here is what I found for" + search_term + "on google")



    # 6: search youtube
    if there_exists(["youtube", 'open youtube']):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        speak("here is what i  found for "+ search_term+"on youtube")
      #  engine_speak("Here is what I found for " + search_term + "on youtube")

    #7: get stock price
    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
       # engine_speak("Here is what I found for " + search_term + " on google")
        speak("Here is what I found for " + search_term + " on google")
    # search for music
    if there_exists(["play music"]):
        search_term= voice_data.split("for")[-1]
        url="https://open.spotify.com/search/"+search_term
        webbrowser.get().open(url)
        speak("you are listening to"+ search_term+"enjoy")
      #  engine_speak("You are listening to"+ search_term +"enjoy sir")

    #search for amazon.com
    if there_exists(["amazon.com", "open amazon","amazon"]):
        search_term = voice_data.split("for")[-1]
        #url="https://www.amazon.in/"+search_term
        url="https://www.amazon.in/"+search_term
        webbrowser.get().open(url)
        #engine_speak("here is what i found for"+search_term + "on amazon.com")
        speak("hey i found for "+search_term+"on amazon.com")

    #make a note
    if there_exists(["make a note","take a note"]):
        search_term=voice_data.split("for")[-1]
        url="https://keep.google.com/#home"
        webbrowser.get().open(url)
        #engine_speak("Here you can make notes")
        speak(" you can make notes here.")

    #open instagram
    if there_exists(["open instagram","want to have some fun time"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.instagram.com/?hl=en"
        webbrowser.get().open(url)
       # engine_speak("opening instagram")
        speak("opening instagram")

    #open twitter
    if there_exists(["open twitter","twitter"]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/"
        webbrowser.get().open(url)
        #engine_speak("opening twitter")
        speak("opening twitter")

    if there_exists(["whatsapp"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.whatsapp.com/"
        webbrowser.get().open(url)
        speak("opening whatsapp")

    if there_exists(["open iris"]):
        search_term=voice_data.split("for")[-1]
        url="https://iris.nitk.ac.in/"
        webbrowser.get().open(url)
        speak("here you go with iris.")


    #8 time table
    if there_exists(["show my time table"]):
        im = Image.open(r"C:\Users\sakshi\Desktop\test.png")
        im.show()

    #9 weather
    if there_exists(["weather","tell me the weather report","whats the condition outside"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        #engine_speak("Here is what I found for on google")
        speak("Here is what I found for on google")

    #open gmail
    if there_exists(["open my mail","gmail","check my email"]):
        search_term = voice_data.split("for")[-1]
        url="https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        #engine_speak("here you can check your gmail")
        speak("here you can check your gmail")

    if there_exists(["capture","my screen","screenshot"]):
        time.sleep(3)
        speak("capturing screenshot in 3 seconds.")
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('screen.png')
        myScreenshot.show()


    #10 stone paper scisorrs

    if there_exists(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves=["rock", "paper", "scissor"]

        cmove=random.choice(moves)
        pmove=voice_data


        #engine_speak("The computer chose " + cmove)
        speak("The computer chose " + cmove)
        #engine_speak("You chose " + pmove)
        speak("You chose " + pmove)
        #engine_speak("hi")
        if pmove==cmove:
            #engine_speak("the match is draw")
            speak("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            #engine_speak("Player wins")
            speak("plyer wins")
        elif pmove== "rock" and cmove== "paper":
            #engine_speak("Computer wins")
            speak("computer wins")
        elif pmove== "paper" and cmove== "rock":
            #engine_speak("Player wins")
            speak("player wins")
        elif pmove== "paper" and cmove== "scissor":
            #engine_speak("Computer wins")
            speak("computer wins")
        elif pmove== "scissor" and cmove== "paper":
            #engine_speak("Player wins")
            speak("player wins")
        elif pmove== "scissor" and cmove== "rock":
            #engine_speak("Computer wins")
            speak("computer wins")

    #11 toss a coin
    if there_exists(["toss","flip","coin","flip a coin"]):
        moves=["head", "tails"]
        cmove=random.choice(moves)
        #engine_speak("The computer chose " + cmove)
        speak("The computer chose " + cmove)

    if there_exists(["exit", "quit", "goodbye","bye", "ok bye","bye see you" , "stop","shut up"]):
        #engine_speak("we could continue more sir, but.,,...,,,,,..,,,,, byee")
        speak("had a great time with you and I'd be more than willing to assist you anythime")
        exit()



    if there_exists(["definition of"]):
        definition=record_audio("what do you need the definition of")
        url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                #engine_speak('im sorry i could not find that definition, please try a web search')
                speak('im sorry i could not find that definition, please try a web search')
            elif definitions[1]:
                #engine_speak('here is what i found '+definitions[1])
                speak('here is what i found '+definitions[1])
            else:
                #engine_speak ('Here is what i found '+definitions[2])
                speak('Here is what i found '+definitions[2])
        else:
                #engine_speak("im sorry i could not find the definition for "+definition)
                speak("im sorry i could not find the definition for "+definition)


    #12 calc
    if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            #engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
            speak(int(voice_data.split()[3]) + int(voice_data.split()[2]))
        elif opr == '-':
            #engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
            speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            #engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
            speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            #engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
            speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            #engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
            speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            #engine_speak("Wrong Operator")
            speak("wrong operator")



time.sleep(1)
person_obj = person()
asis_obj = asis()
#asis_obj.name = 'Kim'
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("Recording") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond
