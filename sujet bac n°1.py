#Ex 1
def recherche (caractere, mot):
    cpt=0
    for e in mot:
        if e==caractere:
            cpt=cpt+1
    return cpt


#Ex 2
pieces=[100,50,20,10,5,2,1]
def rendu_glouton(arendre,solution=[],i=0):
    if arendre==0:
        return solution
    p=pieces[i]
    if p<=arendre:
        solution.append(p)
        return rendu_glouton(arendre-p,solution,i)
    else:
        return rendu_glouton(arendre,solution,i+1)
    
print(rendu_glouton(291,[],0))