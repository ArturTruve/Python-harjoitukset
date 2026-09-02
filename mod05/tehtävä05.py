# Linkki tehtävään: https://metropolia-sw.github.io/sw1-python/fi/tehtavat.html#5-alkuehdollinen-toistorakenne-while

oikea_tunnus = "python"
oikea_salasana = "rules"

tunnus = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")

kerrat = 4  # näin yrityksiä on 6 sijaan 5

while kerrat > 0:

    if tunnus != oikea_tunnus or salasana != oikea_salasana:
        print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.") # fiksaa miks ei tuu ekal vääräl!!!
        tunnus = input("Anna käyttäjätunnus: ")
        salasana = input("Anna salasana: ")
        kerrat -= 1
    else:
        break

if kerrat == 0:
    print("Pääsy evätty.")
else:
    print("Tervettuloa")