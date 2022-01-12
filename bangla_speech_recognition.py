# python #speechtotext
import googletrans
import speech_recognition as s
from googletrans import Translator

print(googletrans.LANGUAGES)
# create a object of Recognizer
sr = s.Recognizer()
translator = Translator()

def listen_to_audio():
    bangla_audio = s.AudioFile('DATA/audio/static_0_56258.wav')
    with bangla_audio as source:
        audio = sr.record(source)
        # sr.pause_threshold = 1
        try:
            query_bn = sr.recognize_google(audio, language='bn-BD')
            print(query_bn)
            trans_to_eng = translator.translate(query_bn, src='bn', dest='en')
            print(trans_to_eng.text)

        except Exception as e:
            print("Sorry,could you repeat it again?")


def listen_to_speech():
    with s.Microphone() as m:
        print(f'Listening......')
        audio = sr.listen(m)
        sr.pause_threshold = 1
        try:
            query_bn = sr.recognize_google(audio, language='bn-BD')
            print(query_bn)
            trans_to_eng = translator.translate(query_bn, src='bn', dest='en')
            if 'বন্ধ' in query_bn:
                exit()

            print(trans_to_eng.text)

        except Exception as e:
            print("Sorry,could you repeat it again?")


if __name__ == '__main__':
    # Listen from audio file
    # listen_to_audio()
    # Listen from real speech
    while True:
        listen_to_speech()
