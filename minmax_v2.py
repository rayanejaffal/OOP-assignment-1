#!/bin/env python3
import sys
from acquisition_methods import read_list
def minmax(l):

    if type(l[0])==int:
        maxi.append(max(l))
    else:
        for i in l:
            minmax(i)

if __name__=="__main__":
    # programme principal
    l = read_list()                   # rÃ©cupÃ©ration de la liste
    maxi = []
    minmax(l)
    print(min(maxi))
