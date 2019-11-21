#isrichard 02
#Richard Heilbron
#​CSCI 102 – Section C
#Week 11 - Part A

def PrintOutput(f):
    result = f
    print('OUTPUT',result)

import string
def LoadFile(x):
    with open(x, 'r') as f:
        ending = f.readlines()
        re = []
        for i in ending:
            temp = ''
            for j in i:
                if j in string.ascii_letters or j == ' ':
                    temp +=j
            re.append(temp)            
    return(re)

def UpdateString(x,y,z):
    new_word = ''
    for i in range(len(x)):
        if i ==z:
            new_word += y
        else:
            new_word += x[i]
    return(new_word)
def FindWordCount(x,y):
    count = 0
    for i in x:
        k = i.split()
        for j in k:
            if (j.upper()) in (y.upper()):
                if y.upper() in j.upper():
                    count += 1
def ScoreFinder(x,y,z):
    idex = 0
    for i in x:
        idex += 1
        if i.upper() == z.upper():
            who = index
    return(z, 'got a score of', y[who])



