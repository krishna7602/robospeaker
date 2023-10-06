import os
import pyttsx3
  

engine = pyttsx3.init()
  

try:
    command = (input("enter:"))
    engine.say(f"{command}, have a great day")
    engine.runAndWait()

except:
    engine.say("it has some error!please check it out! have a great day")
    engine.runAndWait()