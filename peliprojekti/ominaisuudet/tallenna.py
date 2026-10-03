# Tämä funktio tallentaa pelaajan tiedot pelaajan nimeä käyttävään tiedostoon. 
def tallenna_pelaaja(pelaaja, ikä):
    pelaajan_nimi = pelaaja.nimi
    tiedoston_nimi = f"{pelaajan_nimi}_tiedot.txt"
    with open(f"peliprojekti/pelaajat/{tiedoston_nimi}", "w") as pelaajan_tiedot:
        pelaajan_tiedot.write(f"{pelaaja.nimi}\n")
        pelaajan_tiedot.write(f"{ikä}\n")
        pelaajan_tiedot.write(f"{[esine.nimi for esine in pelaaja.esineet]}\n")
        pelaajan_tiedot.write(f"{pelaaja.sijainti.nimi}\n")