# Mod 8 esimerkkejä 9.9.2026

viikonpaivat = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
print(viikonpaivat)
print("ensimmäinen viikonpäivä", viikonpaivat[0])

# monikko monikon sisällä (kaksi- tai moniulotteisesta monikosta)
print("\narkipäivät ja viikonloppu päivät ovat omissa monikoissa monikossa:")
viikonpaivat_v2 = (("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai"), ("lauantai", "sunnuntai"))
print(viikonpaivat_v2)
print("arkipäivät ovat", viikonpaivat_v2[0])
print("viikonlopun päivät ovat", viikonpaivat_v2[1])
print("ensimmäinen arkipäivä on", viikonpaivat_v2[0][0])

# monikon yksittäisten arvojen purku erillisiin muuttujiin

(eka, toka, kolmas, neljäs, viides, kuudes, seitsemäs) = viikonpaivat
print(eka, toka, kolmas, viides, seitsemäs)

## monikko ja funktio (muokattu esimerkki materiaalista)
print("\nTuplanoppa")

import random

def heitä():
    # luodaan kaksialkioinen monikko ja palautetaan se suoraan
    return (random.randint(1, 6), random.randint(1, 6))

nopat = heitä()
#print(nopat)
print(f"Nopista tuli {nopat[0]} ja {nopat[1]}.")

################
## joukko (set)
print("\nJoukkoja")
viikonpaivat = {"maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai"}
print(viikonpaivat)

# saman arvon voi esiintyä joukossa vain kerran (arvot on uniikkeja)
viikonpaivat.add("extrapäivä")
viikonpaivat.add("extrapäivä")
for paivä in viikonpaivat:
    print(paivä)
viikonpaivat.remove("keskiviikko")
# kaatuu jos viitataan arvoon, mitä ei ole
#viikonpaivat.remove("jotainmitäeiole")
print(viikonpaivat)

########################
# Sanakirja (dictionary)
print("\nSanakirjaesimerkkejä")

numerot = {"Viivi": "050-1234567",
           "Ahmed": "040-1112223",
           "Pekka": "050-7654321"}

numerot["Olga"] = "050-1011012"
numerot["Mary"] = "0401-2132139"

# sanakirjan arvoihin viitataan avaimella, joka on uniikki
numerot["Pekka"] = "poistettu"
# sama arvo voi toistua
numerot["Ahmed"] = "050-1234567"

print(numerot)
print("Olgan numero on", numerot["Olga"])

#nimi = input("Anna nimi: ")
nimi = "Pekka"
# if-lauseella voi testata, esiintyykö avain sanakirjassa
if nimi in numerot:
    print(f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}.")

####
# Sisäkkäiset tietorakenteet
print("\nEsimerkki pelaajien mahdollisesta tietorakenteesta jossain moninpelissä")

players = [
    {
        "name": "player 1",
        "skill_level": 10,
        "inventory": {"map", "knife"}
    },
    {
        "name": "player 2",
        "skill_level": 20,
        "inventory": {"axe"}
    }  
]

# Tulostetaan pelaajien tiedot
#print(players)
for player in players:
    #print(player)
    print(f"Pelaajan {player['name']} taitotaso on {player['skill_level']}, hallussa:")
    for item in player["inventory"]:
        print(f"- {item}")