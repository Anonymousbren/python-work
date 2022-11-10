import random
import PyAutoGUI


chars = "abcdefghijklmnopqrstuvwxyz1234567890"
chars_list = list(chars)

password = pyautogui.password("enter your password: ")

guess_password = ""
while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))
    
    print("<==========" + str(guess_password)+ "=============>")
    if(guess_password == list(password)):
        print("your password is:"+ "".join(password))