def RechercheMinMax(tab):
    if len(tab) == 0:
        return {'min': None, 'max': None}
    min, max = tab[0], tab[0]
    for i in tab:
        if i < min:
            min = i
        if i > max:
            max = i
    return {'min': min, 'max': max}


class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10, 
       Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    """Remplit le paquet de cartes"""
    def remplir(self):
        for c in range(1,5):
           for v in range(1,14):
                self.contenu.append(Carte(c,v))

    def getCarteAt(self, pos):
        assert pos < 52, 'erreur de position'
        carte = self.contenu[pos]
        return carte
