import math

pisteet = 200
pisteet = 400
print(pisteet)

merkkijono = "ulla"
#merkkijono = "9"
#merkkijono = ""
pisteet = 0

print(f"Merkkijono: {merkkijono:<20s} sijoitetaan tähän väliin")

kokonaisluku = -9
kokonaisluku_pitkä = 12_456_123_180
liukuluku = 4.973
kompleksiluku = -4 + 2j
totuusarvo = False

print(kompleksiluku)
print(kompleksiluku.real)
print(kompleksiluku.imag)

# printataan muuttujan tyyppi
print(f"Muuttujan tyyppi voidaan tutkia {type(kompleksiluku)}")

print(f"{"vakio":6s}|{"Arvo":>6s}")
print("--------------------")
print(f"{'Pii':6s}:{math.pi:6.2f}")

# Laskutoimitukset
##################

tuloste = """

yhteenlasku (+), vähennyslasku (-)
kertolasku (*) ja jakolasku (/)
jakojäännösoperaatio (%)
pelkän kokonaisosan palauttava jakolasku (//) 
potenssiinkorotus (**)

"""

print(tuloste)

# Laskukone

# Luetaan käyttäjältä 2 lukua (str), jotka täytyy muistaa muuntaa
# Liukuluvuksi eli float ja sijoitetaan muuttujiksi

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))

yhteenlasku = luku1 + luku2
vahennyslasku = luku1 - luku2
kertolasku = luku1 * luku2
potenssiinkorotus = luku1 ** luku2 # esim 2^3
jakolasku = luku1 / luku2
kokonaisosa = luku1 // luku2
jakojäännös = luku1 % luku2

print(f"Yhteenlasku: {yhteenlasku}")
print(f"Vähennyslasku: {vahennyslasku}")
print(f"Kertolasku: {kertolasku}")
print(f"Potenssiinkorotus: {potenssiinkorotus}")
print(f"Jakolasku: {jakolasku}")
print(f"Kokonaisosa: {kokonaisosa}")
print(f"Jakojäännös: {jakojäännös}")