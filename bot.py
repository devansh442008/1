greet = ["hi MR. BOT here to help","how may i help you"]
print(greet[0])
print(greet[1])
while greet != None:
    question = input()
    if question == "how are you":
        print ("\ti am fine")
        question = input()  
    if question == "close":
        exit()
        question = input()      