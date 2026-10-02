from ominaisuudet import Pelaaja, Huone, Esine
import os
from ominaisuudet.tallenna import tallenna_pelaaja

# Kun ohjelma käynnistetään, tulostetaan intro teksti
print()
with open("peliprojekti/intro.txt", "r") as intro_teksti:
    intro = intro_teksti.read()
    print(intro)

# intron alle tulostetaan ohjeet pelaajalle ennen pelin alkamista
with open("peliprojekti/ohjeet.txt", "r") as ohjeet_teksti:
    print()
    ohjeet = ohjeet_teksti.read()
    print(ohjeet)

# Pelaajan nimi ja hänen ikä
print()
nimi = input("Mikä sinun nimi on? ")
print()
ikä = input("Kuinka vanha olet? ")

game_state = True

# Luodaan huoneiden esine oliot
esine_liivi = Esine("Liivi", 5)
esine_miekka = Esine("Miekka", 7)
esine_kypärä = Esine("Kypärä", 3)
esine_aarrearkku = Esine("Aarrearkku", 28)

kaikki_esineet = [esine_liivi, esine_miekka, esine_kypärä, esine_aarrearkku]

# Luodaan huoneet ja annetaan niille esineet
lähtö_huone = Huone("Lähtöhuone", esine_liivi)
toinen_huone = Huone("Toinen huone", esine_miekka)
kolmas_huone = Huone("Kolmas huone", esine_kypärä)
viimeinen_huone = Huone("Viimeinen huone", esine_aarrearkku)

# Lista huoneista liikkumista varten sanakirjana
huoneet = {
    "1": lähtö_huone,
    "2": toinen_huone,
    "3": kolmas_huone,
    "4": viimeinen_huone
}

# Luodaan pelaaja olio
if os.path.exists(f"peliprojekti/{nimi}_tiedot.txt"):   # Jos pelaajan nimellinen tiedosto löytyy,
    rivi = open(f"peliprojekti/{nimi}_tiedot.txt", "r").readlines() # luetaan se rivi kerrallaan ja käytetään tietoja pelaajaa luodessa
    nimi = rivi[0].strip()

    # lukee pelaajan esineet tiedostosta ja muuttaa ne listaksi
    esineet_nimet = eval(rivi[2])
    # esineet listaan laitetaan esineet jotka löytyvät pelaajan tiedoista
    esineet = []
    for e in kaikki_esineet:
        if e.nimi in esineet_nimet:
            esineet.append(e)

    sijainti_nimi = rivi[3].strip()
    # Etsitään tekstimuotoiselle sijainnille vastaava Huone-olio sanakirjasta
    for huone in huoneet.values(): # käy läpi huoneet sanakirjasta. values => käydään läpi vain arvot (Huone-oliot) eikä avaimia (1,2,3,4)
        if huone.nimi == sijainti_nimi:
            sijainti = huone

    pelaaja = Pelaaja(nimi, esineet, sijainti) # luodaan pelaaja olio tallennettuja tietoja käyttäen
    
    for huone in huoneet.values():
        if huone.esine and huone.esine.nimi in esineet_nimet:
            huone.esine = None

    print(f"\nOlemassa olevat tiedot pelaajalle: {nimi} palautetaan.")
else:
    pelaaja = Pelaaja(nimi, [], lähtö_huone)

while game_state:
    if int(ikä) < 12:
        print("Olet alaikäinen. Peli sammutetaan.")
        game_state = False
    else:
        print()
        print(f"Tervetuloa {pelaaja.nimi}")

        while game_state: # Valikko luuppaa kunnes pelaaja antaa komennon 4 tai lopeta
            print()
            print(f"Olet huoneessa: {pelaaja.sijainti.nimi}")
            print("Päävalikko: ")
            print("1. Liiku")
            print("2. Tutki huonetta")
            print("3. Listaa esineet")
            print("4. Lopeta")
            komento = input("Anna komento: ")

            if komento.lower() == "lopeta" or komento == "4": # Lopettaa ohjelman ja tallennetaan pelaajan tiedot
                print()
                print("Tallennetaan tiedot...")
                print("\nOhjelma sammutetaan.")
                # Pelaajan tiedot tallennetaan lopetuksen yhteydessä tekstitiedostoon
                tallenna_pelaaja(pelaaja, ikä)
                game_state = False

            elif komento.lower() == "liiku" or komento == "1":
                print()
                pelaaja.liiku(huoneet) # Kutsutaan pelaajan liiku funktiota

            elif komento.lower() == "tutki huone" or komento == "2":
                print()
                pelaaja.kerää_esine() # Kutsutaan Pelaaja kerää-esin funktiota

            elif komento.lower() == "listaa esineet" or komento == "3":
                print()
                pelaaja.listaa_esineet() # Kutsutaan Pelaajan listaa_esieet funktio