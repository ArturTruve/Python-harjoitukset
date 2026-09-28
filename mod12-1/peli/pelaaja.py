class Pelaaja:
    def __init__(self, nimi, taso):
        self.nimi = nimi
        self.taso = taso

    def huuda(self):
        print(f"{self.taso}. tasoinen {self.nimi} huutaa: AAAAAAA")

if __name__ == "__main__":
    pelaaja_testi = Pelaaja("Testi pelaaja", 0.00)
    pelaaja_testi.huuda()