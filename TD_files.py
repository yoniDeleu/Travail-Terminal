from file import *
"""
#Exo 2
def inverse(file):
    p=pile()
    while not f.est_vide():
        p.empile(f.defile)
    while not p.est_vide():
        file.enfile(p.depile)
    return file
#Exo 3
def separe (f):
    paire=File()
    impaire=File()
    while not f.est_vide ():
        x = f.defile()
        if x % 2 == 0:
            paire.enfile(x)
        else:
            impaire.enfile(x)
    return paire, impaire
"""
#Exo 5
def retire_dernier(file):
    file_rep = File()
    file.defile()
    while not file.est_vide():
        if file.long > 1:
            file_rep.enfile(file.defile())
    return(file_rep)