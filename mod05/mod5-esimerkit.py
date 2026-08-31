import random

"""suorita = True

while suorita:
    print("Tämä printtaantuu vain kerran")
    suorita = False

print("Suoritus loppui")

luku = 1                # 1. alkuavro / kierrosmuuttuja

while luku <= 5:        # 2. ehto
    print(luku)
    luku += 1           # 3. muuttujan arvon muuttaminen

print("Jatketaan ohjelmaa")"""

#-------------------------------------------------------------------#

# Muuta ohjelmaa niin että tulostetaan luvut 10-1
# Muuta ohjelmaa niin että luku 10 kysytään käyttäjältä

"""luku = int(input("Anna luku josta lasketaan alaspäin: ")  )           

while luku >= 1:
    print(luku)
    luku -= 1 """

#-------------------------------------------------------------------#

# Käyttäjä lopettaa toiston

"""salasana = input("Anna salainen salasana jotta pääset sisään (python): ").strip()

while salasana != "python":
    print("Väärä salasana")
    salasana = input("Anna salainen salasana uudelleen: ")

print("Tervettuloa!!!")"""

#-------------------------------------------------------------------#

# While / Else rakenne
# Suoritus siirtyy else-haaraan kun toistoehto on epätosi
# Sitä ei suoriteta jos poistutaan break-lauseella
# Else rakenne on harvemmin käytetty

"""komento = input("Anna komento (lopeta, APUA): ").strip().lower()    # päädyssä poistaa välilyönnit ja tekee inputin pieniksi kirjaimiksi

while komento != "lopeta":
    if komento == "apua":
        break
    print("Annoit komennon: ",komento)
    komento = input("Anna uusi komento: ")
else:
    print("annoit käskyn lopeta, joten näin tehdään!!!")

print("Ohjelma jatkuu")"""

#-------------------------------------------------------------------#

"""noppa1 = noppa2 = heitot = 0

while (noppa1 != 6 or noppa2 != 6):

    noppa1 = random.randint(1,6)
    noppa2 = random.randint(1,6)
    print(f"{noppa1} {noppa2}")
    heitot = heitot + 1

print(f"Tarvittiin {heitot:d} heittoa.")"""

#-------------------------------------------------------------------#

# Sama nopanheitto uudestaan, nyt sisäkkäisellä toistorakenteella

"""eka = 1
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka*toka:d}")
        toka = toka + 1
    eka = eka + 1
"""

#-------------------------------------------------------------------#

"""pelikerta = 0
heitot = 0
while pelikerta < 1000:

    noppa1 = noppa2 = 0
    while (noppa1 != 6 or noppa2 != 6):

        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        #print(f"{noppa1} {noppa2}")
        heitot = heitot + 1

    pelikerta += 1

print(f"Pelikertoja meillä oli: {pelikerta}")
print(f"Tarvittiin {heitot:d} heittoa.")
print(f"Jokaisella kierroksella oli keskimäärn {heitot / pelikerta} heittoa")"""

#-------------------------------------------------------------------#

# Tehtävä 1.

"""luku = 1
while luku <= 1000:
    # Onko luku kolmella jaollinen
    if luku % 3 == 0:
        print(luku)
    luku += 1"""

# Tehtävä 4 modattuna

# TODO: Tee tehtävä loppuun!!!!!!!!!!!!!!!!!!!!!!!!!

"""oikea_numero = 7
arvaus = int(input("Arvaa numero 1 ja 10 välillä: "))

while arvaus != oikea_numero:
    print("VÄÄRIN")
    arvaus = int(input("Arvaa uudestaan: "))

print(f"Yes, sait kaiken oikein!!! Numero tosiaan oli {oikea_numero}")"""

# Usein while-rakennetta käytetään ja varsinkin teidän projektissa!!!
# ns. pääsilmuka ELI main loop

peli_käynnissä = True
# main loop
print("Tervettuloa peliini!!!")

while peli_käynnissä:
    print("Valitse minne mennään (j tai l) eli jatka tai lopeta")
    # j jatkaa peliä ja l lopettaa
    valinta = input("Anna komento: ")
    if valinta == "j":
        print("Jatkoit peliä")
    elif valinta == "l":
        print("Lopetit pelin")
        peli_käynnissä = False
        break

    else:
        print("Et osaa antaa käskyä!!!!")