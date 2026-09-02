import random
#mod 5 tehtävä 6 aloitus ja idea
#n=4n/N, jossa n on ympyrän sisään osuvat pisteet ja N kaikki arvotut pisteet
# piste on ympyrän sisällä, jos x^2+y^2<1

N = 1000 # Kaikkien pisteiden lukumäärä
n = 0 # lasketaan ympyrän sisään osuvat pisteet ja N kaikki arvotut pisteet
counter = 0

while counter < N:
    counter += 1
    # arvotaan satunnainen piste välillä -1,-1 ja 1,1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    print(f"{counter}. arvotun pisteen koordinaatit, x: {x}, y: {y}")
    if x ** 2 + y ** 2 < 1:
        n = n + 1
        print("Piste on ympyrän sisällä")

print(f"Pisteitä arvottu yhteensä {N}, joista ympyrän sisälle osui {n} kpl.")