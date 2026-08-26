# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

print("Sinun biologinen sukupuoli")
sukupuoli = input("mies tai nainen: ")
hemo_arvo = float(input("Mikä on hemoglobiiniarvosi (g/l): "))

if sukupuoli == "nainen":
    if hemo_arvo < 117:
        print("Hemoglobiini arvosi on alhainen. ")
    elif 117 < hemo_arvo < 175:
        print("Hemoglobiini arvosi on normaali. ")
    elif hemo_arvo > 175:
        print("Hemoglobiiniarvosi on korkea. ")

if sukupuoli == "mies":
    if hemo_arvo < 134:
        print("Hemoglobiini arvosi on alhainen. ")
    elif 134 < hemo_arvo < 195:
        print("Hemoglobiini arvosi on normaali. ")
    elif hemo_arvo > 195:
        print("Hemoglobiiniarvosi on korkea. ")