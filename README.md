# Geografische Tweetclusters
Geolocatie van Nederlandstalige twitterberichten via *Naive Bayes*-tekstclassificatie. Een project van Léon Melein en Reinard van Dalen voor het vak Information Retrieval van de bachelor Informatiekunde van de Rijksuniversiteit Groningen.

## Algemeen
Deze Python-programma’s kunnen worden gebruikt om een verzameling twitterberichten voor te bereiden voor gebruik met het programma [*Rainbow*](http://www.cs.cmu.edu/~mccallum/bow/rainbow/), een tekstclassificatieprogramma. Deze programma’s zijn vrijgegeven onder een MIT-licentie. Zie LICENSE voor alle details.

## Gebruik
### Verkrijgen van dataset
Om twitterberichten te kunnen gebruiken voor geolocatie op basis van *Naive Bayes*-tekstclassificatie, moeten deze in een tekstbestand staan met het volgende format: tweetid, gebruikersnaam, bericht, locatie. 

Op de linuxwerkplek (LWP) van de RUG kan deze data als volgt worden geëxtraheerd uit de verzameling Nederlandstalige twitterberichten:
```bash
zcat /net/corpora/twitter2/Tweets/2015/08/* | /net/corpora/twitter2/tools/tweet2tab id user coordinates > output.txt
```
### Verwerken van data
Met het programma *clearData.py* wordt het tekstbestand met twitterberichten omgezet in een Python-dictionary, zodat deze tweets snel doorlopen kunnen worden tijdens de verdere verwerking. Deze dictionary wordt weggeschreven naar een bestand.

Vervolgens kan met het programma *categorize.py* de verzameling twitterberichten worden omgezet in een bruikbaar corpus voor *Rainbow*. De tweets worden per provincie onderverdeeld in mappen. Elke afzonderlijke tweet wordt weggeschreven naar een tekstbestand.


