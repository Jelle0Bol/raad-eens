import random

num = random.randint(1,1000)
guess = None
while guess != num:
    guess = input("Nog een keer raden?: ")
    guess = int(guess)
    if guess == num:
        print ("Je hebt het geraden!")
        break
    elif guess > 1000:
        print ("Gebruik alleen getallen onder de 1000")
    elif guess > num:
        print ("Te groot")
    elif guess < num:
        print ("Te klein")
    else:
            print("gebruik alleen getallen onder de 1000")

