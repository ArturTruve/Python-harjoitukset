print()
nimi = input("Mikä sinun nimi on? ")
print()
ikä = input("Kuinka vanha olet? ")
inventaario = []
suunta = []

game_state = True

def mitä_lisätään():
    esine = input("Lisää esine tai jätä tyhjäksi: ")
    while esine.lower() != "":
        inventaario.append(esine)
        esine = input("Seuraava esine, tai jätä tyhjäksi: ")
    return

def inventaarion_sisältö():
    for item in inventaario:
        print(f"- {item}")
    return

def kartta():
    suuntaan = input("Menitkö: Suoraan, Vasemmalle, Oikealle?\nTai jätä tyhjäksi\n")
    while suuntaan.lower() != "":
        suunta.append(suuntaan)
        suuntaan = input("Mihin suuntaan seuraavaksi?\nTai jätä tyhjäksi\n")
    return

def lue_kartta():
    print("Kartan mukaan olet edennyt seuraavasti: ")
    for kohta in suunta:
        print(f"{suunta.index(kohta)+1}. {kohta}")
    return

while game_state:
    if int(ikä) < 12:
        print("Olet alaikäinen. Ohjelma sammutetaan.")
        game_state = False
    else:
        print()
        print(f"Tervetuloa {nimi}")

        while game_state:   # siirrytään valikkoon, jos käyttäjä on tarpeeksi vanha
            print()
            print("Päävalikko: ")
            print("1. Lisää esine inventaarioon")
            print("2. Inventaarion sisältö")
            print("3. Kartta")
            print("4. Lue kartta")
            print("5. Lopeta")
            komento = input("Anna komento: ")

            if komento.lower() == "lopeta" or komento == "5":
                print()
                print("Ohjelma sammutetaan.")
                game_state = False
                
            elif komento.lower() == "lisää esine inventaarioon" or komento == "1":
                print()
                mitä_lisätään()

            elif komento.lower() == "inventaarion sisältö" or komento == "2":
                print()
                print("Inventaariossa on:")
                inventaarion_sisältö()

            elif komento.lower() == "kartta" or komento == "3":
                print()
                kartta()

            elif komento.lower() == "lue kartta" or komento == "4":
                print()
                lue_kartta()

