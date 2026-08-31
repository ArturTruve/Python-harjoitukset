# Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

# Toimii myös näin:
"""luku = 3

while luku < 1000:
    print(luku)
    luku = luku + 3"""

# Oikeaoppinen tapa:
luku = 1
while luku <= 1000:
    # Onko luku kolmella jaollinen
    if luku % 3 == 0:
        print(luku)
    luku += 1