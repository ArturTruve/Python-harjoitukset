nimi = input("Mikä sinun nimi on? ")
ikä = input("Kuinka vanha olet? ")

game_state = True

while game_state:
    if int(ikä) < 12:
        print("Olet alaikäinen. Ohjelma sammutetaan.")
        game_state = False
    else:
        print(f"Tervetuloa {nimi}")

        while game_state:   # siirrytään valikkoon, jos käyttäjä on tarpeeksi vanha
            print("Päävalikko: ")
            print("1. Nimi")
            print("2. Ikä")
            print("3. Lopeta")
            print("4. Vitsi")
            komento = input("Anna komento: ")

            if komento.lower() == "lopeta" or komento == "3":
                print("Ohjelma sammutetaan.\n")
                game_state = False
                
            elif komento.lower() == "nimi" or komento == "1":
                print(f"Nimesi on {nimi}\n")

            elif komento.lower() == "ikä" or komento == "2":
                print(f"Ikäsi on {ikä}\n")

            elif komento.lower() == "vitsi" or komento == "4":
                print("Miksi AMK-opiskelija haluaa ryhmätyökaverinsa arkunkantajaksi omissa hautajaisissaan?")
                print("Jotta he voivat laskea hänet alas viimeisen kerran.\n")

        

