# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen)
# ja tallentaa ne listarakenteeseen.

# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
# käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

kaupungit = []

for num in range(5):
    syöttö = input("Anna kaupungin nimi: ")
    kaupungit.append(syöttö)

for kaupunki in kaupungit:
    print(kaupunki)