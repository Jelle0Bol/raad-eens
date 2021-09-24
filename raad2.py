import random

score = 0
ronde = 0
hoog = 1000
laag = 1

while ronde <20:
    ronde += 1
    getal = 0
    nummer = random.randint(laag, hoog)

    print("Round", ronde)
    if ronde < 19:
        print("Nog een getal raden?")
    
    while getal < 10:
        getal += 1


        gok = int(input("Typ een nummer- "))

        if nummer == gok:
            print("Nice! hebt ",getal, " keer geraden voordat je het goed had. Je score is" , score)
        elif nummer > gok:
            print("Je hebt laag gegokt.... gok wat hoger")
        elif nummer < gok:
            print(" Je hebt hoog gegokt...... gok wat lager")

    if getal >= 10:
        print("Goed gedaan!")
        print("Bedankt voor het spelen!")
