# Tuntiesimerkkejä mod 6 - 2.9

import random

# arvotaan satunnainen piste välillä -1,-1 ja 1,1
x = random.uniform(-1, 1)
y = random.uniform(-1, 1)

piste = (x, y)

print(piste)

# tulostetaan vain ensimmäisen alkion arvo (x)
print(piste[0])

# esimerkki materiaali

nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]

print(nimet[3])
print(nimet[1])
print(nimet[-2])
print(nimet[1:3])
print(nimet[2:])
print(nimet)

lista_koko = len(nimet)
print(lista_koko)

# listan arvojen tulostaminen yksittäin while-silmukalla
counter = 0
while counter < len(nimet):
    print(f"{counter+1}. nimi: {nimet[counter]}")
    counter += 1

# Listan käsittelyä

nimet.append("Joku uusi nimi")
nimet.insert(4, "Teppo")
print(nimet, len(nimet))

# dummy todo-sovellus
todos = []
todos.append("Tee läksyt!")
new_todo = input("Anna uusi tehtävä: ")
todos.append(new_todo)

# tulostetaan listan sisältö yksittäin for-loopilla
for todo in todos:
    print(todo)
# tai käytetään range()-funktiota
for number in range(len(todos)): # 0, 1 jos len(tudos) => 2
    print(todos[number])

# range esimerkki materiaalista
for luku in range(3, 31, 3):
    print(luku)