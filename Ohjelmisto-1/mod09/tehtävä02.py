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

auto.kiihdytä(-200)
print(f"Auton nopeus jarrutuksen jälkeen: {auto.tämänhetkinen_nopeus}")
