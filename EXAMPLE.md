# Aantal Tweets in Augustus 2015
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

Totaal aantal Tweets: 37863

# Indexing using Rainbow
# 10-fold
/net/aps/32/bin/rainbow --index Flevoland/ Friesland/ Gelderland/ Groningen/ Limburg/ Noord-Brabant/ Noord-Holland/ Overijssel/ Utrecht/ Zeeland/ Zuid-Holland/
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

# Rainbow output
/net/aps/32/bin/rainbow --test=10 --method=naivebayes --test-set=0.1 | /net/aps/32/bin/rainbow-stats
Loading data files...
Randomly selected 37863 documents for the test set:
   1015 : Flevoland
   1937 : Friesland
   5588 : Gelderland
   1088 : Groningen
   1732 : Limburg
   4287 : Noord-Brabant
   7413 : Noord-Holland
   3039 : Overijssel
   2538 : Utrecht
    907 : Zeeland
   8319 : Zuid-Holland
Placed remaining 340774 documents in the train set:
Randomly selected 37863 documents for the test set:
   1015 : Flevoland
   1937 : Friesland
   5588 : Gelderland
   1088 : Groningen
   1732 : Limburg
   4287 : Noord-Brabant
   7413 : Noord-Holland
   3039 : Overijssel
   2538 : Utrecht
    907 : Zeeland
   8319 : Zuid-Holland
Placed remaining 340774 documents in the train set:
Trial 0

Correct: 16761 out of 37863 (44.27 percent accuracy)

 - Confusion details, row is actual, column is predicted
       classname   0   1   2   3   4   5   6   7   8   9  10  :total
 0     Flevoland  55   1  93   1   2  24 312  23   7   . 497  :1015   5.42%
 1     Friesland   . 465 181   .   .  52 404  32   4   . 799  :1937  24.01%
 2    Gelderland   1   6 2340   .   2  98 971  50   9   . 2111  :5588  41.88%
 3     Groningen   .   2 101 131   .  32 247  14   2   . 559  :1088  12.04%
 4       Limburg   .   1 126   1 276  78 365  17   3   . 865  :1732  15.94%
 5 Noord-Brabant   .   2 283   .  18 1222 855  19   6   . 1882  :4287  28.50%
 6 Noord-Holland   1  18 303   .   4  96 4438  31  11   2 2509  :7413  59.87%
 7    Overijssel   1   1 235   1   1  66 634 802   2   . 1296  :3039  26.39%
 8       Utrecht   .   3 207   .   7  57 736  14 311   . 1203  :2538  12.25%
 9       Zeeland   .   2  80   .   1  47 248  11   4  41 473  :907   4.52%
10  Zuid-Holland   1   3 317   4  21 118 1137  28  10   . 6680  :8319  80.30%

Randomly selected 37863 documents for the test set:
   1015 : Flevoland
   1937 : Friesland
   5588 : Gelderland
   1088 : Groningen
   1732 : Limburg
   4287 : Noord-Brabant
   7413 : Noord-Holland
   3039 : Overijssel
   2538 : Utrecht
    907 : Zeeland
   8319 : Zuid-Holland
Placed remaining 340774 documents in the train set:
Trial 1

Correct: 16668 out of 37863 (44.02 percent accuracy)

 - Confusion details, row is actual, column is predicted
       classname   0   1   2   3   4   5   6   7   8   9  10  :total
 0     Flevoland  47   1 100   1   1  19 325  22   3   1 495  :1015   4.63%
 1     Friesland   . 467 182   .   3  48 430  33   2   . 772  :1937  24.11%
 2    Gelderland   1   3 2276   .   2 116 980  49   7   . 2154  :5588  40.73%
 3     Groningen   .   2  80 114   1  21 272  12   4   . 582  :1088  10.48%
 4       Limburg   .   3 132   . 279  65 401   9   5   . 838  :1732  16.11%
 5 Noord-Brabant   1   4 231   .   9 1285 864  25  12   2 1854  :4287  29.97%
 6 Noord-Holland   1  13 294   1   3 100 4405  30   5   . 2561  :7413  59.42%
 7    Overijssel   .   1 274   .   3  62 601 873   4   . 1221  :3039  28.73%
 8       Utrecht   .   3 208   .   6  54 731  10 309   . 1217  :2538  12.17%
 9       Zeeland   .   4 100   .   .  58 221  10   1  36 477  :907   3.97%
