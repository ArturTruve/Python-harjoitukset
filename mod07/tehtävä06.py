import math

def calculate_unite_price(diameter_in_cm, price):

    # pinta-ala: pi * r^2
    r = diameter_in_cm / 100 / 2
    area = math.pi * r**2
    # palautetaan yksikköhinnan eur/m2
    return price / area

unit_prices = []
for pizza_number in range(2):

    diameter = float(input(f"Anna {pizza_number+1}. pizzan halkaisija (cm): "))
    price = float(input(f"Anna {pizza_number+1}. pizzan hinta (eur): "))
    unit_price = (calculate_unite_price(diameter, price))
    unit_prices.append(unit_price)
    print(f"{pizza_number+1}Pizzan yksikköhinta (eur/m2): {unit_price:0.2f}")

if unit_prices[0] < unit_prices[1]:
    print("Ensimmäinen pizza on halvempi.")
elif unit_prices[0] > unit_prices[1]:
    print("Toinen pizza on halvempi.")
else:
    print("Yhtä halpoja.")

# TODO EXTRA: miten laajentaa ohjelmaa niin, että se toimii N määrällä pizzoja?
# 
