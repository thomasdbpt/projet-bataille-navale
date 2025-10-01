from grille import Grille
from bateau import Bateau


grid = Grille(4, 4)
grid.tirer(1, 2)
grid.__str__()
grid.ajoute(Bateau(1, 1, 3, True))
grid.__str__()
