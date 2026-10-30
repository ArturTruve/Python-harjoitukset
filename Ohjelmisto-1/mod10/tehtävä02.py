class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.nykyinen_kerros = alin_kerros
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.numero = None

    def siirry_kerrokseen(self, kohdekerros):
        print(f"Hissi {self.numero}: siirrytään kerrokseen {kohdekerros}")
        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
            print(f"Hissi {self.numero} on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
            print(f"Hissi {self.numero} on nyt kerroksessa {self.nykyinen_kerros}")


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = []
        for i in range(hissien_lkm):
            uusi_hissi = Hissi(alin_kerros, ylin_kerros)
            uusi_hissi.numero = i + 1
            self.hissit.append(uusi_hissi)

    def aja_hissiä(self, numero, kohdekerros):
        self.hissit[numero-1].siirry_kerrokseen(kohdekerros)


h = Hissi(2, 12)
h.numero = 1
h.siirry_kerrokseen(10)
h.siirry_kerrokseen(h.alin)
print()
talo = Talo(0, 12, 3)

talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 7)
talo.aja_hissiä(3, 8)
talo.aja_hissiä(3, 0)