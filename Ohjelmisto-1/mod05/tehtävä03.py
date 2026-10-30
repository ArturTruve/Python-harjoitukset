# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

tila = 1
tila2 = 2
jono = []

while tila == 1:
    luku = input("Anna uusi luku: ")

    if luku != "":
        jono.append(int(luku))
        print(jono)
        pienin = min(jono)
        suurin = max(jono)

    else:
        print(f"pienin: {pienin} ja Suurin {suurin}")
        tila = tila2