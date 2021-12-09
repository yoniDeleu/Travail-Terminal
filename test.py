"""
velos = {"id":12358,"typ":"classique","station":"lol","statut":"dispo"}
#1)
velos["typ"]="electrique"
velos["id"]=1210
velos["station"]="place italie"
velos["statut"]="en panne"
"dispo" in velos.values()
print(velos)
"""
#Exo 2
velo1={"id":12357,"typ":"classique","station":"zimbabwai","statut":"en déplacement"}
velo2={"id":12358,"typ":"electrique","station":"paris","statut":"dispo"}
velo3={"id":12359,"typ":"classique","station":"italie","statut":"en panne"}

parc_velib = []
parc_velib.append(velo1)
parc_velib.append(velo2)
parc_velib.append(velo3)
print(parc_velib)

def recherche_velo(parc_velib):
    for velo in parc_velib:
        if velo["statut"] == "en déplacement":
            return True
        else:
            return False
print(recherche_velo(parc_velib))

def recherche_velo_bis(parc_velib):
    for velo in parc_velib:
        if velo["statut"] == "dispo":
            return velo["station"]
        else:
            return None
print(recherche_velo_bis(parc_velib))