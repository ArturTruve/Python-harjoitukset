# Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

luku1 = input("Anna ensimmäinen kokonaisluku: ")
luku2 = input("Anna toinen kokonaisluku: ")
luku3 = input("Anna kolmas kokonaisluku")

luku1 = int(luku1)
luku2 = int(luku2)
luku3 = int(luku3)

print("Lukujen summa on:", luku1 + luku2 + luku3)
print("Lukujen tulo on: ", luku1 * luku2 * luku3)
print("Lukujen keskiarvo on: ", (luku1 + luku2 + luku3) / 3)