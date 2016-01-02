# categorize.py
# Reinard van Dalen (s2497867)
# Léon Melein (s)

import pickle
import sys
import os

def main():
	provinces = ['Noord-Holland', 'Zuid-Holland', 'Noord-Brabant', 'Gelderland', 'Zeeland', 'Friesland', 'Utrecht', 'Limburg', 'Overijssel', 'Drenthe', 'Groningen', 'Flevoland']
	tweets = pickle.load(open('tweets.pickle','rb'))
	os.chdir("collection")
	for key,value in tweets.items():
		filenameEnd = 0
		if key in provinces:
			if not os.path.exists(key):
				os.makedirs(key)
			os.chdir(key)
			for tweet in value:
				twitterID = tweet[0]
				twitterUser = tweet[1]
				twitterText = tweet[2]
				twitterGEO	= tweet[3]
				filenameEnd += 1
				filename = "art."+str(filenameEnd)
				file = open(filename, "w")
				file.write(twitterText)
				file.close()
			os.chdir("..")

if __name__ == "__main__":
	main()