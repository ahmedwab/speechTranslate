import speech_recognition as sr
import pyaudio

from googletrans import Translator

translator = Translator()



r = sr.Recognizer()


def recordAudio(language):
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.listen(source, timeout=5)
        # convert speech to text
        text = r.recognize_google(audio_data)
        translation = translator.translate(text, dest=language)
        return translation.text
def translate(text,language):
    translation = translator.translate(text, dest=language)
    return translation.text