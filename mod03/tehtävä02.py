# 2. Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

import math

# pi = 3.14
# Ympyrän pinta-ala = pi * r(säde) ** 2(potenssiin)

säde = float(input("Anna ympyrän säde niin lasken ympyrän pinta-alan: "))

print(f"Ympyrän pinta-ala on: {math.pi * säde ** 2:.2f} neliömetriä")