#Exercice 1
"""
def recherche (tab, n):
    r=len(tab)
    liste = len(tab)
    for i in range (liste):
        if tab[i] == n:
            r == i
    return r

print(recherche([2,4],2))
"""
#Exercice 2

from math import sqrt

def distance(point1, point2):
    return sqrt(point1[0]-point1[1]**2 + (point2[0]-point2[1])**2)
assert distance((1, 0), (5, 3)) == 5.0,



"""
def plus_courte_distance(tab, depart):
   
    point = tab[0]
    min_dist = ...
    for i in range (1, ...):
        if distance(tab[i], depart)...:
            point = ...
            min_dist = ...
    return point

assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == [2, 5], "erreur"
"""