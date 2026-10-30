print()
class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

auto = Auto("ABC-123", "142")

print(f"Auton rekisteri tunnus: {auto.rekisteritunnus}")
print(f"Auton huippunopeus: {auto.huippunopeus}")
print(f"Auton tämänhetkinen nopeus: {auto.tämänhetkinen_nopeus}")
print(f"Auton juljettu matka: {auto.kuljettu_matka}")