10  Zuid-Holland   1   3 308   1  15 115 1262  31   6   . 6577  :8319  79.06%

Randomly selected 37863 documents for the test set:
   1015 : Flevoland
   1937 : Friesland
   5588 : Gelderland
   1088 : Groningen
   1732 : Limburg
   4287 : Noord-Brabant
   7413 : Noord-Holland
   3039 : Overijssel
   2538 : Utrecht
    907 : Zeeland
   8319 : Zuid-Holland
Placed remaining 340774 documents in the train set:
Trial 2

Correct: 16777 out of 37863 (44.31 percent accuracy)

 - Confusion details, row is actual, column is predicted
       classname   0   1   2   3   4   5   6   7   8   9  10  :total
 0     Flevoland  62   1 103   .   4  26 310  13   3   . 493  :1015   6.11%
 1     Friesland   . 474 188   1   1  43 410  35   6   . 779  :1937  24.47%
 2    Gelderland   1   4 2333   .   1 121 956  51   5   . 2116  :5588  41.75%
 3     Groningen   .   2  98 117   .  32 287  17   1   . 534  :1088  10.75%
 4       Limburg   .   1 145   . 287  79 364  10   2   . 844  :1732  16.57%
 5 Noord-Brabant   .   4 243   1  15 1251 859  22   9   . 1883  :4287  29.18%
 6 Noord-Holland   2  15 273   .   4 104 4396  33   9   1 2576  :7413  59.30%
 7    Overijssel   .   3 262   1   1  80 613 846   4   . 1229  :3039  27.84%
 8       Utrecht   .   1 193   .   7  57 718  17 326   . 1219  :2538  12.84%
 9       Zeeland   1   1  80   .   .  61 221   7   3  42 491  :907   4.63%
10  Zuid-Holland   .   4 291   .  22 124 1198  27  10   . 6643  :8319  79.85%

Randomly selected 37863 documents for the test set:
   1015 : Flevoland
   1937 : Friesland
   5588 : Gelderland
   1088 : Groningen
   1732 : Limburg
   4287 : Noord-Brabant
   7413 : Noord-Holland
   3039 : Overijssel
   2538 : Utrecht
    907 : Zeeland
   8319 : Zuid-Holland
Placed remaining 340774 documents in the train set:
Trial 3

Correct: 16836 out of 37863 (44.47 percent accuracy)

 - Confusion details, row is actual, column is predicted
       classname   0   1   2   3   4   5   6   7   8   9  10  :total
 0     Flevoland  52   2  91   .   2  25 318  19   3   . 503  :1015   5.12%
 1     Friesland   1 423 164   .   .  48 454  38   5   . 804  :1937  21.84%
 2    Gelderland   1   4 2401   1   6  88 956  61  11   . 2059  :5588  42.97%
 3     Groningen   .   4 100 125   .  35 261  21   3   . 539  :1088  11.49%
 4       Limburg   .   2 123   1 279  79 395   9   1   . 843  :1732  16.11%
 5 Noord-Brabant   .   5 281   1  12 1260 837  20   9   3 1859  :4287  29.39%
 6 Noord-Holland   .  14 293   1   3 100 4474  32   9   2 2485  :7413  60.35%
 7    Overijssel   .   2 239   .   1  79 625 860   6   . 1227  :3039  28.30%
 8       Utrecht   1   4 176   .   8  59 692  11 318   . 1269  :2538  12.53%
 9       Zeeland   .   3  93   .   .  38 219   9   2  36 507  :907   3.97%
10  Zuid-Holland   .   4 292   2  26 103 1240  35   9   . 6608  :8319  79.43%

Randomly selected 37863 documents for the test set:
   1015 : Flevoland
   1937 : Friesland
   5588 : Gelderland
   1088 : Groningen
   1732 : Limburg
   4287 : Noord-Brabant
   7413 : Noord-Holland
   3039 : Overijssel
   2538 : Utrecht
    907 : Zeeland
   8319 : Zuid-Holland
