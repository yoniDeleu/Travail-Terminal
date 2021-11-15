#Exercice 1
"""
def somme_recursif(n):
    if n == 0 :
        return 0
    else : 
        return n + somme_recursif(n-1)
somme_recursif(100)
"""

"""
def somme_iteratif(n):
    f = 0
    while n != 0:
        f = f + n
        n = n - 1
    return f
print(somme_iteratif(100))
import timeit
timeit.timeit('somme_recursif(1000)', number=50, setup="from __main__ import somme_recursif")
"""
#Exercice 3
"""
#3)
def factorielle (n):
    if n == 0:
        return 1
    else:
        return n * factorielle (n-1)
"""
#Exercice 7.1
"""
def nbr_de_chiffre(x):
    if x < 10:
        return 1
    else:
        return nbr_de_chiffre(x//10) + 1

print(nbr_de_chiffre(34639))
"""
#Exercice 8
"""
def appartient (liste,mot,i):
    if liste[i] == mot:
        return True
    elif i == len(liste) -1
        return False
    else:
        appartient(liste,mot,i+1)
"""
#Exercice 9
def est_palindrome(sofiane):
    