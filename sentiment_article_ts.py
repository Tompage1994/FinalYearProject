import sys
import re
import string
import collections
import numpy as np
import os
import shutil

#This program creates a time series of sentiment for articles. It is designed to be run after the sentimentArticles program has been run

dates = {}
fd = open("/home/zcabtpa/dates",'r')#Get the list of dates
i = 0
for dateline in fd:
    dates[dateline[0:8]] = i
    i+=1
fd.close()
outlets=["Metro", "BBC News","The Mirror","Daily Mail","The Guardian","Sky \
News","The Daily Telegraph","Daily Express","London Evening Standard"]
m = np.zeros((366*24,5*9), dtype=np.float)
for i in range(9):
    f = open("labelledarticles",'r')
    l = 0
    t=""
    for line in f:
        t += line
        if t.find("@@@@@@") == -1: #Used to mark end of article
            continue
        tweet = t.split('\t')
        t=""
        outlet = tweet[0]
        date = tweet[1]
        if int(date)>2015093024:
            sentiment = eval(tweet[3])
            if (sentiment['neu'] < 1.0) and (outlet == outlets[i]):
                loc=dates[date[0:8]]*24+int(date[8:10])
                #take the labelling and place it in a time series matrix
                m[loc,i*5] += 1
                m[loc,i*5+1] += sentiment['compound']
                m[loc,i*5+2] += sentiment['neg']
                m[loc,i*5+3] += sentiment['pos']
                m[loc,i*5+4] += sentiment['neu']
    f.close()
fw = open("sentiment_article_ts","w")
#Write time series to file
for day in range(366*24):
    l=""
    for o in range(9):
        for i in range(4):
            if m[day,o*5] > 0:
                #If there are entries at this slot then take the average
                l+=(str(m[day,o*5+i+1]/m[day,o*5]) + " ")
            else:
                #If no entries, avoid a div by zero and set to zero
                l+=("0 ")
    fw.write(l + '\n')                
fw.close()
            
