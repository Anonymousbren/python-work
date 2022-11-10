import pyttsx3
engine = pyttsx3.init()


text = "happy birthday to you!!!!!!!!!!!!  we wish you long life. may the good lord bless you  in anything you do"
engine.say(text)
engine.runAndWait()
engine.setProperty("rate", 2)
engine.say(text)
engine.runAndWait
engine.save_to_file(text, "python.mp3")
engine.runAndWait