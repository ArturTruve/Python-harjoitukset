print("Kuinka pitkä kuhasi on? ")
pituus = float(input("cm: "))

puute = 37 - pituus

if pituus < 37:
    print("Laske kuha takaisin järveen.")
    print(f"Kuha on {puute:.2f} cm liian lyhyt.")
else:
    print("Saat pitää kuhan.")