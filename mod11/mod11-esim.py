# mod 11 - perintä - esimerkkejä

class Elain:

    # staattinen eli luokkamuuttuja, jonka arvo on yhteinen kaikille olioille
    elainten_lkm = 0

    def __init__(self, nimi, paino, synt_aika):
        self.nimi = nimi
        self.paino = paino
        self.synt_aika = synt_aika
        Elain.elainten_lkm += 1

    def liiku(self):
        print(f"{self.nimi} liikkuu jotenkin johonkin.")

    def kaikki_tiedot(self):
        print(f"Nimi: {self.nimi}, paino: {self.paino/1000} kg, syntymäaika: {self.synt_aika}")

# Jotkut eläinlajit voivat olla myös petoja
class Peto:
    def __init__(self, on_metsastaja):
        self.on_metsastaja = on_metsastaja

# Tässä esimerkissä ilves ei olekkaan peto
class Ilves(Elain):
    def kilju(self):
        print(f"Ilves nimeltä {self.nimi} kiljuu!")

    def kaikki_tiedot(self):
        print("\nIlves")
        super().kaikki_tiedot()


# Karhu perii kaksi luokkaa (moniperintä)
class Karhu(Elain, Peto):

    def __init__(self, nimi, paino, synt_aika, on_horroksessa, on_metsastaja):
        self.on_horroksessa = on_horroksessa
        # Koska konstruktori "ylikirjoitetaan", 
        # tarvitsee yliluokka konstruktoria kutsua erikseen, jos sitä haluaa hyödyntää
        super().__init__(nimi, paino, synt_aika) # super() viittaa vain ensin perittävään luokkaan
        # voidaan käyttää myös suoraan yliluokan nimeä:
        # --> Elain.__init__(self, nimi, paino, synt_aika)
        # muiden perittävien luokkien konstruktoreihin viitataan aina luokan nimellä
        # Huom: vaatii myös "self"-parametrin
        Peto.__init__(self, on_metsastaja)

    def karju(self):
        print(f"Karhu nimeltä {self.nimi} karjuu!")

    def liiku(self):
        print(f"Karhu {self.nimi} möyrii eteenpäin.")

    def kaikki_tiedot(self):
        print(f"\nKarhu on metsästäjä: {self.on_metsastaja}, joka on nyt talviunilla: {self.on_horroksessa}")
        super().kaikki_tiedot()


# Eläintarha eläimiä varten (assosiaatioesimerkki)
class Elaintarha:
    def __init__(self, nimi="nimetön"):
        self.nimi = nimi
        self.elaimet = []

    def lisaa_elain(self, elain):
        self.elaimet.append(elain)

    def listaa_kaikki(self):
        print(f"\nEläintarhan {self.nimi} kaikki eläimet ({len(self.elaimet)} kpl)")
        print("=================================")
        for elain in self.elaimet:
            elain.kaikki_tiedot()
            print("---")



uusi_elain = Elain("Joku elukka", 1500, 20250921)
# uusi_elain.liiku()

ilves1 = Ilves("Ilveskissa", 6500, 20230621)
# ilves1.liiku()
# ilves1.kilju()

karhu1 = Karhu("Nalle", 155000, 20200812, False, True)
# karhu1.karju()
# karhu1.liiku()
# print(karhu1.on_horroksessa)

tarha = Elaintarha("Korkeasaari")
tarha.lisaa_elain(ilves1)
tarha.lisaa_elain(karhu1)
tarha.lisaa_elain(Karhu("Isonalle", 205000, 20210411, True, True))

tarha.listaa_kaikki()

# Staattiseen muuttujaan viitataan 
print(f"Eläimiä luotu yhteensä: {Elain.elainten_lkm}")