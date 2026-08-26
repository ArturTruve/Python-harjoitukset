# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. 
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuuma = 2.54

käyttäjä = float(input("Tuumia ... joista senttimetrejä: "))

while käyttäjä >= 0:
    print(f"{tuuma * käyttäjä} centtimetriä. ")
else:
    print("Negatiivinen tuumien määrä. ")