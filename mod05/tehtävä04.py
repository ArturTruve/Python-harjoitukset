# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. 
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.

# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

kone = random.randint(1,10)

arvaus = int(input("Arvaa 1 ja 10 väliltä: "))

while arvaus != kone:

    if arvaus < kone:
        print("Liian pieni arvaus")

    elif arvaus > kone:
        print("Liian suuri arvaus")

    arvaus = int(input("Arvaa uudelleen: "))

print("Oikein")