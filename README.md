# Hackathon-groupe-13


Nous avons choisi le sujet Takin.



Pour étudier ce problème, on a réparti différentes tâches sur différents fichiers.
Ainsi, le fichier config_initial permet de créer une configuration aléatoire de l'état du jeu et donc d'initialiser les parties.

Ensuite, il fallait déterminer toutes les configurations attaignables depuis le problème initial. Les différents essais sont documentés dans 3 fichier :
 - un fichier configurations_atteignables_V0.py 
 - un fichier configurations_atteignables_V1.py
 - un fichier configurations_atteignables_avec_heapq.py qui permet d'établir une liste de toutes les configurations du jeu, et détermine lesquelles sont voisines
Les versions V0 et V1 ont à peu près le même fonctionnement mais la 'pile' utilisée ne fonctionne pas. C'est pour cela qu'on a ensuite utilisé la librairie heapq.

Le fichier Dijkstra comporte l'algorithme Dijkstra qui correspond à la recherche d'un chemin possible entre la configuration initiale (123456780) et la configuration finale (qui correspond en fait à la manière dont le jeu a été initialisé). Il permet aussi d'afficher les coups successifs (ou le fait qu'il n'a pas trouvé de solution).

Le fichier interface_graphique.py permet de faire l'interface graphique. (il n'affiche que la configuration que l'on souhaite atteindre)

Enfin, le fichier Le_tout.ipynb regroupe tous les fichiers (sauf celui de l'interface graphique) pour résoudre le problème.




Projet réalisé par Lise, Anaïs et Laure.


```python

```
