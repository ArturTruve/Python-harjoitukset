from ominaisuudet import Pelaaja, Huone, Esine

# Pelaajan nimi ja hänen ikä
print()
nimi = input("Mikä sinun nimi on? ")
print()
ikä = input("Kuinka vanha olet? ")

game_state = True

# Luodaan huoneiden esineet
esine_liivi = Esine("Liivi", 5)
esine_miekka = Esine("Miekka", 7)
esine_kypärä = Esine("Kypärä", 3)
esine_aarrearkku = Esine("Aarrearkku", 28)

# Luodaan huoneet ja annetaan niille esineet
lähtö_huone = Huone("Lähtöhuone", esine_liivi)
toinen_huone = Huone("Toinen huone", esine_miekka)
kolmas_huone = Huone("Kolmas huone", esine_kypärä)
viimeinen_huone = Huone("Viimeinen huone", esine_aarrearkku)

# Lista huoneista liikkumista varten sanakirjaan
huoneet = {
    "1": lähtö_huone,
    "2": toinen_huone,
    "3": kolmas_huone,
    "4": viimeinen_huone
}

# Luodaan pelaaja olio
pelaaja = Pelaaja(nimi, [], lähtö_huone)

while game_state:
    if int(ikä) < 12:
        print("Olet alaikäinen. Peli sammutetaan.")
        game_state = False
    else:
        print()
        print(f"Tervetuloa {pelaaja.nimi}") # siirrytään valikkoon, jos käyttäjä on tarpeeksi vanha

        while game_state: # Valikko luuppaa kunnes pelaaja antaa komennon 7 tai lopeta
            print()
            print(f"Olet huoneessa: {pelaaja.sijainti.nimi}")
            print("Päävalikko: ")
            print("1. Liiku")
            print("2. Tutki huonetta")
            print("3. Listaa esineet")
            print("4. Lopeta")
            komento = input("Anna komento: ")

            if komento.lower() == "lopeta" or komento == "4": # Lopettaa ohjelman jos toteutuu
                print()
                print("Ohjelma sammutetaan.")
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