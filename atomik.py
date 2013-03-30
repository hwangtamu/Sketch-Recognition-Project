__author__ = 'han wang'

import re

keyboard = {}
sample = {}

def layout():
    keyboard['b'] = (0,0,1,1)
    keyboard['d'] = (0,1,1,2)
    keyboard['k'] = (0,2,1,3)
    keyboard['g'] = (0,3,1,4)
    keyboard['c'] = (1,0,2,1)
    keyboard['a'] = (1,1,2,2)
    keyboard['n'] = (1,2,2,3)
    keyboard['i'] = (1,3,2,4)
    keyboard['m'] = (1,4,2,5)
    keyboard['q'] = (1,5,2,6)
    keyboard['f'] = (2,0,3,1)
    keyboard['l'] = (2,1,3,2)
    keyboard['e'] = (2,2,3,3)
    keyboard['s'] = (2,3,3,4)
    keyboard['y'] = (2,4,3,5)
    keyboard['x'] = (2,5,3,6)
    keyboard['j'] = (3,0,4,1)
    keyboard['h'] = (3,1,4,2)
    keyboard['t'] = (3,2,4,3)
    keyboard['o'] = (3,3,4,4)
    keyboard['p'] = (3,4,4,5)
    keyboard['v'] = (3,5,4,6)
    keyboard['r'] = (4,2,5,3)
    keyboard['w'] = (4,3,5,4)
    keyboard['u'] = (4,4,5,5)
    keyboard['z'] = (4,5,5,6)

def mapping():
    with open('dict.txt') as f:
        for line in f:
            tmp = re.findall(r'[A-Za-z]+',line)
    
    for item in tmp:
        sample[item] = []
        for letter in item:
            pos = (keyboard[letter.lower()][0]+0.5,keyboard[letter.lower()][1]+0.5)
            sample[item].append(pos)
            
    file('./data.txt','w').writelines(str(sample))
        

if __name__ == '__main__':
    layout()
    mapping()