Placed remaining 340774 documents in the train set:
Trial 4

Correct: 16765 out of 37863 (44.28 percent accuracy)

 - Confusion details, row is actual, column is predicted
       classname   0   1   2   3   4   5   6   7   8   9  10  :total
 0     Flevoland  59   3  95   .   4  21 318  18   3   . 494  :1015   5.81%
 1     Friesland   . 463 179   .   3  49 417  29   5   . 792  :1937  23.90%
 2    Gelderland   1   2 2316   .   5  98 1005  54   8   . 2099  :5588  41.45%
 3     Groningen   .   5  83 127   .  28 269  16   .   . 560  :1088  11.67%
 4       Limburg   .   . 125   . 291  57 384  15   2   . 858  :1732  16.80%
 5 Noord-Brabant   1   4 273   .  21 1235 863  27   5   . 1858  :4287  28.81%
 6 Noord-Holland   3  17 305   .   .  99 4462  21   8   . 2498  :7413  60.19%
 7    Overijssel   .   4 255   .   2  74 572 888   3   . 1241  :3039  29.22%
 8       Utrecht   .   3 202   .   7  47 716  13 270   . 1280  :2538  10.64%
 9       Zeeland   .   2  85   1   .  51 242   5   1  45 475  :907   4.96%
10  Zuid-Holland   1   6 276   1  20 111 1268  20   6   1 6609  :8319  79.44%

Randomly selected 37863 documents for the test set:
   1015 : Flevoland
   1937 : Friesland
   5588 : Gelderland
   1088 : Groningen
   1732 : Limburg
   4287 : Noord-Brabant
   7413 : Noord-Holland
   3039 : Overijssel
   2538 : Utrecht
    907 : Zeeland
   8319 : Zuid-Holland
Placed remaining 340774 documents in the train set:
Trial 5

Correct: 16815 out of 37863 (44.41 percent accuracy)

 - Confusion details, row is actual, column is predicted
       classname   0   1   2   3   4   5   6   7   8   9  10  :total
 0     Flevoland  42   .  91   1   .  22 347  16   5   . 491  :1015   4.14%
 1     Friesland   . 485 167   .   .  43 422  33   4   2 781  :1937  25.04%
 2    Gelderland   .   6 2321   .   3 110 980  49   8   . 2111  :5588  41.54%
 3     Groningen   .   6 103 122   .  24 258  23   1   . 551  :1088  11.21%
 4       Limburg   .   1 107   . 300  63 414   7   5   . 835  :1732  17.32%
 5 Noord-Brabant   1   4 249   .   9 1236 895  23  12   . 1858  :4287  28.83%
 6 Noord-Holland   1   8 308   .   5  97 4443  24  10   . 2517  :7413  59.94%
 7    Overijssel   .   1 227   1   2  77 599 878   4   . 1250  :3039  28.89%
 8       Utrecht   .   2 189   .   3  51 707  18 301   . 1267  :2538  11.86%
 9       Zeeland   .   2  97   1   .  54 213   8   1  47 484  :907   5.18%
10  Zuid-Holland   .   4 298   2  15 112 1214  24  10   . 6640  :8319  79.82%

Randomly selected 37863 documents for the test set:
   1015 : Flevoland
   1937 : Friesland
   5588 : Gelderland
   1088 : Groningen
   1732 : Limburg
   4287 : Noord-Brabant
   7413 : Noord-Holland
   3039 : Overijssel
   2538 : Utrecht
    907 : Zeeland
   8319 : Zuid-Holland
Placed remaining 340774 documents in the train set:
Trial 6

Correct: 16792 out of 37863 (44.35 percent accuracy)

 - Confusion details, row is actual, column is predicted
       classname   0   1   2   3   4   5   6   7   8   9  10  :total
 0     Flevoland  67   3  67   .   .  30 304  14   7   . 523  :1015   6.60%
 1     Friesland   . 433 169   .   1  45 413  29   6   . 841  :1937  22.35%
 2    Gelderland   .   1 2375   .   2 109 934  39  14   2 2112  :5588  42.50%
 3     Groningen   .   2 104 123   2  24 286  17   3   . 527  :1088  11.31%
 4       Limburg   1   . 103   . 296  70 408  12   3   . 839  :1732  17.09%
 5 Noord-Brabant   2   6 257   .  10 1249 853  24   5   . 1881  :4287  29.13%
 6 Noord-Holland   1  13 327   .   2  97 4411  28   7   2 2525  :7413  59.50%
 7    Overijssel   .   2 236   1   1  64 597 867   2   . 1269  :3039  28.53%
 8       Utrecht   .   1 214   .   8  75 727  15 299   . 1199  :2538  11.78%
 9       Zeeland   .   1  82   .   1  55 259  10   4  47 448  :907   5.18%
