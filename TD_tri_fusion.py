def tri_fusion(liste):
    """
    Premièrement on découpe la liste initial en sous-liste ensuite on tri les sous-listes
    chaqu'un de leur coté puis on fusionne en triant les sous-listes entre elles
    """
    if len(liste) < 2 : #cas de base
        return liste
    else :
        liste1, liste2 = coupe (liste) #Etape 1 
        liste1 = tri_fusion(liste1) #Etape 2
        liste2 = tri_fusion(liste2)
        return fusion (liste1, liste2) #Etape 3













def coupe(liste)