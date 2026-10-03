# "Veden likaajat tukkoon!"
**Artur Truve**

## Pelin idea
Pelaaja luo hahmon nimellä ja iällä, joka voi vapaasti liikkua 4 sijainnin välillä. Sijainneissa on esineitä, joita pelaaja voi kerätä halutessaan. Pelaajan tavoite on kerätä esine jokaisesta sijainnista, jonka jälkeen hän voi valikon kautta päättää pelin ja voittaa. Pelaaja voi jatkaa siitä mihin hän jäi käyttämällä samaa nimeä, jolla hän ennen pelasi.

## Miten peli toimii
Pelaajalle näytetään intro ja ohjeet, sitten pelaajalta pyydetään nimi ja ikä. Jos ikä on alle 12, ohjelma sammuu. Jos ikä on 12 tai yli, ohjelma siirtyy valikkoon jossa pelaaja voi liikkua, tutkia ympäristöään ja löytää sieltä esineitä, katsoa mitä esineitä pelaajalla on ja lopettaa halutessaan. Pelaajan lopettaessa, hänen tietonsa tallennetaan omaan tiedostoon, jota voidaan käyttää tietojen palauttamisessa myöhemmin. Jos pelaajan syöttämää nimeä vastaava tiedosto löytyy, pelaaja saa tallennetut tiedot itselleen eikä hänen tarvitse antaa ikäänsä uudelleen. Kun pelaajalla on kaikki 4 tulpan osaa, hän voi käyttää niitä voittamiseen, jolloin voitto teksti tulostuu ja tiedot tallennetaan. 

## pelin rakenne
peliprojektin juuressa on pääohjelma: peli.py, intro.txt, ohjeet.txt, pelaaja_voittaa.txt ja ominaisuudet sekä pelaajat paketti. Ominaisuudet paketti sisältää moduuleja joissa on pelin käyttämiä luokkia ja niiden ominaisuuksia sekä tallenna ominaisuus ja init. peli.py tuo ominaisuudet paketista Pelaaja, Huone, Esine luokat + tallennus funktion ja os:n joita käytetään peliä ajettaessa. 

## Kestävä kehitys
Suuret tehtaat tuhoavat vesistöjä jos niiden annetaan päästää jätevettä vesistöihin. 
Pelissä lopputuloksena tehdään pieni protestimuotoinen teko tukkimalla jätevesiputki tulpalla. 
Tällä teolla ilmaistaan tahtoa suojella vesistöjä saastumiselta. 