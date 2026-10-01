class Pelaaja:
    def __init__(self, nimi, esineet, sijainti):
        self.nimi = nimi
        self.esineet = esineet
        self.sijainti = sijainti


    def listaa_esineet(self): # Tulostaa pelaajan esineet, jos niitä on
        if not self.esineet:
            print("Sinulla ei ole esineitä.")
        else:
            print("Sinulla on seuraavat esineet:")
            for esine in self.esineet:
                print(f"- {esine.nimi}, joka on {esine.paino} kg")


    def liiku(self, huoneet): # Tulostaa liikkumis kohteet listan ja pelaajan valinta johtaa muutamaan tulokseen
        print("\n1. Lähtöhuone  2. Toinen huone  3. Kolmas huone  4. Viimeinen huone")
        valinta = input("Valitse huoneen numero (1 - 4): ")

        if valinta in huoneet: # Jos pelaajan valinta löytyy huoneet sanakirjasta edetään
            valittu_huone = huoneet[valinta]

            if valittu_huone == self.sijainti: # Jos valittu huone sama kuin nykyinen => kirjoittaa alla olevan
                print(f"\nOlet jo valitsemassasi huoneessa ({self.sijainti.nimi}).")
            else:
                self.sijainti = valittu_huone # Muuten pelaajan sijainti => valittu huone. 
                print(f"\n{self.nimi} liikkuu...")
                print(f"Siirryit huoneeseen: {self.sijainti.nimi}")
        else:
            print("Virheellinen valinta.")

    def kerää_esine(self):
        esine = self.sijainti.esine  # Haetaan pelaajan nykyisen huoneen esine
        if esine is not None:
            print(f"Löysit esineen: {esine.nimi}, joka painaa {esine.paino} kg")
            kyllä_ei = input("Haluatko kerätä esineen? (K/E): ")
            if kyllä_ei.lower() == "k":
                self.esineet.append(esine)
                self.sijainti.esine = None  # Poistetaan esine huoneesta
                print(f"{esine.nimi} on lisätty inventaarioosi.")
            else:
                print(f"Esine {esine.nimi} jäi huoneeseen.")
        else:
            print("Tässä huoneessa ei ole kerättäviä esineitä.")