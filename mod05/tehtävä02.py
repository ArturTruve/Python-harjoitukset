# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. 
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuuma = 2.54

käyttäjä = float(input("Tuumia ... joista senttimetrejä: "))

while käyttäjä >= 0:
    print(f"{käyttäjä} tuumaa on {käyttäjä * tuuma} senttimetriä. ")
    käyttäjä = 0
    käyttäjä = float(input("Tuumia ... joista senttimetrejä: "))
else:
    print("En hyväksy negatiivisia lukuja. ")