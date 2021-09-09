import random
grande_liste=[random.randrange(100) for i in range(100)]
grande_liste.sort()
print(grande_liste)

def recherche_dichotomique(liste,valeur):
    gauche=0
    droite=len(liste)-1
    while gauche <= droite:
        pivot=(gauche+droite)//2
        if pivot == valeur:
            return True
        elif liste[pivot] < valeur:
            gauche=pivot+1
        elif liste[pivot] > valeur:
            droite=pivot-1
    return False
print(recherche_dichotomique(grande_liste,15))