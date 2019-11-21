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
