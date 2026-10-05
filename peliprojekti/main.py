from ominaisuudet import Pelaaja, Esine, Paikka
import os
from ominaisuudet.tallenna import tallenna_pelaaja

print()
with open("peliprojekti/tekstit/intro.txt", "r") as intro_teksti:
    intro = intro_teksti.read()
    print(intro)

with open("peliprojekti/tekstit/ohjeet.txt", "r") as ohjeet_teksti:
    print()
    ohjeet = ohjeet_teksti.read()
    print(ohjeet)

print()
nimi = input("Mikä sinun nimi on? ")

game_state = True

eka_tulpanosa = Esine("Punaisen Tulpan", 1)
toka_tulpanosa = Esine("Vihreän Tulpan", 2)
kolmas_tulpanosa = Esine("Sinisen Tulpan", 3)
neljas_tulpanosa = Esine("Keltaisen Tulpan", 4)
vaihtoehtoinen_tulpanosa = Esine("Hopeisen Tulpan", 5)
vaihtoehtoinen_tulpanosa2 = Esine("Kultaisen Tulpan", 6)

kaikki_esineet = [eka_tulpanosa, toka_tulpanosa, kolmas_tulpanosa, neljas_tulpanosa, vaihtoehtoinen_tulpanosa, vaihtoehtoinen_tulpanosa2]

niitty = Paikka("Niitty", eka_tulpanosa)
metsä = Paikka("Metsä", toka_tulpanosa)
vanha_talo = Paikka("Vanha talo", kolmas_tulpanosa)
oja = Paikka("Oja", neljas_tulpanosa)
luola = Paikka("Luola", vaihtoehtoinen_tulpanosa)
reikä = Paikka("Reikä", vaihtoehtoinen_tulpanosa2)

# Lista paikoista liikkumista varten sanakirjana
paikat = {
    "1": niitty,
    "2": metsä,
    "3": vanha_talo,
    "4": oja,
    "5": luola,
    "6": reikä
}

# Luodaan pelaaja olio ==>
if os.path.exists(f"peliprojekti/pelaajat/{nimi}_tiedot.txt"):
    rivi = open(f"peliprojekti/pelaajat/{nimi}_tiedot.txt", "r").readlines() # luetaan rivi kerrallaan ja käytetään tietoja pelaajaa luodessa
    nimi = rivi[0].strip()

    # lukee pelaajan esineet tiedostosta ja muuttaa ne listaksi
    esineet_nimet = eval(rivi[2])
    # esineet listaan laitetaan esineet jotka löytyvät pelaajan tiedoista
    esineet = []
    for e in kaikki_esineet:
        if e.nimi in esineet_nimet:
            esineet.append(e)

    sijainti_nimi = rivi[3].strip()
    for paikka in paikat.values(): # käy läpi paikat sanakirjasta. values => käydään läpi vain arvot (Paikka-oliot) eikä avaimia (1,2,3,4,5,6)
        if paikka.nimi == sijainti_nimi:
            sijainti = paikka

    pelaaja = Pelaaja(nimi, esineet, sijainti)
    
    for paikka in paikat.values():
        if paikka.esine and paikka.esine.nimi in esineet_nimet: # Jos pelaajalla on jo paikan esine, paikassa ei ole enää esinettä.
            paikka.esine = None

    print(f"\nOlemassa olevat tiedot pelaajalle: {nimi} palautetaan.")
    ikä = rivi[1].strip()
else:
    pelaaja = Pelaaja(nimi, [], niitty)
    print()
    ikä = input("Kuinka vanha olet? ")

# Tästä alkaa pääohjelma
while game_state:
    if int(ikä) < 12:
        print("Olet alaikäinen. Peli sammutetaan.")
        game_state = False
    else:
        print()
        print(f"Tervetuloa {pelaaja.nimi}")

        while game_state:
            print()
            print(f"Olet paikassa: {pelaaja.sijainti.nimi}")
            print("Päävalikko: ")
            print("1. Liiku")
            print("2. Tutki ympäristöäsi")
            print("3. Listaa esineet")
            print("4. Lopeta")
            print("5. Kasaa tulppa (tarvitset 4 osaa)")
            komento = input("Anna komento: ")

            if komento.lower() == "lopeta" or komento == "4":
                print()
                print("Tallennetaan tiedot...")
                print("\nOhjelma sammutetaan.")
                
                tallenna_pelaaja(pelaaja, ikä)
                game_state = False

            elif komento.lower() == "liiku" or komento == "1":
                print()
                pelaaja.liiku(paikat)

            elif komento.lower() == "tutki ympäristöäsi" or komento == "2":
                print()
                pelaaja.kerää_esine()

            elif komento.lower() == "listaa esineet" or komento == "3":
                print()
                pelaaja.listaa_esineet()

            # Kun pelaaja on kerännyt 4 osaa, peli päättyy ja haluussa olevista osista riippuen saadaan eri lopetus
            elif komento.lower() == "kasaa tulppa" or komento == "5":
                if len(pelaaja.esineet) >= 4:
                    print()
                    print("Tallennetaan tiedot...")
                    print()
                    pelaajan_esineet_nimet = [e.nimi for e in pelaaja.esineet]
                    on_hopeinen = "Hopeisen Tulpan" in pelaajan_esineet_nimet
                    on_kultainen = "Kultaisen Tulpan" in pelaajan_esineet_nimet

                    if on_hopeinen and on_kultainen:
                        tiedosto = "peliprojekti/tekstit/super_voitto.txt"
                    elif on_kultainen:
                        tiedosto = "peliprojekti/tekstit/kultaa_voitto.txt"
                    elif on_hopeinen:
                        tiedosto = "peliprojekti/tekstit/pelaaja_voittaa_luola.txt"
                    else:
                        tiedosto = "peliprojekti/tekstit/pelaaja_voittaa.txt"

                    with open(tiedosto, "r") as loppu_teksti:
                        print(loppu_teksti.read())
                    
                    tallenna_pelaaja(pelaaja, ikä)
                    game_state = False
                else:
                    print(f"\nTulpan osia vielä puuttuu. Sinulla on {len(pelaaja.esineet)}/4 osaa.")