import random
from grille import Grille
from porte_avion import PorteAvion
from croiseur import Croiseur
from torpilleur import Torpilleur
from sous_marin import SousMarin
import fctn as fctn


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


def demander_coordonnees():
    """
    Demande à l'utilisateur une coordonnée (ex: B7) et la convertit en indices
    pour accéder à la grille (0-indexé).
    """
    while True:
        saisie = input("Entrez une coordonnée (ex: A1, B5) : ").strip().upper()

        # Vérifier que la saisie est au moins de longueur 2
        if len(saisie) < 2:
            print("Coordonnée trop courte. Réessayez.")
            continue

        # Extraire la lettre (ligne) et le reste (colonne)
        ligne_char = saisie[0]
        colonne_str = saisie[1:]

        # Vérifier que la ligne est valide
        if not ('A' <= ligne_char <= chr(ord('A') + 8 - 1)):
            print("Lettre de ligne invalide. Réessayez.")
            continue

        # Vérifier que la colonne est un nombre
        if not colonne_str.isdigit():
            print("Numéro de colonne invalide. Réessayez.")
            continue

        ligne = ord(ligne_char) - ord('A')
        colonne = int(colonne_str) - 1  # -1 car indices commencent à 0

        # Vérifier que la colonne est dans les bornes
        if colonne < 0 or colonne >= 10:
            print("Numéro de colonne hors limites. Réessayez.")
            continue

        return (ligne, colonne)


def jouer():
    grid = Grille(8, 10)
    fctn.placement_random(grid, PorteAvion)
    fctn.placement_random(grid, Croiseur)
    fctn.placement_random(grid, Torpilleur)
    fctn.placement_random(grid, SousMarin)

    coups = 0

    while not grid.tous_bateaux_coules():
        grid.afficher()
        coord = fctn.demander_coordonnees()
        resultat = grid.tirer(coord[0], coord[1])
        print(resultat)
        coups += 1

    print(f"Bravo ! Tous les bateaux sont coulés en {coups} coups.")