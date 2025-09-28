user_input = str(input("Hi! Do you want to talk to me?\n")).strip().lower()

running = True

while running:
    if user_input != "no":
        print("That's cool!")
        user_input = str(input("What do you want to talk about?\n")).strip().lower()
    else:
        print("Alright, bye!")
        running = False
