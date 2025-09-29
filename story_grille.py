# plouf dans l'eau

from grille import Grille  # import du constructeur Grille de la classe grille

grid = Grille(5, 8)  # on crée une grille de 5 lignes et 8 colonnes
compteur = 0   # comteur pour stopper le jeu après quelques coups de test
while compteur < 3:
    grid.__str__()
    x = int(input("donne moi la coordonnée x de la case que tu veux toucher"))  # on demande à l'utilisateur quel case il veut tirer 
    y = int(input("donne moi la coordonnée y de la case que tu veux toucher"))
    grid.tirer(x, y)
    compteur += 1

grid.__str__()
