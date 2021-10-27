import random

while 1 == 1:
    randNum = random.randint(1,100)

    u = int(input("Guess the number: "))
    if u > randNum:
        print("Too High")
    elif u < randNum:
        print("Too Low")
    elif u == randNum:
        print("You're a witch!")
    else:
        print("Error. Please guess a number")