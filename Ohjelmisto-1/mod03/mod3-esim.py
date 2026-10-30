# Tuntiesimerkit 19.8.2026

teksti = "Tämä on laskukone, anna kaksi lukua."

luku = input("Anna 1. luku: ")
luku2 = input("Anna 2. luku: ")

luku = float(luku) # esim. "10.5" -> 10.5
luku2 = float(luku2)

summa = luku + luku2
#print("summa", summa)

# print("Lukujen", luku, luku2, "summa on",summa)

# sama liitosoperaatiolla (+)
summa = str(summa)
#print("summa: " + summa)

print("Lukujen " + str(luku) + " ja " + str(luku2) +" " + "summa on " + summa + ".")

uusi_kayttäjä = input("Anna nimesi:")
#print("Hauska tavata, " + uusi_kayttäjä + "!")

ikä = 21

print(f"Hauska tavata {uusi_kayttäjä} ja ikäni on {ikä}!!!!!")

pisteet = 200
pisteet = 400
print(pisteet)

merkkijono = "ulla"
#merkkijono = "9"
#merkkijono = ""
pisteet = 0

print(f"Merkkijono: {merkkijono:<20s} sijoitetaan tähän väliin")