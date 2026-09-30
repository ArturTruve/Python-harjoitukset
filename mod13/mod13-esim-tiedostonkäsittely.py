# mod 13 - tiedostonkäsittelyä

# datan lukeminen
with open("mod13/intro-teksti.txt") as intro_file:
    print(intro_file.read())

# datan tallentaminen
# Tässä tapauksessa tiedoston polku määritellään suhteessa projektin juurikansioon
with open("mod13/data.txt", "a") as data_tiedosto:
    data_tiedosto.write("kukkuu\n")

# datan lukeminen rivi kerrallaan
with open("mod13/data.txt", "r") as mun_data_tiedosto:
    mun_data = mun_data_tiedosto.readline()
    print("tiedoston data:", mun_data)
    mun_data = mun_data_tiedosto.readlines()
    print("tiedoston data:", mun_data)


# pelaajan tietojen tallennus (suoraan matskusta)

import json

pelaajan_tiedot = {
    "pelaaja": "Matti",
    "taso": 5,
    "varusteet": ["miekka", "kilpi", "haarniska"]
}
with open("mod13/save.json", "w") as tiedosto:
    json.dump(pelaajan_tiedot, tiedosto)

with open("mod13/save.json", "r") as tiedosto:
    data_luettu = json.load(tiedosto)
print(f"Pelaaja: {data_luettu['pelaaja']}, taso: {data_luettu['taso']}, varusteet: {data_luettu['varusteet']}")

