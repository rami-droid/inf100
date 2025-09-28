user_input = str(input("Hi! Do you want to talk to me?\n")).strip().lower()

running = True

while running:
    if user_input != "no":
        print("That's cool!")
<<<<<<< HEAD
        user_input = str(input("What do you want to talk about?\n")).strip().lower()
=======
        user_input = str(input("Hi! Do you want to talk to me?\n")).strip().lower()
>>>>>>> 2b3c8f15c78cb651a425f8274e7ed951dc0b72c7
    else:
        print("All right, bye!")
        running = False
