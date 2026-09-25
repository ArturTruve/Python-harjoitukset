print()
class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.tämänhetkinen_nopeus += muutos
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0


    def kulje(self, tuntimäärä):

        self.kuljettu_matka += self.tämänhetkinen_nopeus * tuntimäärä


class Sähköauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko




auto = Auto("ABC-123", 142)

print(f"Auton rekisteri tunnus: {auto.rekisteritunnus}")
print(f"Auton huippunopeus: {auto.huippunopeus}")
print(f"Auton tämänhetkinen nopeus: {auto.tämänhetkinen_nopeus}")
print(f"Auton juljettu matka: {auto.kuljettu_matka}")
print()


# Kiihdytä!!!!
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"Auton nopeus kiihdytyksen jälkeen: {auto.tämänhetkinen_nopeus}")
auto.kulje(1.5)
print(f"Kuljettu matka 1.5h jälkeen on: {auto.kuljettu_matka}")

auto.kiihdytä(-200)
print(f"Auton nopeus jarrutuksen jälkeen: {auto.tämänhetkinen_nopeus}")


# Sähköauto ja polttomoottoriauto

sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.kiihdytä(90)
polttomoottoriauto.kiihdytä(100)

sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print()
print("--- Sähköauto ja polttomoottoriauto ---")
print(f"Sähköauto {sähköauto.rekisteritunnus} kulki {sähköauto.kuljettu_matka} km")
print(f"Polttomoottoriauto {polttomoottoriauto.rekisteritunnus} kulki {polttomoottoriauto.kuljettu_matka} km")