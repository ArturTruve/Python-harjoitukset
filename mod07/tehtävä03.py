# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina 
# ja palauttaa paluuarvonaan vastaavan litramäärän.

# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.

def gallonista_litraan():
    galloni = gallon_määrä
    litra = galloni * 3.785
    return litra

while True:
    gallon_määrä = float(input("Anna gallonmäärä: "))
    if gallon_määrä >= 0:
        print(f"{gallon_määrä} gallonia on {gallonista_litraan():.2f} litraa. ")
    else:
        break