import sys
import re
import os
import shutil
import string
import collections
import nltk
import json
import numpy as np
from nltk.corpus import stopwords

#This program is used to collect the frequency of each established keyword in each outlet for each hour across the year. The output is a time series for each keyword. 

source = sys.argv[1] # The name of the news outlet is given as the argument to this such that it can be run by a script which calls each of the news outlets. This is because otherwise we ran out of memory. 
dates = {}
fd = open("/home/zcabtpa/dates",'r') #Get the list of dates
i = 0
for dateline in fd:
    dates[dateline[0:8]] = i
    i+=1
fd.close()
for i in range(1):
    print("File Number: " + '{:02d}'.format(i))
    shutil.copy("/home/zcabtpa/bbc_juicer_data_20151001_20161001_filter_url.jsonl", ".") #So large we must copy to local folder
    f = open("bbc_juicer_data_20151001_20161001_filter_url.jsonl",'r')
    dict = ['referendum','brexit','immigration','farage','independence','boris','sovereignty','sturgeon','leave','remain']#list of keywords
    m = np.zeros((366*24+1,len(dict)), dtype=np.int)
    for line in f:
        l = json.loads(line)
        src = l["source"]
        date = l["published"]
        date = date[0:4]+date[5:7]+date[8:10]+date[11:13]
        if (int(date)>2015093024)&(src == source):
            text = l["text"]
            #search text for keywords
            text = text.lower()
            
            for i in range(len(dict)):
                if text.find(dict[i])!=-1:
                        loc = dates[date[0:8]]*24+int(date[8:10])
                        m[loc+1,i] += 1                      
                        m[0,i] += 1
                        #Where we find a keyword we add one to the frequency for that keyword at that hour
    f.close()
    fw = open("articlefile" + source,"w")
    #Write output to file
    for t in range(len(dict)):
        fw.write(dict[t])
        for day in range(366*24+1):
            fw.write(" " + str(m[day,t]))
        fw.write('\n')
    fw.close()
            
