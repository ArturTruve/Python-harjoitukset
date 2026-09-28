class Vihollinen:
    def __init__(self, nimi, taso):
        self.nimi = nimi
        self.taso = taso

    def huuda(self):
        print(f"{self.taso}. tasoinen {self.nimi} huutaa: RAAAHHHHH")