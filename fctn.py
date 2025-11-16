import random
from grille import Grille
from porte_avion import PorteAvion
from croiseur import Croiseur
from torpilleur import Torpilleur
from sous_marin import SousMarin


def placement_random(grille, bateau_class):
    while True:
        # Choix aléatoire de la position et orientation
        ligne = random.randint(0, grille.nombre_lignes - 1)
        colonne = random.randint(0, grille.nombre_colonnes - 1)
        vertical = random.choice([True, False])

        # Création du bateau
        bateau = bateau_class(ligne, colonne, vertical)

        # Vérifie si toutes les positions sont libres
        if all(
            0 <= x < grille.nombre_lignes and 
            0 <= y < grille.nombre_colonnes and 
            grille.matrice[grille.calcul_position(x, y)] == grille.vide
            for (x, y) in bateau.positions
        ):
            grille.ajoute(bateau)
            return bateau
