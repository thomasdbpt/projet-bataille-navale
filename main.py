from grille import Grille
from bateau import Bateau
from porte_avion import PorteAvion
from croiseur import Croiseur
from torpilleur import Torpilleur
from sous_marin import SousMarin
import fctn as fctn

grid = Grille(8, 10)
grid.afficher()
fctn.placement_random(grid, PorteAvion)
grid.afficher(True)