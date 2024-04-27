import speech_recognition as sr

# initialize speech recognizer
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speek now")
    audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except:
        print(f"Sorry, I can't recognize your voice")