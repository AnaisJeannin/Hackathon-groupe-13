import numpy as np

probleme = [8,9,7,5,0,1,3,2,4]

solution = [1,2,3,4,5,6,7,8,0]

configurations_atteignables = set(probleme)  #on ajoute toutes les configurations possibles

arrete = {} # dictionnaire avec configuration possible en clé et en valeurs la liste des configurations auxquelles elle est reliée par un mouvement élémentaire

#on trouve la position initiale du 0
for i in range(9):
        if probleme[i]== 0 :
            position = [i//3 , i%3]
            indice = i
            break

voisins = [probleme] #on y met les configuartions atteignables que l'on n'a pas encore visité
mouvements_possibles = [np.array([1,0]) , np.array([-1,0]) , np.array([0,1]) , np.array([0,-1])] #mouvements élémentaires possibles

for config in voisins :
    arrete[config] = []
    for k in mouvements_possibles :
        nouvelle_position = position + k
        i , j = position[0] , position[1] 
        i_nouv , j_nouv = nouvelle_position[0], nouvelle_position[1] 
        indice_nouv = 3*i_nouv + j_nouv
        if (i_nouv <= 2 ) and (j_nouv <= 2 ) and (i_nouv >= 0 ) and (j_nouv >= 0) :
            nouv_config = probleme.copy()
            nouv_config[indice_nouv] , nouv_config[indice] = probleme[indice] , probleme[indice_nouv]
           
            configurations_atteignables.add(nouv_config)
            voisins.append(nouv_config)
            arrete[config].append(nouv_config)

    voisins.pop(0)
    