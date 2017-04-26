import sys
import re
import string
import collections
import numpy as np
import os
import shutil

#This program labels creates a time series of the mean sentiment scores for each hour across the year for relevant tweets. This program is designed to be run after sentimentTweets.py

dates = {}
fd = open("/home/zcabtpa/dates",'r')#get a list of dates
i = 0
for dateline in fd:
    dates[dateline[0:8]] = i
    i+=1
fd.close()
m = np.zeros((366*24,5), dtype=np.float)
for i in range(1):
    f = open("labelledtweets",'r')#open output of sentimentTweets
    l = 0
    for line in f:
        tweet = line.split('\t')
        date = tweet[0]
        if int(date)>2015093024:
            sentiment = eval(tweet[2])#evaluate the dict format saved to file
            if sentiment['neu'] < 1.0:
                loc=dates[date[0:8]]*24+int(date[8:10])
                m[loc,0] += 1
                m[loc,1] += sentiment['compound']
                m[loc,2] += sentiment['neg']
                m[loc,3] += sentiment['pos']
                m[loc,4] += sentiment['neu']
    f.close()
fw = open("sentiment_ts","w")
for day in range(366*24):
    for i in range(4):
        if m[day,0] > 0:
            fw.write(" " + str(m[day,i+1]/m[day,0]))#Write the mean for that hour if at least one relevant tweet posted
        else:
            #record zeros
            fw.write("0 0 0 0")
            fw.write('\n')
fw.close()
            
