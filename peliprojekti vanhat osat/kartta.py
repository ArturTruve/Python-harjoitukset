suunta = []

def kartta():
    suuntaan = input("Menitkö: Suoraan, Vasemmalle, Oikealle?\nTai jätä tyhjäksi\n")
    while suuntaan.lower() != "":
        suunta.append(suuntaan)
        suuntaan = input("Mihin suuntaan menit seuraavaksi?\nTai jätä tyhjäksi\n")
    return

def lue_kartta():
    print("Kartan mukaan olet edennyt seuraavasti: ")
    for kohta in suunta:
        print(f"{suunta.index(kohta)+1}. {kohta}")
    return