## sovellettuja tehtävä esimerkkejä
import random

# T1 + T2 + EXTRA
def heitä_noppaa(tahkojen_lkm):
    return random.randint(1,tahkojen_lkm)


def noppapeli():
    print("\n=== Noppapeli ===")
    nopan_koko = int(input("Anna nopan koko (maksimi silmäluku): "))
    silmäluku = 0
    heittolaskuri = 0
    while silmäluku != nopan_koko:
        heittolaskuri += 1
        silmäluku = heitä_noppaa(nopan_koko)
        print(silmäluku)
    print(f"Heitettäessä {nopan_koko}-tahkoista noppaa, meni {heittolaskuri} heittoa, jotta saatiin {nopan_koko}")


# Sovelluksen Päävalikko, ns. main loop, josta voidaan käynnistää eri alaohjelmia!
while True:
    komento = input("Anna komento>> ")
    if komento == "lopeta":
        print("heippa")
        break
    if komento == "noppa":
        noppapeli()
    else:
        print("en ymmärtänyt!")