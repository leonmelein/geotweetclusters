# geotweetclusters
Geolocatie van twitterberichten via tekstclassificatie

# Nederlandse Tweets Augustus 2015 
zcat /net/corpora/twitter2/Tweets/2015/08/* | /net/corpora/twitter2/tools/tweet2tab id user coordinates | wc -l
20372259

# Nederlandse Tweets met GEO Place als resulaat van clearData.py geteld met count.py
Noord-Holland 74132
Friesland 19368
Overijssel 30400
Utrecht 25382
Gelderland 55874
Zuid-Holland 83199
Zeeland 9078
Limburg 17314
Groningen 10877
Noord-Brabant 42867
Flevoland 10146

# Indexing using Rainbow
/net/aps/32/bin/rainbow --index Flevoland/ Friesland/ Gelderland/ Groningen/ Limburg/ Noord-Brabant/ Noord-Holland/ Overijssel/ Utrecht/ Zeeland/ Zuid-Holland
Class `Flevoland'
  Gathering stats... files : unique-words ::  10146 :    24449
Class `Friesland'
  Gathering stats... files : unique-words ::  19368 :    51310
Class `Gelderland'
  Gathering stats... files : unique-words ::  55874 :   109126
Class `Groningen'
  Gathering stats... files : unique-words ::  10877 :   119141
Class `Limburg'
  Gathering stats... files : unique-words ::  17314 :   136406
Class `Noord-Brabant'
  Gathering stats... files : unique-words ::  42867 :   174110
Class `Noord-Holland'
  Gathering stats... files : unique-words ::  74132 :   237194
Class `Overijssel'
  Gathering stats... files : unique-words ::  30400 :   262316
Class `Utrecht'
  Gathering stats... files : unique-words ::  25382 :   280125
Class `Zeeland'
  Gathering stats... files : unique-words ::   9078 :   286271
Class `Zuid-Holland'
  Gathering stats... files : unique-words ::  83199 :   337652
