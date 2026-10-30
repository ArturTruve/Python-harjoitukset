## mod 10, hissitehtävä 1 - 3 malli.

class Hissi:
    def __init__(self, nimi, alin_kerros, ylin_kerros):
        self.nykyinen_kerros = alin_kerros
        self.alin = alin_kerros 
        self.ylin = ylin_kerros
        self.nimi = nimi

    def siirry_kerrokseen(self, kohdekerros):
        print(f"Siirrytään kerrokseen {kohdekerros}")
        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
            print(f"Hissi {self.nimi} on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
            print(f"Hissi {self.nimi} on nyt kerroksessa {self.nykyinen_kerros}")


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = []
        for i in range(hissien_lkm):
            uusi_hissi = Hissi(f"numero {i+1}", alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)

    def aja_hissia(self, numero, kohdekerros):
        # esim. hissi nro 1 on listalla indeksissä 0
        print(f"Ajetaan hissiä {numero} kerrokseen {kohdekerros}")
        self.hissit[numero-1].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("Palohälytys!!!")
        # muuttuja h viittaa vuorollaan jokaiseen hissiolioon listalla 
        for h in self.hissit:
            h.siirry_kerrokseen(h.alin)

talo = Talo(2, 12, 3)

#talo.hissit[0].siirry_kerrokseen(5)
talo.aja_hissia(1, 5)
talo.aja_hissia(1, 7)
talo.aja_hissia(3, 2)
talo.aja_hissia(3, 8)

talo.palohalytys()



    

# Testejä pelkällä hissiluokalla suoraan pääohjelmasta
"""
hissi1 = Hissi("Pääaula 1", 1, 12)
hissi2 = Hissi("Henkilökunta", 5, 20)
#print(hissi1.nykyinen_kerros)
#print(hissi2.nykyinen_kerros)
hissi1.siirry_kerrokseen(8)
hissi2.siirry_kerrokseen(15)
hissi1.siirry_kerrokseen(5)
hissi1.siirry_kerrokseen(5)
hissi2.siirry_kerrokseen(5)
hissi1.siirry_kerrokseen(1)
"""