10  Zuid-Holland   2   6 284   .  17 106 1244  27   8   . 6625  :8319  79.64%

Randomly selected 37863 documents for the test set:
   1015 : Flevoland
   1937 : Friesland
   5588 : Gelderland
   1088 : Groningen
   1732 : Limburg
   4287 : Noord-Brabant
   7413 : Noord-Holland
   3039 : Overijssel
   2538 : Utrecht
    907 : Zeeland
   8319 : Zuid-Holland
Placed remaining 340774 documents in the train set:
Trial 7

Correct: 16860 out of 37863 (44.53 percent accuracy)

 - Confusion details, row is actual, column is predicted
       classname   0   1   2   3   4   5   6   7   8   9  10  :total
 0     Flevoland  47   1  86   .   1  27 334  17   4   . 498  :1015   4.63%
 1     Friesland   . 461 181   1   2  39 434  29   5   . 785  :1937  23.80%
 2    Gelderland   .   3 2357   .   5 117 960  49   9   1 2087  :5588  42.18%
 3     Groningen   .   4  97 110   1  22 299  21   2   . 532  :1088  10.11%
 4       Limburg   .   4 123   . 283  64 395  10   3   . 850  :1732  16.34%
 5 Noord-Brabant   1   6 273   .   8 1246 844  24  12   1 1872  :4287  29.06%
 6 Noord-Holland   1  13 303   1   2  96 4444  24  10   . 2519  :7413  59.95%
 7    Overijssel   .   3 234   .   1  79 606 840   4   . 1272  :3039  27.64%
 8       Utrecht   .   . 197   .   7  60 705  16 328   . 1225  :2538  12.92%
 9       Zeeland   .   1  84   1   1  47 227  12   6  42 486  :907   4.63%
10  Zuid-Holland   .   4 264   1  18 104 1182  34  10   . 6702  :8319  80.56%

Randomly selected 37863 documents for the test set:
   1015 : Flevoland
   1937 : Friesland
   5588 : Gelderland
   1088 : Groningen
   1732 : Limburg
   4287 : Noord-Brabant
   7413 : Noord-Holland
   3039 : Overijssel
   2538 : Utrecht
    907 : Zeeland
   8319 : Zuid-Holland
Placed remaining 340774 documents in the train set:
Trial 8

Correct: 16915 out of 37863 (44.67 percent accuracy)

 - Confusion details, row is actual, column is predicted
       classname   0   1   2   3   4   5   6   7   8   9  10  :total
 0     Flevoland  47   1  97   1   2  21 306  28   6   . 506  :1015   4.63%
 1     Friesland   . 476 196   .   2  40 406  37   3   2 775  :1937  24.57%
 2    Gelderland   1   2 2353   .   5 109 957  38  10   1 2112  :5588  42.11%
 3     Groningen   .   1  89 126   .  30 261  15   1   . 565  :1088  11.58%
 4       Limburg   .   2 134   . 252  69 379  11   4   . 881  :1732  14.55%
 5 Noord-Brabant   2   2 244   .  10 1306 899  18  12   1 1793  :4287  30.46%
 6 Noord-Holland   1  16 279   .   2  74 4536  23  12   . 2470  :7413  61.19%
 7    Overijssel   .   3 255   .   2  74 606 806   2   . 1291  :3039  26.52%
 8       Utrecht   .   1 203   .  10  54 704  13 292   . 1261  :2538  11.51%
 9       Zeeland   1   3  98   .   1  38 240   9   4  36 477  :907   3.97%
10  Zuid-Holland   1   8 269   4  21 110 1192  19  10   . 6685  :8319  80.36%

Trial 9

