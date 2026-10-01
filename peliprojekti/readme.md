# "Tähän pelin nimi"
**Artur Truve**

## Miten peli toimii

Pelaajalta pyydetään nimi ja ikä. Jos ikä on alle 12, ohjelma sammuu. Jos ikä on 12 tai yli, ohjelma siirtyy valikkoon jossa pelaaja voi liikkua, tutkia huonetta ja löytää huoneista esineitä, katsoa mitä esineitä pelaajalla on ja lopettaa halutessaan. 

## pelin rakenne
peliprojektin juuressa on pääohjelma: peli.py ja ominaisuudet paketti. Ominaisuudet paketti sisältää moduuleja joissa on määritelty pelin käyttämät luokat ja niiden funktiot. peli.py tuo ominaisuudet paketista Pelaaja, Huone ja Esine luokat + niiden funktiot, joita sitten käytetään pelissä. 