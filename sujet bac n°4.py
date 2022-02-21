def recherche(tab):
    couples = []
    if len(tab) > 1:
        a = 0
        while a < len(tab)-1:
            if tab[a] == tab[a+1] - 1:
                couples.append((tab[a], tab[a+1]))
            a += 1
    return couples
print(recherche([1,3,7,5]))
