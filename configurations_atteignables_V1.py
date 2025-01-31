import numpy as np

probleme = [8,9,7,5,0,1,3,2,4]
probleme_t = tuple(probleme)

configurations_atteignables = set()  #on ajoute toutes les configurations possibles
configurations_atteignables.add(probleme_t)

arretes = {} # dictionnaire avec configuration possible en clé et en valeurs la liste des configurations auxquelles elle est reliée par un mouvement élémentaire
arretes[probleme_t] = []

#on trouve la position initiale du 0
def position_0(grille) :
        for i in range(9):
                if grille[i]== 0 :
                    position = np.array([i//3 , i%3])
                    indice = i
                    break
        return position , indice

voisins = [probleme] #on y met les configuartions atteignables que l'on n'a pas encore visité
mouvements_possibles = [np.array([1,0]) , np.array([-1,0]) , np.array([0,1]) , np.array([0,-1])] #mouvements élémentaires possibles

for config in voisins :
    arretes[config] = []
    position , indice = position_0(config)    
    config_t = tuple(config)
    for k in mouvements_possibles :
        nouvelle_position = position + k
        i , j = position[0] , position[1] 
        i_nouv , j_nouv = nouvelle_position[0], nouvelle_position[1] 
        indice_nouv = 3*i_nouv + j_nouv
        if (i_nouv <= 2 ) and (j_nouv <= 2 ) and (i_nouv >= 0 ) and (j_nouv >= 0) :
            nouv_config = config.copy()
            nouv_config[indice_nouv] , nouv_config[indice] = config[indice] , config[indice_nouv]
            nouv_config_t = tuple(nouv_config)
            if nouv_config_t not in configurations_atteignables :
                configurations_atteignables.add(nouv_config_t)
                voisins.append(nouv_config)
                arretes[config_t].append(nouv_config_t)
                arretes[nouv_config_t] = [config_t]

    voisins.pop(0)
