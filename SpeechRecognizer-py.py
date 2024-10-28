import speech_recognition as sr
 
r = sr.Recognizer()
 
test = sr.AudioFile('/Users/shaojie/Desktop/1.wav')
 
with test as source:
    audio = r.record(source)

try:
    text = r.recognize_google(audio,language='zh-CN')
    print(text)
except sr.UnknowValueError:
    print('无法识别')


