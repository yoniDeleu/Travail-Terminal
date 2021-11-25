#Exercice 3
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
"""
"""
#Exerice 2.2
from math import sqrt
class Triangle_rectangle:
    def __init__(self, cote1,cote2):
        self.cote1 = cote1
        self.cote2 = cote2
        self.hypothenuse = sqrt(self.cote1**2 + self.cote2**2)
        
    def get_cote1(self):
        return self.cote1
    
    def get_cote2(self):
        return self.cote2
    
    def get_hypothenuse(self):
        return self.hypothenuse
    
    def set_cote1(self,nbr):
        self.cote1 = nbr
        self.hypothenuse = sqrt(self.cote1**2 + self.cote2**2)
        
    def set_cote2(self,nbr):
        self.cote2 = nbr
        self.hypothenuse = sqrt(self.cote1**2 + self.cote2**2)
        
triangle = Triangle_rectangle(5,5)
print(triangle.cote1)
print(triangle.cote2)
print(triangle.hypothenuse)

#Exercice 4
import math
class Point:
    def __init__(self,x,y):
        self.coor_abs = x
        self.coor_ord = y
        
    def __repr__(self):
        return "(" +str(self.coor_abs)+ "," +str(self.coor_ord)+ ")"
 
A=Point(-2, 5)
"""
class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
    
    def __repr__(self):
        if self.denom == 1:
            return str(slef.num)
        else:
            return str(self.num) + "/" + str(self.denom)

    def __eq__(self, frac2):
        if self.num / self.denom == frac2.num / frac2.denom:
            return True
        else:
            return False
        
    def __lt__(self, frac2):
        if self.num / self.denom < frac2.num / frac2.denom:
            return True
        else:
            return False
        
    def __add__(self, frac):
        if self.num==self.denom:
            return (self.num + frac2.num) / self.denom
        else:
            return (self.num * frac2.denom
    
    
    
    
    
A=Fraction(12, 35)