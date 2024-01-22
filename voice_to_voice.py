import speech_recognition as sr
from utils.client import send
from utils.speaker import speak, speech_to_text

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            text = r.recognize_whisper(audio, model="base.en")
            print(text)
            speak(send(text))
    except KeyboardInterrupt:
        print("Disconnected")
