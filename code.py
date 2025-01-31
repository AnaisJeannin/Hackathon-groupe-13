import numpy as np

probleme = np.array([[8,6,7],[5,0,1],[3,2,4]])

solution = np.array([[1,2,3], [4,5,6],[7,8,0]])

configurations_atteignables = [probleme]  #on ajoute toutes les configurations possibles

arrete = {} # dictionnaire avec configuration possible en clé et en valeurs la liste des configurations auxquelles elle est reliée par un mouvement élémentaire

#on trouve la position initiale du 0
for i in range(3):
    for j in range(3):
        if probleme[i][j] == 0 :
            position = np.array([i,j])
            break

voisins = [probleme] #on y met les configuartions atteignables que l'on n'a pas encore visité
mouvements_possibles = [np.array([1,0]) , np.array([-1,0]) , np.array([0,1]) , np.array([0,-1])] #mouvements élémentaires possibles

for config in voisins :
    arrete[config] = []
    for k in mouvements_possibles :
        nouvelle_position = position + k
        i , j = position[0] , position[1] 
        i_nouv , j_nouv = nouvelle_position[0], nouvelle_position[1] 
        if (i_nouv <= 2 ) and (j_nouv <= 2 ) and (i_nouv >= 0 ) and (j_nouv >= 0) :
            nouv_config = probleme.copy()
            nouv_config[i_nouv][j_nouv] , nouv_config[i][j] = probleme[i][j] , probleme[i_nouv][j_nouv]
            if nouv_config not in configurations_atteignables :
                configurations_atteignables.append(nouv_config)
                voisins.append(nouv_config)
                arrete[config].append(nouv_config)
    voisins.pop(0)
