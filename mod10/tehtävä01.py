# Tehtävä 1.

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.nykyinen_kerros = alin_kerros
        self.alin = alin_kerros
        self.ylin = ylin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        print(f"Siirrytään kerrokseen {kohdekerros}")
        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")




h = Hissi(2, 12)
h.siirry_kerrokseen(10)
h.siirry_kerrokseen(h.alin)