"""koira1_rotu = "noutaja"
koira1_nimi = "Jhonny"
koira1_syntymävuosi = 2000

koira2_rotu = "Lapinkoira"
koira2_nimi = "Inna"
koira2_syntymävuosi = 2019

koira3_rotu = "Labradori"
koira3nimi = "Sisu"
koira3_syntymävuosi = 2020"""

"""class Koira:
    pass

# Luokka on kuin suunnitelma. Olio on sen perusteella rakennettu yksilö

koira = Koira()
koira2 = Koira()

koira.nimi = "Jhonny"
koira.rotu = "noutaja"

koira2.nimi = "Inna"
koira2.rotu = "Lapinkoira"

print(f"Ensimmäisen koiran nimi: {koira.nimi}")
print(f"Ensimmäisen koiran rotu: {koira.rotu}")

print(f"Toisen koiran nimi: {koira2.nimi}")
print(f"Toisen koiran rotu: {koira2.rotu}")"""

# Teimme juuri luokan koira ilman ominaisuuksia
# Tämän jälkeen määrittelimme ominaisuudet yksi kerrallaan == työlästä!!!

# Näin teemme oikeasti:
# Oliossa määritellään ns. tieto ja toiminta

# Koira:

# koiran ominaisuudet
# - nimi
# - rotu
# - syntymävuosi

# Koiran toiminnot
# - Hauku
# - Syö
# - Nuku

class Koira:

    # Luokkamuuttuja
    tehty = 0

    def __init__(self, nimi, rotu, syntymävuosi, haukahdus="Vuuf-Vuuf"):
        self.nimi = nimi
        self.rotu = rotu
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        self.luokitus = "nisäkäs"
        Koira.tehty += 1

    def hauku(self, kerrat):
        print(f"{self.nimi} Tervehtii sinua")
        for i in range(kerrat):
            print(self.haukahdus)

koira = Koira("Lissu", "Bokseri", 2022, "Hau Hau")
koira2 = Koira("Wuffe", "Mastiffi", 2025, "Wof Wof")
koira3 = Koira("Fifi", "Puudeli", 2025)


koira.hauku(2)
print()
koira2.hauku(3)
print()
koira3.hauku(1)


print(f"Koiran 1 nimi on: {koira.nimi} ja rotu {koira.rotu} ja syntynyt {koira.syntymävuosi}.")
print(f"Koiran 2 nimi on: {koira2.nimi} ja rotu {koira2.rotu} ja syntynyt {koira2.syntymävuosi}.")
print(f"Koiran 1 nimi on: {koira.nimi} ja rotu {koira.rotu} ja syntynyt {koira.syntymävuosi}.")
print(koira)


print(f"Koiria on nyt {Koira.tehty}")
# print(koira) - viittaus olioon, ei muuttuja

"""
players = [
    {
        "name": "player 1",
        "skill_level": 10,
        "inventory": {"map", "knife"}
    },
    {
        "name": "player 2",
        "skill_level": 20,
        "inventory": {"axe"}
    }  
]

for player in players:
    print(f"Pelaajan {player['name']} taitotaso on {player['skill_level']}, hallussa:")
    for item in player["inventory"]:
        print(f"- {item}")
"""

### Miten tämä edellinen voitaisiin kuvata luokkana
# esim. PELAAJA
print()
print("--------------------")

info2 = "Pelaajan tiedot"

class Pelaaja:
    def __init__(self, nimi, taito_taso, inventaario):
        self.nimi = nimi
        self.taito_taso = taito_taso
        self.inventaario = inventaario

    def tiedot(self):
        print(info2)
        print("Pelaajan nimi: ", self.nimi)
        print(f"Taso: ", self.taito_taso)
        print("Inventaario: ")
        for esine in self.inventaario:
            print(f"> {esine}")
        print("----------")
        pass

    def add_item(self, item):
        self.inventaario.add(item)


pelaaja1 = Pelaaja("Ulla", 10, {"kartta", "veitsi", "vasara"})
pelaaja2 = Pelaaja("Matti", 20, {"kirves"})

pelaaja1.tiedot()
pelaaja2.tiedot()

pelaaja1.add_item("Avain")
pelaaja1.tiedot()


# Pelaajan tiedot
# print(f"Pelaaja 1 nimi on: {pelaaja1.nimi} ja taso on {pelaaja1.taito_taso}.")