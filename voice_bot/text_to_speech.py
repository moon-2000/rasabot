import subprocess
import gtts as gTTS

my_text = "Welcome to Hla Bot"

language = "en"

my_obj = gTTS(text = my_text, lang = language)
my_obj.save("welcome.mp3")

# play the converted file
subprocess.call(['vlc', "welcome.mp3", '--play-and-exit'])