# plouf dans l'eau

from grille import Grille  # import du constructeur Grille de la classe grille

grid = Grille(5, 8)  # on crée une grille de 5 lignes et 8 colonnes
compteur = 0   # comteur pour stopper le jeu après quelques coups de test
while compteur < 5:
    grid.afficher()
    x, y = ask_coordonnées()  # on demande à l'utilisateur quel case il veut tirer 
    grid.tirer(x, y)
    compteur += 1
