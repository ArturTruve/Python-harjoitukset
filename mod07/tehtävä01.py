# T1

import random

print("\n=== Noppapeli ===")
def heitä_noppaa():
    return random.randint(1,6)

silmäluku = 0
while silmäluku != 6:
    silmäluku = heitä_noppaa()
    print(silmäluku)