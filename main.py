import openai
import speech_recognition as sr
import gtts
from playsound import playsound

openai.api_key = "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"

# r = sr.Recognizer()

# mic = sr.Microphone(device_index=1)
# # https://realpython.com/python-speech-recognition/
# with mic as source:
#     audio = r.listen(source)
#     r.recognize_google(audio)


tts = gtts.gTTS("Hello world")
tts.save("hello.mp3")
playsound("hello.mp3")