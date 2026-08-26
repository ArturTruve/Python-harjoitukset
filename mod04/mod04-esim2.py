# Kirjoita ohjelma, joka kysyy käyttäjältä sähkönkulutusta kilowattitunteina (kWh). 
# Ohjelman tulee laskea sähkölasku kolmen eri porrastetun hinnan mukaan ja tulostaa loppusumma.

# Linkki: https://github.com/ilkkamtk/python-tuntiesimerkit
# Sähkölaskulaskin

kulutus = float(input("\nSyötä sähkön kulutus (KWh): "))

hinta = 0

if kulutus <= 50:
    # KWh hinta on aina 10 senttiä.
    hinta = kulutus * 10

elif kulutus <= 200:
    # ensimmäiset 50 KWh 10 senttiä ja loput 8
    hinta = 50 * 10
    # ja loput 8 senttiä
    hinta = hinta + (kulutus - 50) * 8

else:
    # ensimmäiset 50 KWh 10 senttiä, seuraavat 150 8 senttiä
    # loput yli 200 KWh 6 senttiä
    hinta = 50 * 10 + 150 * 8 + (kulutus - 200) * 6

print(f"Sähkön hinta: {hinta//100:.0f},{hinta%100:.0f} euroa ")






# idea
"""
elif kulutus > 200:
    hinta = (50 * 10) + (150 * 8)
    hinta = hinta + (kulutus - 200) * 6

print(f"Sähkön hinta: {hinta/100:.0f} euroa ja {hinta%100:.0f} senttiä. ")
"""