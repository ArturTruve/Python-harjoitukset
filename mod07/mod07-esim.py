# Mod 07 funktio tuntiesimerkkejä

print("print() on Pythonin sisäänrakennettu funktio")

def do_nothing():
    pass

do_nothing()

"""def print_list_of_numbers():
    print(1)
    print(2)
    print(3)

print_list_of_numbers()
print_list_of_numbers()
"""

# Funktion parametrit (argumentit) ovat muuttujia, joiden arvot on käytössä funktion sisällä. 
# Ja joille syötetään arvot funktiota kutsuttaessa. 
def print_list_of_numbers(start, end):
    print(f"Tulostetaan väli: {start}, {end}")
    for i in range(start, end+1, 1):
        print(i)

print_list_of_numbers(1,5)
# funktio ilman return sanaa tai pelkkä return sana ilman määritettyä paluuarvoa palauttaa arvon: None
test_return_value = print_list_of_numbers(7,11)
print("test return value", test_return_value)

## Funktio ja paluuarvo (return)
print()
number = "01"
# int()-fuktio palauttaa annetun parametrin arvon kokonaislukutyyppisenä
print(int(number)) # "01" --> 1


# Funktio joka ei tulosta numeroita suoraan vaan palauttaa ne listamuodossa
def create_list_of_numbers(start, end):
    print(f"Tehdään lista, jossa arvot: {start}-{end}")
    number_list = []
    for i in range(start, end+1, 1):
        number_list.append(i)
    return number_list

print(create_list_of_numbers(3, 7))

list_of_numbers = create_list_of_numbers(11, 16)
#print(list_of_numbers)

###
# Lista parametrina (ks. materiaali)

def inventaario(tavarat):
    print("Sinulla on seuraavat tavarat:")
    for t in tavarat:
        print("- " + t)
    return

reppu = ["Vesipullo", "Kartta", "Kompassi"]
inventaario(reppu)
reppu.append("Linkkuveitsi")
inventaario(reppu)

### primitiiviarvoilla alkuperäinen (pääohjelma b) arvo ei muutu
def tulosta_luku(a):
    print(a)
    a = 0

b = 3
tulosta_luku(b)
tulosta_luku(b) # tulostaa edelleen 3

###############
### Vaihtuva määrä parametreja, käsitellään monikkona (kuin lista)
print()

def summa(*luvut):
    print("Syötetyt arvot: ", luvut)
    s = 0
    for l in luvut:
        s += l
    return s

print("Summa on", summa(1, 1, 1, 1, 1, 1))


########
## tehtäväesimerkkejä
import random

# T1
"""print("\n=== Noppapeli ===")
def heitä_noppaa():
    return random.randint(1,6)

silmäluku = 0
while silmäluku != 6:
    silmäluku = heitä_noppaa()
    print(silmäluku)"""

# T2
print("\n=== Noppapeli ===")
def heitä_noppaa(tahkojen_lkm):
    return random.randint(1,tahkojen_lkm)

nopan_koko = int(input("Anna nopan koko (maksimi silmäluku): "))

silmäluku = 0
while silmäluku != nopan_koko:
    silmäluku = heitä_noppaa(nopan_koko)
    print(silmäluku)