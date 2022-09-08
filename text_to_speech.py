import pyttsx3
text_speech=pyttsx3.init()
answer=input("What you want to convert from text to speech: ")
text_speech.say(answer)
text_speech.runAndWait()