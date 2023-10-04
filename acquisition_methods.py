#!/bin/env python3
#module
#acquisition_methods
import sys
import re
"""
si aucun argument est fourni sur la ligne de commande, alors les listes sont demandées interactivement à l’utilisateurs,

sinon, si 1 argument unique est fourni sur la ligne de commande, alors c’est le nom du fichier dans lequel seront lues les listes (1 par ligne),

sinon les arguments fournissent la liste à traiter.

"""
def read_list(): #détermine la méthode d'acquisition
  if len(sys.argv) == 1:
      return read_list_interactively()
  elif len(sys.argv) == 2:
    return read_list_from_file(sys.argv[1]) 
  else:
    return read_list_argument()
    
def read_list_interactively(): #lire la list interactivement
    l = []
    i = 0
    def mklist(l0):
        nonlocal i
        l = []          # sous-liste courante
        while True:
            if l0[i]=="[":   # c'est une sous-liste de listes
                i+=1                 
                if i!=1:             # pour la premiÃ¨re sous-liste, on ne fait rien
                    l.append(mklist(l0))    # sinon on construit cette sous-liste et on la met dans la sous-liste courante
            elif l0[i]=="]": # c'est la fin de la sous-liste courante,
                i+=1
                return l             # on renvoie la sous-liste courante
            else:                  # c'est une sous-liste d'entiers
                l.append(int(l0[i]))   
                i+=1
    while True:
        line = input("? ").rstrip("\n").strip()
        if line == "":
            break
        lline = re.split(r' +',line.rstrip("\n"))
        l = mklist(lline)
    return l
    
def read_list_from_file(l0): #lire la liste du fichier
    l = []
    def _build(l0):
        nonlocal i
        l = []          # sous-liste courante
        while True:
            if l0[i]=="[":   # c'est une sous-liste de listes
                i+=1                 
                if i!=1:             # pour la premiÃ¨re sous-liste, on ne fait rien
                    l.append(_build(l0))    # sinon on construit cette sous-liste et on la met dans la sous-liste courante
            elif l0[i]=="]": # c'est la fin de la sous-liste courante,
                i+=1
                return l             # on renvoie la sous-liste courante
            else:                  # c'est une sous-liste d'entiers
                l.append(int(l0[i]))   
                i+=1
    i = 0
    f = open(sys.argv[1], "r")
    for line in f:
        lline = re.split(r' +',line.rstrip("\n"))
        l = _build(lline)
    return l
    res = _build()
    return res


def read_list_argument(): #lire la liste des arguments
    def _construire():
        nonlocal i  
        l = []          
        while True:
            if sys.argv[i]=="[":   
                i+=1               
                if i!=2:                  # pour la premiÃ¨re liste, on ne fait rien
                    l.append(_construire()) 
            elif sys.argv[i]=="]":        # c'est la fin de la liste,
                i+=1
                return l                  # on renvoie la liste constuite
            else:                         # c'est une liste d'entiers
                l.append(int(sys.argv[i]))   
                i+=1
    i = 1                              # indice pour parcourir les arguments
    return _construire()
