import requests
import speech_recognition as sr
import subprocess
from gtts import gTTS
import pygame

bot_msg = ""
speaker_msg = ""

# Initialize pygame
pygame.mixer.init()

while bot_msg != "Bye":

    # Text to Speech
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now")
        audio = recognizer.listen(source)
        try:
            input_message = recognizer.recognize_google(audio)
            print(f"You said: {input_message}")
        except:
            print(f"Sorry, I can't recognize your voice")

        if len(input_message) == 0:
            continue

        # Getting Bot Answer
        print("Sending Your Message Now......")
        response = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": input_message})

        # Text To Speech
        print("Bot Says ... ", end='')
        for message in response.json():  # Use response.json() to get the parsed JSON content
            bot_msg = message['text']  # Access the 'text' key of each message dictionary
            print(bot_msg)
            
            my_obj = gTTS(text=bot_msg)
            my_obj.save("bot_answer.mp3")
            print('Bot Answer Saved')
            
            # Play the audio file using pygame
            pygame.mixer.music.load("bot_answer.mp3")
            pygame.mixer.music.play()

            # Wait for the audio to finish playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)


# Cleanup
pygame.mixer.quit()