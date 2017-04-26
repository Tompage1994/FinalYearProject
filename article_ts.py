import sys
import re
import os
import shutil
import string
import collections
import json
import numpy as np

#This program is run to create a time series of the number of articles from each news outlet

dates = {}
#Get the list of dates
fd = open("/home/zcabtpa/dates",'r')
i = 0
for dateline in fd:
    dates[dateline[0:8]] = i
    i+=1
fd.close()
for i in range(1):
    print("File Number: " + '{:02d}'.format(i))
    #Such a large file we need to copy this locally at runtime
    shutil.copy("/home/zcabtpa/bbc_juicer_data_20151001_20161001_filter_url.jsonl", ".")
    f = open("bbc_juicer_data_20151001_20161001_filter_url.jsonl",'r')
    outlets=["Metro", "BBC News","The Mirror","Daily Mail","The Guardian","Sky News","The Daily Telegraph","Daily Express","London Evening Standard"]      
    m = np.zeros((366*24+1,9), dtype=np.int)
    for line in f:
        l = json.loads(line)
        src = l["source"]
        date = l["published"]
        #alter date to be in format 'yyyymmddhh'
        date = date[0:4]+date[5:7]+date[8:10]+date[11:13] 
        if (int(date)>2015093024):
            #select location within matrix
            loc = dates[date[0:8]]*24+int(date[8:10])
            i = outlets.index(src)
            m[loc+1,i] += 1 #Increase frequency at this time               
            m[0,i] += 1 #Total count of articles for each time
    f.close()
    fw = open("articlefile","w")
    #write to file
    for t in range(9):
        fw.write(outlets[t])
        for day in range(366*24+1):
            fw.write(" " + str(m[day,t]))
        fw.write('\n')
    fw.close() 
            
