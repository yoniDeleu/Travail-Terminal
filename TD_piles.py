"""
def creer_pile():
     Créé une pile vide
    :return: Une pile vide représentée par la liste vide
    
    return []
def est_vide(p):
     Teste si une pile est vide
    :param p: Une pile
    :return: True si p est vide, False sinon
    
    return p == []
def empiler(p, e):
     Empile un élément au sommet d'une pile
    :param p: Une pile
    :param e: Un élément
    :return: None
    :Effets: Empile e au sommet de p
    
    p.append(e)
    
def depiler(p):
     Dépile un élément au sommet d'une pile et le renvoie
    :param p: Une pile
    :return: L'élément au sommet de la pile
    :Précondition: p est non vide
    
    assert not est_vide(p), "Impossible de dépiler une pile vide"
    return p.pop()
#Exercice 1
def pile_alternee(n):
    p =creer_pile ()
    for i in range (n):
        if i % 2 == 0:
            empiler(p, i)
        else:
            empiler(p, -i)
    return p
print(pile_alternee(7))
#Exercice 2
def vider_pile(n):
    while not est_vide (p):
        depiler(n)
p=creer_pile()
empiler(p, 2)
empiler(p, 6)
empiler(p, 8)
print(p)
vider_pile(p)
print (p)
def sommet_pile(p):
    if est_vide(p):
        return None
    else:
        save = depiler(p)
        empile (p, save)
        return save
print(p)
"""
"""
#Exercice 3
def est_bien_parenthesee (n):
    p = creer_pile ()
    for i in n:
        if i=="(":
            empiler(p, i)
        else:
            if est_vide(p) == False:
                depiler(p)
            else:
                return False
    return est_vide(p)
print(est_bien_parenthesee('((())())'))
print(est_bien_parenthesee('((())'))
print(est_bien_parenthesee('())('))
"""
#Exercice 7 P1
def est_balise_fermante(html):
    dernier_element = len(html)-1
    y=html[dernier_element]
    if html[0] == "<" and html[1] == "/" and y == ">":
        return True
    else:
        return False
print(est_balise_fermante("</p>"))

def est_paire_balises(prem, deux):
    return prem[1 : len(prem)-2] == deux[2 : len(deux)-2]

#P2

