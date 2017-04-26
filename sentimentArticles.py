from nltk.sentiment.vader import SentimentIntensityAnalyzer
import time
#This program labels relevent articles with their sentiment. it is designed to be run after the BrexitArticles program is run 

f=open('relarticles','r')
fw=open('labelledarticles','w')
i=0
sid = SentimentIntensityAnalyzer()
t = ""
for l in f:
    t += l
    if t.find("@@@@@@") == -1: #Marker used at end of articles (since articles across multiple lines)
        continue
    i=i+1
    text = t.split('\t')
    article = text[2]
    score = sid.polarity_scores(article)#Get the sentiment score from VADER
    #Label the article with its sentiment
    fw.write(text[0] + '\t' + text[1] + '\t'  + article[0:len(article)-1] + '\t' + str(score) +'\n')
    t=""
    
