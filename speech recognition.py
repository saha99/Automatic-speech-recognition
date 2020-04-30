# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:02:36 2020

@author: Piku Saha
"""

import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
	print('say something')
	audio=r.record(source,duration=5)
	
print('You have said :')
text=r.recognize_google(audio,language='bn-IN')
print(text)
text=r.recognize_google(audio,language='hi-IN')
print(text)
text=r.recognize_google(audio,language='en-IN')
print(text)
print('it is the end')
   
     