import random as rand
import math as math
from time import sleep

deck = [x+1 for x in range(13) for y in range(4)]

rand.shuffle(deck)
counter = 0
while len(deck) != 0:

    pickedcard = rand.randint(1,13)
    curretcard = deck.pop()
    print(f"Wybrana karta: {pickedcard} -- Wylosowana karta: {curretcard} : iteracja: {counter}")
    if curretcard == pickedcard:
        print("Wylosowałeś wybraną karte: BRAWO!!1")
    else:
        print("Wylosowana karta nie jest prawidłowa: :C:C:C:")
        deck.insert(rand.randint(0,math.fabs(len(deck)-1)),pickedcard)
    counter +=1
    sleep(0.4)
