# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista 
# paitsi että siitä on karsittu pois kaikki parittomat luvut.

# Kirjoita testausta varten pääohjelma, jossa luot listan, 
# kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

        # Funktio #
def kokonaislukuja(lista):
    uusi_lista = []
    for i in lista:
        if i % 2 == 0:
            uusi_lista.append(i)
    return uusi_lista


         # Pääohjelma #
vanha_lista = [1,2,3,4,5,6,7,8,9,10]

uusi = kokonaislukuja(vanha_lista)

print(f"Vanha lista: {vanha_lista}")
print(f"Uusi lista: {uusi}")