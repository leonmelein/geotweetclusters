# categorize.py
# Reinard van Dalen (s2497867)
# Léon Melein (s2580861)

import pickle
import sys
import os


def main():
    provinces = ['Noord-Holland', 'Zuid-Holland', 'Noord-Brabant', 'Gelderland', 'Zeeland', 'Friesland', 'Utrecht',
                 'Limburg', 'Overijssel', 'Drenthe', 'Groningen', 'Flevoland']
    tweets = pickle.load(open('tweets.pickle', 'rb'))

    count = {}

    for key, value in tweets.items():
        if key in provinces:
            for item in value:
                search = count.get(key,None)
                if search == None:
                    count[key] = 1
                else:
                    search += 1
                    count[key] = search
            
    for key, value in count.items():
        print(key+" "+str(value))
    
if __name__ == "__main__":
    main()