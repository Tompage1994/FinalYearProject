import sys
import re
import string
import collections
import shutil
import nltk
import numpy as np
from nltk.corpus import stopwords

#This program was used to create a vector space model for each day of the year. It is from this that initial analysis into keywords and analyses of relevant articles and tweets. Another version of this program was adapted in order toc collect the same data from articles

dates = {}
fd = open("/home/zcabtpa/dates",'r')#Get the list of dates
i = 0
for dateline in fd:
    dates[dateline[0:8]] = i
    i+=1
fd.close()
printable = set(string.printable)
stops = set(stopwords.words('english'))#ignore a list of stopwords, e.g. 'to' or 'and'
stops.add('rt') #ignore the word 'rt' as this is an indcator a tweet is a retweet in twitter, we therefore do not want to include this value
dict={}#recorded the position of each word
revdict={}#records the word for each position
pos = 0
prev=1
a=0
m = np.zeros((367,50000000), dtype=np.int)
for i in range(12):
    print("File Number: " + '{:02d}'.format(i))
    f = open("part-r-000" + '{:02d}'.format(i),'r')#data spread across 12 files access 1 by 1
    for line in f:
        a+=1
        tweet = line.split('\t',3)
        date = tweet[2][0:8] #get date as yyyymmdd
        if int(date)>20150930:
            text = tweet[3]
            c=0
            while True:
                if c >= len(text):
                    break
                if ord(text[c])>127:#ignoring non ascii symbols (eg emojis)
                    if c<1:
                        text = text[c+1:]
                        c-=1
                    elif c<len(text)-2:
                        text = text[:c] + text[c+2:]
                        c-=1
                    else:
                        text = text[:c-1]
                        break
                c+=1
            text = text.lower()
            text = filter(None, re.split("[,\n \-!?\']+",text))#remove punctuation
            for word in text:
                if (word not in stops)& (word not in string.punctuation) & (word[0:4] != 'http'):#ignore stopwords, punctuation and links
                    if not word in dict:#new word
                        dict[word] = pos
                        revdict[pos] = word
                        loc = dates[date]
                        m[loc+1,pos] = 1#count of word for specific date
                        m[0,pos] = 1#count of each word
                        m[loc+1,0] += 1#count of words for each date
                        m[0,0] += 1#count of all words counted
                        pos += 1
                    else:
                        p = dict[word]
                        loc = dates[date]
                        m[loc+1,p] += 1                      
                        m[loc+1,0] += 1
                        m[0,p] += 1
                        m[0,0] += 1
    f.close()
    #output matrix to file
    fw = open("wordfile","w")
    for t in range(pos):
        fw.write(revdict[t])
        for day in range(367):
            fw.write(" " + str(m[day,t]))
        fw.write('\n')
    fw.close()
            

