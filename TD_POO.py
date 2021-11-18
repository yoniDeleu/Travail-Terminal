import random
class Personnage:

    def __init__(self, nom , points_de_vie):
        self.vie = points_de_vie
        self.nom = nom

    def perd_vie(self):
        if random.random() < 0.5:
            nbPoint = 1
        else:
            nbPoint = 2
        self.vie = self.vie - nbPoint
        return nbPoint
        
bilbo = Personnage("Bilbo", 20)
gollum = Personnage("Gollum", 20)
frodon = Personnage("Frodon", 20)
araignee = Personnage("Araignée", 10)
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