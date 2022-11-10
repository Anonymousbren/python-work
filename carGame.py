command = ""

while command.lower() != "quit":
    command = input("> ") 
    if command.lower() == "start":
        print("car started.......")
    elif command == "stop":
        print("car stopped")
    elif command == "help":
        print(''''
    start - to satrt the car
    stop - to stop the car
    quit - to  quit
        
        
        ''')
    elif command == "quit":
        break
    else:
        print("sorry bro are u drunk i dont understand you")
    