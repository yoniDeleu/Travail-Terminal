vélos = {"id":12358,"typ":"classique","station":"lol","statut":"dispo"}
#1)
vélos["typ"]="electrique"
vélos["id"]=1210
vélos["station"]="place italie"
vélos["statut"]="en panne"
"dispo" in vélos.values()
print(vélos)

#Exo 2
vélo1={"id":12357,"typ":"classique","station":"zimbabwai","statut":"dispo"}
vélo2={"id":12358,"typ":"electrique","station":"paris","statut":"en déplacement"}
vélo3={"id":12359,"typ":"classique","station":"italie","statut":"en panne"}

parc_vélib