Correct: 16831 out of 37863 (44.45 percent accuracy)

 - Confusion details, row is actual, column is predicted
       classname   0   1   2   3   4   5   6   7   8   9  10  :total
 0     Flevoland  48   . 103   1   2  19 333  14   2   1 492  :1015   4.73%
 1     Friesland   . 435 166   1   2  39 456  31   5   1 801  :1937  22.46%
 2    Gelderland   1   5 2387   1   5  96 952  55   7   1 2078  :5588  42.72%
 3     Groningen   .   3 106 124   3  30 267  18   3   . 534  :1088  11.40%
 4       Limburg   .   1 120   . 302  68 351   9   4   . 877  :1732  17.44%
 5 Noord-Brabant   .   3 310   .   9 1296 847  27   9   1 1785  :4287  30.23%
 6 Noord-Holland   .  11 297   1   1  89 4436  18   9   1 2550  :7413  59.84%
 7    Overijssel   .   5 243   .   .  68 614 826   2   . 1281  :3039  27.18%
 8       Utrecht   .   3 212   .   8  56 689  15 297   . 1258  :2538  11.70%
 9       Zeeland   .   2  94   .   .  55 226   6   2  35 487  :907   3.86%
10  Zuid-Holland   1   4 318   2  17 117 1168  32  14   1 6645  :8319  79.88%

Percent_Accuracy  average 44.38 stderr 0.05

# 1-fold
/net/aps/32/bin/rainbow --test=1 --method=naivebayes --test-set=0.1 | /net/aps/32/bin/rainbow-stats
Loading data files...
Randomly selected 37863 documents for the test set:
   1015 : Flevoland
   1937 : Friesland
   5588 : Gelderland
   1088 : Groningen
   1732 : Limburg
   4287 : Noord-Brabant
   7413 : Noord-Holland
   3039 : Overijssel
   2538 : Utrecht
    907 : Zeeland
   8319 : Zuid-Holland
Placed remaining 340774 documents in the train set:
Trial 0

Correct: 16746 out of 37863 (44.23 percent accuracy)

 - Confusion details, row is actual, column is predicted
       classname   0   1   2   3   4   5   6   7   8   9  10  :total
 0     Flevoland  52   3  90   .   5  23 313  20   7   . 502  :1015   5.12%
 1     Friesland   1 424 189   .   2  34 418  34   2   . 833  :1937  21.89%
 2    Gelderland   .   5 2329   .   1 111 1006  43   7   . 2086  :5588  41.68%
 3     Groningen   .   1  93 109   .  23 274  19   4   . 565  :1088  10.02%
 4       Limburg   .   1 119   . 275  67 377  10   2   . 881  :1732  15.88%
 5 Noord-Brabant   1   2 263   .  14 1247 838  25   9   1 1887  :4287  29.09%
 6 Noord-Holland   1  13 309   1   3 110 4392  28   6   1 2549  :7413  59.25%
 7    Overijssel   .   1 228   1   1  81 595 861   5   . 1266  :3039  28.33%
 8       Utrecht   1   2 208   .   5  45 701  17 306   . 1253  :2538  12.06%
 9       Zeeland   .   .  97   1   2  44 227   5   5  56 470  :907   6.17%
10  Zuid-Holland   1   5 264   1  23 118 1181  21   9   1 6695  :8319  80.48%

Percent_Accuracy  average 44.23 stderr 0.00

# Precision, Recall en F-Score
Flevoland
Precision 	= 52/(52+3+90+5+23+313+20+7+502)							= 5,12%
Recall 		= 52/(52+1+1+1+1+1) 										= 91%
F-Score 	= (2*5,12*0,91)/(5,12+0,91)									= 1,55%

Friesland
Precision	= 424/(1+424+189+2+34+418+34+2+833)							= 21,89%
Recall		= 424/(3+424+5+1+1+2+13+1+2+5)								= 93%
F-Score		= (2*21,89*0,93)/(21,89+0,93)								= 1,78%

Gelderland
Precision	= 2329/(5+2329+1+111+1006+43+7+2086)						= 41,68%
Recall		= 2329/(90+189+2329+93+119+263+309+228+208+97+264)			= 56%
F-Score		= (2*41,68*0,56)/(41,68+0,56)								= 1,11%

