# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon. 

# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, 
# syötettiinkö nimi ensimmäistä kertaa. 

# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. 
# Käytä joukkotietorakennetta nimien tallentamiseen.


nimi_lista = set()
"""nimi = input("Anna nimi: ")
nimi_lista.add(nimi)"""

while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    elif nimi in nimi_lista:
        print("Aiemmin syötetty")
    else:
        print("Uusi nimi")
        nimi_lista.add(nimi)

for nimet in nimi_lista:
    print(f"{nimet}")