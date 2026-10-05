class Pelaaja:
    def __init__(self, nimi, esineet, sijainti):
        self.nimi = nimi
        self.esineet = esineet
        self.sijainti = sijainti


    def listaa_esineet(self):
        if not self.esineet:
            print("Sinulla ei ole esineitä.")
        else:
            print("Olet löytänyt seuraavat esineet:")
            for esine in self.esineet:
                print(f"- {esine.nimi} numero {esine.numero}")


    def liiku(self, paikat):
        print("\n1. Niitty  2. Metsä  3. Vanha talo  4. Oja  5. Luola  6. Reikä")
        valinta = input("Valitse paikan numero (1 - 6): ")

        if valinta in paikat: # Jos pelaajan valinta löytyy paikat sanakirjasta edetään
            valittu_paikka = paikat[valinta]

            if valittu_paikka == self.sijainti:
                print(f"\nOlet jo valitsemassasi paikassa.")
            else:
                self.sijainti = valittu_paikka
                print(f"\n{self.nimi} liikkuu...")
                print(f"Siirryit paikkaan: {self.sijainti.nimi}")
        else:
            print("Virheellinen valinta.")

    def kerää_esine(self):
        esine = self.sijainti.esine
        if esine is not None:
            print(f"Löysit numero: {esine.numero}. {esine.nimi}")
            kyllä_ei = input("Haluatko kerätä tulpan? (K/E): ")
            if kyllä_ei.lower() == "k":
                self.esineet.append(esine)
                self.sijainti.esine = None
                print()
                print(f"Otit {esine.nimi} mukaasi.")
            elif kyllä_ei.lower() == "e":
                print()
                print(f"Jätit {esine.nimi} paikalleen.")
        else:
            print("Et löytänyt mitään.")