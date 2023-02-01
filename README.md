# RUSH HOUR


## Description
Voor deze case hebben wij algoritmes en heuristieken uitgewerkt en toegepast op het bordspel Rush Hour.
Het programma kan gerund worden voor verschillende speelborden, algoritmes en output geven van statistische informatie omtrent de case.

## Inhoud
- codefiles
  - algorithms: BFS, DFS, Beam Search en random algoritmes als classes
  - classes: elementen zoals Board, Car, Queue en Stack als classes die gebruikt worden door algoritmes
  - visualisations: bestaande uit de representatie, het up- en downloaden van data naar/uit csv bestanden en functies voor grafieken
- data
  - statistics: csv bestand met data over gerunde algoritmes
  - speelborden: csv bestan met informatie over de begin-states van speelborden
- main.py: functies voor in- en output van/naar de gebruiker

## Installaties
De volgende packages zijn nodig om het programma te runnen:
- numpy
- matplotlib
- colorhash
- csv
- sys
- time
- copy
- random
- operator

## Gebruik

Experimenten kunnen gedaan worden middels "python3 main.py [filename] [algorithm] [nr of runs]"
Als filename verwacht het programma een "RushHour{dim}x{dim}_n" bestand als input en een integer voor het gewenste aantal runs.
Er kan uit de volgende algoritmes gekozen worden:
 - random: dit algoritme kiest willekeurig legale zetten
 - breadth: hierbij wordt gebruik gemaakt van een breadth first search
 - randombreadth: een breadth first die in de queue enkel states heeft van het random algoritme
 - depth: hierbij wordt gebruikt gemaakt van een depth first search
 - beam: hierbij wordt gebruik gemaakt van een beam Search
Eerst zal het speelbord gevisualiseerd worden, nadat het venster wordt gesloten begint het algoritme te runnen.
Waaneer een oplossing is gevonden zal de oplossing worden weergegeven en de laatste state van het speelbord verschijnen. Nogmaals het venster sluiten biedt de mogelijkheid om andere input te geven, daarnaast zullen de resultaten van het algoritme automatisch worden geüpload naar het geschikte csv bestand (indien aanwezig).

Data visualiseren kan op de volgende manier: "python3 main.py statistics [algorithm] [dimension]"
Een keuze kan gemaakt worden uit eerder genoemde algoritmes, daarbij moet de gewenste dimensie van het speelbord aangegeven worden. Vervolgens worden verscheiden histogrammen weergegeven.
Enkele kanttekeningen:
- Voor het random algoritme is de lengte van de oplossing gelijk aan het aantal bezochte states
- Voor BFS zijn op eenzelfde computer de resultaten per speelbord hetzelfde


## Bijlagen
![schets](images/ac8d9a2f-b2d0-490b-95e6-5e25167d6668.jpeg)
![instantie](images/Rushhour6x6img.jpg)
