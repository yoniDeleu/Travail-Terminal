def moyenne (tab):
    n = len(tab)
    if n == 0:
        return "erreur"
    s = 0
    for v in tab:
        s = s + v
    return s / n


def tri(tab):
    i= 0
    j= len(tab) - 1
    while i != j :
        if tab[i]== 0:
            i= i + 1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j= j - 1
    return tab
