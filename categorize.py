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

    if not os.path.exists("collection"):
        os.mkdir("collection")
    os.chdir("collection")

    for key, value in tweets.items():
        filenameEnd = -1
        if key in provinces:
            if not os.path.exists(key):
                os.makedirs(key)
            os.chdir(key)
            for tweet in value:
                twitterText = tweet[2]

                # Remove emoji's from tweet
                clearEmojis = twitterText.encode("iso-8859-1", "ignore")

                filenameEnd += 1
                filename = "art." + str(filenameEnd)
                file = open(filename, "w", encoding="iso-8859-1")
                file.write(clearEmojis.decode(encoding="iso-8859-1"))
                file.close()
            os.chdir("..")


if __name__ == "__main__":
    main()
