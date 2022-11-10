from gtts import gTTS
import os

myText = "Welcome to Ecwa international college of technology jos..............technology for christ"

language = 'en'

output = gTTS(text=myText, lang=language, slow=False)


output.save("me.mp3")
os.system("start me.mp3")
 