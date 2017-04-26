import sys
import re
import string
import collections
import nltk
import numpy as np
import os
import shutil

#This was used to create a time series of a number of keywords from twitter. Not all of these keywords were used for the final stages of the study, however this time series was used to establish which keywords were relevant.

dates = {}
fd = open("/home/zcabtpa/dates",'r')#get list of dates
i = 0
for dateline in fd:
    dates[dateline[0:8]] = i
    i+=1
fd.close()
#Our list of relevant keywords, found from a number of sources including other studies, some news articles, and collective discussion
dict=['metro','bbc news','daily express','daily mail','telegraph','guardian','sky news','evening standard','daily mirror','referendum','brexit','immigration','farage','independence','boris','sovereignty','sturgeon','leave','remain','#voteleave','#strongerin','#voteremain','#leaveeu','@metrouk','@bbcnews','@daily_express','@mailonline','@telegraph','@guardian','@skynews','@standardnews','@dailymirror']
m = np.zeros((1+366*24,len(dict)), dtype=np.int)
for i in range(12):
    print("File Number: " + '{:02d}'.format(i))
    #Data spread across 12 files. This must be loaded used and deleted 1 by 1
    shutil.copy("/home/zcabtpa/part-r-000"+'{:02d}'.format(i),".")
    f = open("part-r-000" + '{:02d}'.format(i),'r')
    for line in f:
    
        tweet = line.split('\t',3)
        date = tweet[2][0:10]
        if int(date)>2015093024:
            text = tweet[3]
            text = text.lower()
            for w in range(len(dict)):
                if text.find(dict[w]) != -1:#if word within the text of the tweet then we increase the count for that hour for that word.
                    loc=dates[date[0:8]]*24+int(date[8:10])
                    m[loc+1,w]+=1
                    m[0,w]+=1           
    f.close()
    os.remove("part-r-000" + '{:02d}'.format(i))
fw = open("outletfile","w")
#Write time series to file
for t in range(len(dict)):
    fw.write(dict[t])
    for day in range(1+366*24):
        fw.write(" " + str(m[day,t]))
    fw.write('\n')
fw.close()
            
