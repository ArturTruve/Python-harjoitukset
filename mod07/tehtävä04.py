# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan. 
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def kokonaislukuja(lista):
    x = 0
    for i in lista:
        x += i
    summa = x
    return summa


# Pääohjelma #

num_lista = [1,2,3,4,5]

tulos = kokonaislukuja(num_lista)

print("Funktion palauttama summa on: " , tulos)