Groningen
Precision	= 109/(1+93+109+23+274+19+4+565)							= 10,02%
Recall		= 109/(109+1+1+1+1)											= 96%
F-Score		= (2*10,02*0,96)/(10,02+0,96)								= 1,75%

Limburg
Precision	= 275/(1+119+275+67+377+10+2+881)							= 15,88%
Recall		= 275/(5+2+1+275+14+3+1+5+2+23)								= 83%
F-Score		= (2*15,88*0,83)/(15,88+0,83)								= 1,58%

Noord-Brabant
Precision	= 1247/(1+2+263+14+1247+838+25+9+1+1887)					= 29,09%
Recall		= 1247/(23+34+111+23+67+1247+110+81+45+44+118)				= 66%
F-Score		= (2*29,09*0,66)/(29,09+0,66)								= 1,29%

Noord-Holland
Precision	= 4392/(1+13+309+1+3+110+4392+28+6+1+2549)					= 59,25%
Recall		= 4392/(313+418+1006+274+377+838+4392+595+701+227+1181)		= 43%
F-Score		= (2*59,25*0,43)/(59,25+0,43)								= 0,85%

Overijssel
Precision 	= 861/(1+228+1+1+81+595+861+5+1266)							= 28,33%
Recall		= 861/(20+34+43+19+10+25+28+861+17+5+21)					= 80%
F-Score		= (2*28,33*0,80)/(28,33+0,80)								= 1,56%

Utrecht
Precision 	= 306/(1+2+208+5+45+701+17+306+1253)	 					= 12,06%
Recall		= 306/(7+2+7+4+2+9+6+5+306+5+9)								= 85%
F-Score		= (2*12,06*0,85)/(12,06+0,85)								= 1,59%

Zeeland
Precision 	= 56/(97+1+2+44+227+5+5+56+470)								= 80,48%
Recall		= 56/(1+1+56+1)												= 95%
F-Score		= (2*80.48*0,95)/(80.48+0,95)								= 1,90%

Zuid-Holland
Precision 	= 6695/(1+5+264+1+23+118+1181+21+9+1+6695)					= 28,33%
Recall		= 6695/(502+833+2086+565+881+1887+2549+1266+1253+470+6695)	= 35%
F-Score		= (2*28,33*0,35)/(28,33+0,35)								= 0,69%

Overall
Precision	= (5,12%+21,89%+41,68%+10,02%+15,88%+29,09%+59,25%+28,33%+12,06%+80,48%+28,33%)/11	= 30%
Recall		= (91%+93%+56%+83%+66%+43%+80%+85%+95%+35%)/11										= 66%
F-Score		= (2*30*66)/(30+66)																	= 41,25%

# Feature Selection
/net/aps/32/bin/rainbow --prune-vocab-by-infogain=50 --test=10 --method=naivebayes --test-set=0.1 | /net/aps/32/bin/rainbow-stats

N 			Accuracy
50			26,03
100			27,93
500			32,76
1000		35,43
2000		38,03
3000		39,61
4000		40,94
5000		41,72
6000		42,45
7000		43,01
8000		43,49
9000		44,08
10000		44,20
15000		45,39
20000		46,08
25000		46,50
30000		46,53
35000		46,83
40000		46,90
50000		47,01
60000		47,08
70000		47,15
75000		47,16
75125		47,27
75250		47,11
75500		47,02
76000		46,91
80000		46,86
90000		46,75
100000		46,69

Beste bij de 75125 meest informatieve woorden.
Accuracy 	: 47,27
Precision 	: 35,65%
Recall 		: 64,76%
F-Score		: 45,99%

# Significant verschil tussen wel/geen Feature selection
Unpaired t-test SPSS

Incl. Feature Selection 	Excl. Feature Selection
47,37						44,27
47,53						44,02
47,50						44,31
47,31						44,47
46,80						44,28
47,03						44,41
47,31						44,35
47,11						44,53
47,22						44,67
47,48						44,45

t-score : 31,406
p-value	: 0,000

De p-waarde is <0,05. Er is dus sprake van een significant verschil tussen het gebruik van de feature selection en het niet gebruiken ervan.