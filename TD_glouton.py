#TP1 sac a dos
"""
listeObjets = [[7,12], [4,11], [3,8], [3,10]]
def tri(objet):
    return objet[0]/objet[1]
listeObjets_trie = sorted(listeObjets,key = tri, reverse = True)
poidsac=0
sac=[]
#version for
for obj in listeObjets_trie:
    if poidsac + obj[1] <= 25:
        sac.append(obj)
        poidsac=poidsac+obj[1]
        
#version while
i=0
obj=listeObjets_trie[0]
while poidsac + obj[1] <= 25 and i<len(listeObjets_trie):
    sac.append(obj)
    poidsac=poidsac+obj[1]
    i=i+1
    obj=listeObjets_trie[i]
"""    
#TP2 rendu monnaie
def renduMonnaieGlouton(x):
    systeme_pieces = [200, 100, 50, 20, 10, 5, 2, 1]
    i = 0
    monnaie=[]
    while(x>0):
        if systeme_pieces[i] > x:
            i = i+1
        else:
            monnaie.append(x)
            x = x-systeme_pieces[i]
            return monnaie
renduMonnaieGlouton(100)
