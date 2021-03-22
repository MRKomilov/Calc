from translate import Translator
import speech_recognition as sr
from gtts import gTTS

def main():
   
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        print('...')
        audio = r.listen(source)
    a = r.recognize_google(audio, language = 'uz-UZ')
    print('UZB: ', a)

    translator= Translator(from_lang="uzbek",to_lang="english")
    trans = translator.translate(a)


    print('ENG: ',trans)

    #language = 'eng'
    #output = gTTS(text=trans, lang=language, slow=False)
    #output.save("output.mp3")
    #os.system("start output.mp3")

for i in range(5):
    main()
