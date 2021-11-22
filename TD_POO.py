"""
import random
class Personnage:

    def __init__(self, nom , points_de_vie , force):
        self.vie = points_de_vie
        self.nom = nom
        self.force = force
        
    def perd_vie(self, adversaire):
        coup = random.randint(1, adversaire.force)
        self.vie = self.vie - coup
        return coup
        
bilbo = Personnage("Bilbo", 20, 3)
gollum = Personnage("Gollum", 20 , 4)
frodon = Personnage("Frodon", 20 , 10)
araignee = Personnage("Araignee", 10 , 7)
aragorn = Personnage("Aragorn", 10 , 6)
orc = Personnage("Orc", 10 , 9)
    
def game(combattant1, combattant2):

    while combattant1.vie > 0 and combattant2.vie > 0:
        coup = combattant1.perd_vie(combattant2)
        print(combattant1.nom + " perd " + str(coup) + " point de vie")
        coup = combattant2.perd_vie(combattant1)
        print(combattant2.nom + " perd " + str(coup) + " point de vie")
        
    if combattant1.vie <= 0 and combattant2.vie > 0:
        msg = combattant2.nom + " est vainqueur, il lui reste encore " + str(combattant2.vie) + " points de vie alors que " + combattant1.nom + " est mort"
    elif combattant2.vie <= 0 and combattant1.vie > 0:
        msg = combattant1.nom + " est vainqueur, il lui reste encore " + str(combattant1.vie) + " points de vie alors que " + combattant2.nom + " est mort"
    else:
        msg = "Les deux combattants sont morts en même temps"
    return msg
print(game(aragorn, orc))
"""
import random
class Personnage:

    def __init__(self, nom , points_de_vie):
        self.vie = points_de_vie
        self.nom = nom

    def perd_vie(self):
        coup_critique = random.random()
        if random.random() < 0.5:
            nbPoint = 1
            if coup_critique > 0.95:
                nbPoint = nbPoint * 5
        else:
            nbPoint = 2
            if coup_critique > 0.95:
                nbPoint = nbPoint * 5
        self.vie = self.vie - nbPoint
        return nbPoint

bilbo = Personnage("Bilbo", 20)
gollum = Personnage("Gollum", 20)
frodon = Personnage("Frodon", 20)
araignee = Personnage("Araignee", 10)
aragorn = Personnage("Aragorn", 10)
orc = Personnage("Orc", 10)
    
def game(combattant1, combattant2):

    while combattant1.vie > 0 and combattant2.vie > 0:
        P1=combattant1.perd_vie()
        print(combattant1.nom + " perd " + str(P1) + " point de vie")
        P2=combattant2.perd_vie()
        print(combattant2.nom + " perd " + str(P2) + " point de vie")
        
    if combattant1.vie <= 0 and combattant2.vie > 0:
        msg = combattant2.nom + " est vainqueur, il lui reste encore " + str(combattant2.vie) + " points de vie alors que " + combattant1.nom + " est mort"
    elif combattant2.vie <= 0 and combattant1.vie > 0:
        msg = combattant1.nom + " est vainqueur, il lui reste encore " + str(combattant1.vie) + " points de vie alors que " + combattant2.nom + " est mort"
    else:
        msg = "Les deux combattants sont morts en même temps"
    return msg
print(game(aragorn, orc))