__author__ = 'han wang'

#Mar.26 2013
#Get alphabetical wordlist from a collection of novels

import os
import re

wordlist = []
filelist = []
vocal = []

#get file names
def getwordlist():
    global wordlist
    tmp = []
    names = os.walk('books')
    for root,dirs,files in names:
        for file_a in files:
            filelist.append(os.path.join(root,file_a))

    for i in range(len(filelist)):
        with open(filelist[i],'r') as f:
            for line in f:
                l = re.findall(r'[A-Za-z]+',line)
                if len(l)>0:
                    tmp += l
            wordlist += tmp
            tmp = []
    wordlist = list(set(wordlist))
    wordlist.sort()
    file('./dict.txt','w').writelines(str(wordlist))

    
if __name__ == '__main__':
    getwordlist()
    
