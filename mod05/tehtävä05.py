# Linkki tehtävään: https://metropolia-sw.github.io/sw1-python/fi/tehtavat.html#5-alkuehdollinen-toistorakenne-while

oikea_tunnus = "python"
oikea_salasana = "rules"

tunnus = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")

kerrat = 5

while kerrat > 0:

    if tunnus != oikea_tunnus or salasana != oikea_salasana:
        tunnus = input("Anna käyttäjätunnus: ")
        salasana = input("Anna salasana: ")
        kerrat -= 1

        