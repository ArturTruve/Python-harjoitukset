# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = float(input("Anna vuosiluku: "))

"""
if vuosi / 4 == True:
    print(f"{vuosi} on karkausvuosi.")
elif vuosi / 100 == True and vuosi / 400 == True:
    print(f"{vuosi} on karkaus vuosi. ")
else:
    print(f"{vuosi:.0f} ei ole karkausvuosi. ")
"""

if vuosi % 4 == 0 and vuosi >= 400:
    print(f"{vuosi:.0f} on karkausvuosi. ")

elif vuosi % 400 == 0:
    print(f"{vuosi:.0f} on karkausvuosi. ")

else:
    print(f"{vuosi} ei ole karkausvuosi. ")