# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan. 
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

piiri = (kanta + korkeus) * 2
pinta_ala = kanta * korkeus



print(f"Suorakulmion piiri on: {piiri:.2f} ja pinta-ala {(kanta * korkeus):.2f}")