import speech_recognition as sr
from gtts import gTTS
import os 
import playsound


r = sr.Recognizer()
language = 'en'
while True:
    with sr.Microphone() as source:
        print('microphone')
        audio = r.listen(source)
    try:
        print("Speech was: " + r.recognize_google(audio))
        mytext = r.recognize_google(audio)
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("output.mp3")
        playsound.playsound("output.mp3")
    except LookupError:
        print('Speech not understood')