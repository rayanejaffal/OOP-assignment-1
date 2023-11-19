# OOP-assignment-1
#### Master1 Data Science
#### University of Angers
#### Course: POO et traitement des données en Python
#### Prof: Jacquelin Charbonnel

  Énoncé :: Master Data Science 1    

[Master Data Science 1](../../..)

### [Génie logiciel](../index.html)

*   *   [Généralités](../intro.html)
    *   [Processus de développement](../processus.html)
    *   [Application à Fortran](../fortran.html)
    *   [Application à Python](../python.html)
    *   Problème
        *   [Énoncé](sujet.html)
        *   [Éléments de réponse](indications.html)

Génie logiciel 2024

*   Génie logiciel
    *   [2024](../index.html)
*   Git b.a. ba
    *   [2024](../../../git_baba/2024/index.html)
*   Index
    *   [2024](../../../ds1/2024/index.html)
*   Python objet
    *   [2024](../../../python_objet/2024/index.html)
*   Unix b.a. ba
    *   [2024](../../../unix_baba/2024/index.html)

[](../../../ds1/2024/index.html)

*   [Génie logiciel](../index.html)
*   Problème
*   [Énoncé](sujet.html)

[Edit this Page](file:///users/200003833/gitwc/antora_components/genie_logiciel/starts/ds1/modules/probleme/pages/sujet.adoc)

modifié le

Énoncé
======

[](#_objectif)1\. Objectif
--------------------------

Le but est d’enrichir les fonctionnalités de 3 applications développées indépendamment les unes des autres, en faisant bénéficier chacune d’elles de fonctionnalités présentes dans les 2 autres. Il s’agit donc de réagencer un code existant (_refactoring_). Il n’est pas nécessaire de comprendre finement ce que font les différents programmes existants.

[](#_sujet)2\. Sujet
--------------------

Soit L le type _liste non vide dont les éléments sont soit tous de type `int`, soit tous de type L_. Exemple d’une liste de type L :

\[\[1,3\],\[\[2,3,4\],\[5,4,3,2\],\[\[3,1\],\[2\]\]\],\[0,9\]\]

Exemple d’une liste qui n’est pas de type L :

\[\[1,3\],\[\[2,3,4\],\[5,4,3,2\],\[\[3,1\],2\]\],\[0,9\]\]

car la sous-liste `[[3,1],2]]` n’est pas de type L. De même, la liste :

\[\[1,3\],\[\[2,3,4\],\[5,4,3,2\],\[\[\],\[2\]\]\],\[0,9\]\]

n’est pas de type L, car la sous-liste `[[],[2]]]` n’est pas de type L.

On dispose de 3 programmes réalisant chacun une opération particulière sur une liste de type L :

*   [minmax.py](_attachments/minmax.py), qui calcule le min des max des sous-listes d’une liste de type L (par exemple, pour la liste ci-dessus, les max sont 3, 4, 5, 3, 2, 9, donc le min des max est 2)
    
*   [tri.py](_attachments/tri.py), qui ordonne les éléments des sous-listes d’une liste de type L (ce qui donne pour la liste ci-dessus `[[1,3],[[2,3,4],[2,3,4,5],[[1,3],[2]]],[0,9]]`)
    
*   [prof.py](_attachments/prof.py). qui calcule la profondeur d’une liste de type L (soit 4 pour la liste ci-dessus).
    

Les listes sont spécifiées suivant la syntaxe des listes python, mais sans virgule, et avec un espace obligatoire entre les élément et les crochets. Par exemple, la liste ci-dessus est spécifiée :

\[ \[ 1 3 \] \[ \[ 2 3 4 \] \[ 5 4 3 2 \] \[ \[ 3 1 \] \[ 2 \] \] \] \[ 0 9 \] \]

Les listes à traiter ne sont pas récupérées de la même façon par les 3 programmes. Parfois la liste est spécifiée à l’appel sur la ligne de commande, parfois elle est saisie interactivement par l’utilisateur, parfois des listes à traiter sont contenues dans un fichier dont le nom est fourni sur la ligne de commande.

Question 1

Tester ces 3 programmes.

Question 2

Réécrire ces 3 programmes de façon à ce que chacun d’eux soit capable au choix de récupérer la liste à traiter depuis la ligne de commande, ou bien depuis une saise interactive de l’utilisateur, ou bien de lire des listes à traiter depuis un fichier dont le nom est spécifié sur la ligne de commande.

Plus précisément, le comportement de ces 3 applications devra être le suivant :

*   si aucun argument est fourni sur la ligne de commande, alors les listes sont demandées interactivement à l’utilisateurs,
    
*   sinon, si 1 argument unique est fourni sur la ligne de commande, alors c’est le nom du fichier dans lequel seront lues les listes (1 par ligne),
    
*   sinon les arguments fournissent la liste à traiter.
    

Ecrire ces 3 applications en factorisant le code commun dans un module, de façon à ce qu’il n’y ait pas de code dupliqué entre ces 3 applications.

Jacquelin Charbonnel   —   Support publié sous licence Creative Commons BY-NC-ND   —   2017-2023

var myDate = new Date(document.lastModified); myNewDate = new Intl.DateTimeFormat( undefined, {year: "numeric", month: "long", day: "numeric", hour: "2-digit", minute: "2-digit"} ) .format(myDate).replace(/\\./g, '-'); document.getElementById("lastmodify").innerHTML = myNewDate ;
