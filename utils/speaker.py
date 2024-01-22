import pyttsx3
import whisper

model_whisper = whisper.load_model("base.en", device="cpu")
engine = pyttsx3.init()


def speech_to_text(audio) -> str:
    result = model_whisper.transcribe(audio, fp16=False)
    return result["text"]


def speak(word):
    engine.setProperty('rate', 135)
    engine.setProperty('volume', 1)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(str(word))
    engine.runAndWait()
    engine.stop()
