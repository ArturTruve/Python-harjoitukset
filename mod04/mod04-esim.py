# Tuntiesimerkkejä moduulin 4

## Kolikonheittosimulaattori
import random
random_number = random.randint(0,1)
""" 
kolikko = random.randint(0,1)

if kolikko == 0:
     print(f"Kolikko on {kolikko}")
elif kolikko == 1:
     print(f"Kolikko on {kolikko}")
"""

print(random_number)

# if lauseen _enhto_ muodostuu AINA True tai False arvoksi
# Jos ehto on tosi suoritetaan if lohko, muuten suoritetaan else lohko
if random_number == 0:
    result = "kruuna"
    print("kruuna tuli")
else:
    result = "klaava"

"""
if random_number == 1:
    result = "klaava"
"""

print(f"Heitit kolikon ja sait {result}n.")

# boolean
"""
onko_totta = False
if onko_totta:
    print("Onhan se totta!")
"""

## Kolikonheittosimulaattori 2.0
# kolikko pystyy tod.näk. oikeasti jotain 1/6000 luokkaa?
random_number = random.random()
print(random_number) # liukulukuarvo väliltä 0-1

# kolikko jää pystyyn todennäköisyys 1/100
if random_number < 0.01:
    print("Kolikko jäi pystyyn")
elif random_number < 0.505:
    print("Kruuna tuli.")
else:
    print("Klaava tuli")

## erilaisia ehtoja

arvo = 150

print(90 < arvo < 110)
print(100 != 101)

# kalvoesimerkki

ikä = int(input("Anna ikä: "))
if 15 <= ikä < 18:
    paino = float(input("Anna paino (kg): "))
if ikä >= 18 or (ikä >= 15 and paino >= 55):
    print("Lääkkeen käyttö on sallittua.")


# esimerkki ehdoista (jälkimmäinen if-lause) ikäarvolla 18
# print(True or (True and False))

print(not True)