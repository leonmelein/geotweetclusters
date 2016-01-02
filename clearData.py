# clearData.py
# Reinard van Dalen (s2497867)
# Léon Melein (s2580861)

import pickle
import sys

def main():
	tweets = {}
	for line in sys.stdin:
		datalist = line.rstrip().split('	')
		tweetID = datalist[0]
		tweetUser = datalist[1]
		tweetText = datalist[2]
		try:
			tweetGEO = datalist[3]
			Province = tweetGEO.split(', ')[1]
			search = tweets.get(Province,None)
			if search is None:
				tweets[Province] = [(tweetID, tweetUser, tweetText, tweetGEO)]
			else:
				search.append((tweetID, tweetUser, tweetText, tweetGEO))
				tweets[Province] = search
		except:
			dotnothing = "dotnothing"
	
	with open('tweets.pickle','wb') as f:
		pickle.dump(tweets,f)

if __name__ == "__main__":
	main()
