# OOP-assignment-1
Master1 Data Science 
University of Angers
Course: POO et traitement des données en Python
Prof: Jacquelin Charbonnel

Énoncé
1. Objectif
Le but est d’enrichir les fonctionnalités de 3 applications développées indépendamment les unes des autres, en faisant bénéficier chacune d’elles de fonctionnalités présentes dans les 2 autres. Il s’agit donc de réagencer un code existant (refactoring). Il n’est pas nécessaire de comprendre finement ce que font les différents programmes existants.

2. Sujet
Soit L le type liste non vide dont les éléments sont soit tous de type int, soit tous de type L. Exemple d’une liste de type L :

[[1,3],[[2,3,4],[5,4,3,2],[[3,1],[2]]],[0,9]]
Exemple d’une liste qui n’est pas de type L :

[[1,3],[[2,3,4],[5,4,3,2],[[3,1],2]],[0,9]]
car la sous-liste [[3,1],2]] n’est pas de type L. De même, la liste :

[[1,3],[[2,3,4],[5,4,3,2],[[],[2]]],[0,9]]
n’est pas de type L, car la sous-liste [[],[2]]] n’est pas de type L.

On dispose de 3 programmes réalisant chacun une opération particulière sur une liste de type L :

minmax.py, qui calcule le min des max des sous-listes d’une liste de type L (par exemple, pour la liste ci-dessus, les max sont 3, 4, 5, 3, 2, 9, donc le min des max est 2)

tri.py, qui ordonne les éléments des sous-listes d’une liste de type L (ce qui donne pour la liste ci-dessus [[1,3],[[2,3,4],[2,3,4,5],[[1,3],[2]]],[0,9]])

prof.py. qui calcule la profondeur d’une liste de type L (soit 4 pour la liste ci-dessus).

Les listes sont spécifiées suivant la syntaxe des listes python, mais sans virgule, et avec un espace obligatoire entre les élément et les crochets. Par exemple, la liste ci-dessus est spécifiée :

[ [ 1 3 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
Les listes à traiter ne sont pas récupérées de la même façon par les 3 programmes. Parfois la liste est spécifiée à l’appel sur la ligne de commande, parfois elle est saisie interactivement par l’utilisateur, parfois des listes à traiter sont contenues dans un fichier dont le nom est fourni sur la ligne de commande.

Question 1
Tester ces 3 programmes.

Question 2
Réécrire ces 3 programmes de façon à ce que chacun d’eux soit capable au choix de récupérer la liste à traiter depuis la ligne de commande, ou bien depuis une saise interactive de l’utilisateur, ou bien de lire des listes à traiter depuis un fichier dont le nom est spécifié sur la ligne de commande.

Plus précisément, le comportement de ces 3 applications devra être le suivant :

si aucun argument est fourni sur la ligne de commande, alors les listes sont demandées interactivement à l’utilisateurs,

sinon, si 1 argument unique est fourni sur la ligne de commande, alors c’est le nom du fichier dans lequel seront lues les listes (1 par ligne),

sinon les arguments fournissent la liste à traiter.

Ecrire ces 3 applications en factorisant le code commun dans un module, de façon à ce qu’il n’y ait pas de code dupliqué entre ces 3 applications.
