import random

print("\n=== Noppapeli ===")
def heitä_noppaa(tahkojen_lkm):
    return random.randint(1,tahkojen_lkm)

nopan_koko = int(input("Anna nopan koko (maksimi silmäluku): "))

silmäluku = 0
while silmäluku != nopan_koko:
    silmäluku = heitä_noppaa(nopan_koko)
    print(silmäluku)