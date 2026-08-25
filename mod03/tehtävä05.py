# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. 
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

# Esimerkki arvot: 3, 9 ja 13,5

# Ensin kysytään määrät
leiviskät = input("Anna leviskät: ")
naulat = input("Anna naulat: ")
luodit = input("Anna luodit: ")

# Lasketaan grammoiksi annetut arvot
leiviskä = (float(leiviskät) * 20 * 32 * 13.3)
naula = (float(naulat) * 32 * 13.3)
luoti = float(luodit) * 13.3

# Muutetaan grammat kilogrammoiksi ja lasketaan grammat
kilogrammat = float((leiviskä + naula + luoti) // 1000)
grammat = float((leiviskä + naula + luoti) % 1000)

# Tulostetaan pyydetyllä tavalla + pyöristetään grammamäärä kahden desimaalin tarkkuuteen
print("Massa nykymittojen mukaan: ")
print(f"{kilogrammat:.0f} kilogrammaa ja {grammat:.2f} grammaa")