import sys
import re
import string
import collections
import numpy as np
import os
import shutil

#This program filters each tweet so that only relevant tweets are remaining. 

#List of selected keywords
keywords=['referendum','brexit','immigration','farage','independence','boris','sovereignty','sturgeon','#voteleave','#strongerin','#voteremain','#leaveeu']

outfile = open('reltweets','w')

for i in range(12):
    #Tweets split across 12 different files, these must be 1 by 1 copied, used and deleted
    print("File Number: " + '{:02d}'.format(i))
    shutil.copy("/home/zcabtpa/part-r-000"+'{:02d}'.format(i),".")
    f = open("part-r-000" + '{:02d}'.format(i),'r')
    for line in f:
    
        tweet = line.split('\t',3)
        date = tweet[2][0:10]
        if int(date)>2015093024:
            text = tweet[3]
            text = text.lower()
            for w in keywords:
                if text.find(w)!=-1:#If we find the word within the text of the tweet  
                    #write to file
                    outfile.write(date +"\t"+ text) #We only keep important data: date and text
                    break
                      
    f.close()
    os.remove("part-r-000" + '{:02d}'.format(i)) #Remove the data file
outfile.close()            
