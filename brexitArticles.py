import sys
import re
import string
import collections
import numpy as np
import os
import shutil
import json

#This program is used to find the relevant articles for usage in the study. It outputs a copy of the data, with irrelevant articles removed.

#List of keywords established. Although hashtags are unlikely within news articles, they are included nonetheless
keywords=['referendum','brexit','immigration','farage','independence','boris','sovereignty','sturgeon','#voteleave','#strongerin','#voteremain','#leaveeu']

outfile = open('relarticles','w')

for i in range(1):
    shutil.copy("/home/zcabtpa/bbc_juicer_data_20151001_20161001_filter_url.jsonl",".")#copy data to local folder
    f = open("bbc_juicer_data_20151001_20161001_filter_url.jsonl",'r')
    for line in f:
        article=json.loads(line)
        date = article["published"]
        date = date[0:4]+date[5:7]+date[8:10]+date[11:13]
        #putting date into format yyyymmddhh
                
        if int(date)>2015093024:
            src = article["source"]
            text = article["text"]
            text = text.lower()
            for w in keywords:
                if text.find(w)!=-1:  #If keyword within article
                    #write to file
                    #We need to mark end of article, as we are no longer using json formal. So @@@@@@@ is appended.
                    outfile.write(src + "\t" + date +"\t"+ text + "@@@@@@@\n")
                    break
                    
                
    f.close()
    os.remove("bbc_juicer_data_20151001_20161001_filter_url.jsonl")
outfile.close()            
