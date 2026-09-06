# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random

summat = []

kuutioita = int(input("Anna arpakuutioiden lukumäärä: "))

for luku in range(kuutioita):
    silmäluku = random.randint(1, 6)
    summat.append(silmäluku)

print(f"Arvottujen silmälukujen summa on: {sum(summat)}")