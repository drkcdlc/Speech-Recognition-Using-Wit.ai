import speech_recognition as sr

recog = sr.Recognizer()

try:
    with sr.Microphone() as mic:
        print("Say Something")
        recog.adjust_for_ambient_noise(mic, duration=0.5)
        audio = recog.listen(mic, phrase_time_limit = 10)
        text = recog.recognize_wit(audio, key="apikeyofwitai")
        text = text.lower()
        print(text)

except sr.UnknownValueError():
    print("Wit.ai Recognition could not understand audio")
    recog = sr.Recognizer()
except sr.RequestError as e:
    print("Could not request results from wit.ai Recognition service; {0}".format(e))