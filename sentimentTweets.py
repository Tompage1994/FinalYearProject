from nltk.sentiment.vader import SentimentIntensityAnalyzer
import time

#This porgram is used to label tweets with their sentiment scores. It is designed to be run on the output of brexitTweets

f=open('reltweets','r')
fw=open('labelledtweets','w')
i=0
sid = SentimentIntensityAnalyzer()
for t in f:
    i=i+1
    text = t.split('\t')
    tweet = text[1]
    score = sid.polarity_scores(tweet)#Get the sentiment score
    #Write to file
    fw.write(text[0] + '\t' + tweet[0:len(tweet)-1] + '\t' + str(score) +'\n')
       
