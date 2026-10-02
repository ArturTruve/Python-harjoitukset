# "AVAINJAHTI"
**Artur Truve**

## Miten peli toimii

Pelaajalle näytetään intro ja ohjeet, sitten pelaajalta pyydetään nimi ja ikä. Jos ikä on alle 12, ohjelma sammuu. Jos ikä on 12 tai yli, ohjelma siirtyy valikkoon jossa pelaaja voi liikkua, tutkia huonetta ja löytää huoneista esineitä, katsoa mitä esineitä pelaajalla on ja lopettaa halutessaan. Jos pelaajan syöttämää nimeä vastaava tiedosto löytyy, pelaaja saa tallennetut tiedot itselleen. 

## pelin rakenne
peliprojektin juuressa on pääohjelma: peli.py, intro.txt, ohjeet.txt ja ominaisuudet paketti. Ominaisuudet paketti sisältää moduuleja joissa on määritelty pelin käyttämät luokat ja niiden funktiot sekä init. peli.py tuo ominaisuudet paketista Pelaaja, Huone, Esine luokat + niiden funktiot + tallennus funktion, joita sitten käytetään pelissä. 