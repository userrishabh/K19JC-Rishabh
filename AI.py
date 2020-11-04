from tkinter import * #Imports Tkinter
import sys #Imports sys, used to end the program later

from tkinter import messagebox
#import tkinter as tk
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import random
import webbrowser
import os


root=Tk()
def Start():
     
     engine=pyttsx3.init('sapi5')
     voices = engine.getProperty('voices')
     #print(voices[1].id)
     engine.setProperty('voice', voices[1].id)
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

           speak("I am Kyto, a voice assistant. Please command me so that I can help you and you can also change the voice to male")

     def takeCommand():
          #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            # r.pause_threshold = 1
            audio = r.listen(source)

        try:
           print("Recognizing...")    
           query = r.recognize_google(audio, language='en-in')
           print(f"User said: {query}\n")

        except Exception as e:
         # print(e)    
           print("Say that again please...")  
           return "None"
        return query


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
                  speak("Opening Youtube")
                  webbrowser.open("youtube.com")

            elif 'open google' in query:
                  speak("Opening Google")
                  webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                  speak("Opening Stackoverflow")
                  webbrowser.open("stackoverflow.com")   


            elif 'play music' in query:
                   music_dir = 'D:\songs'
                   songs = os.listdir(music_dir)
                   s1=random.choice(songs)
                   speak(f"playing music {s1}")
                   print(s1)    
                   os.startfile(os.path.join(music_dir, s1))

            elif 'the time' in query:
                 strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                 speak(f"Sir, the time is {strTime}")

            elif 'open dev c' in query:
                  codePath = "D:\Installed_software\dev-c\Dev-Cpp\devcpp.exe"
                  speak("opening dev c compiler")
                  os.startfile(codePath)
            elif 'about' in query:
                  speak("Hello,I am Rocky a voice assistant developed by Rishabh")
            elif 'restart' in query:
                  wishMe()
            elif 'change the voice' in query:
            
                  engine.setProperty('voice', voices[0].id)
                  speak("voice is changed to male")
                  wishMe()
            
            

        
            elif 'quit' in query:
                 speak('Thankyou sir, I hope you enjoyed the assistant')
                 exit()
      
   # root.destroy()
   # sys.exit()
   # raise SystemExit
                            
root.title("Virtual Assistant")            
B3 = Button(root, text = "Start", command = Start,font=('arial',20,'bold'),width=10)
B3.grid(row=0,column=22,columnspan=6)

 #This hides the main window, it's still present it just can't be seen or interacted with
root.mainloop() #Starts the event loop for the main window

