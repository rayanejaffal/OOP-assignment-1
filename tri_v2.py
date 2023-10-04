#!/bin/env python3
import sys, re
from acquisition_methods import read_list

def tri(l):

    if type(l[0])==int:
        l.sort()
    else:
        for i in l:
            tri(i)

if __name__=="__main__":
    # programme principal
        l = read_list()                      # rÃ©cupÃ©ration de la liste
        tri(l)
        print(f"{l=}")
