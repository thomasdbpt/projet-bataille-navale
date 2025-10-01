from bateau import Bateau
from grille import Grille
from porte_avion import PorteAvion
from croiseur import Croiseur
from torpilleur import Torpilleur
from sous_marin import SousMarin


def test_contructeur():
    bateau1 = Bateau(1, 3)
    assert isinstance(bateau1, Bateau)


def test_positions():
    assert Bateau(2, 3, longueur=3).positions == [(2, 3), (2, 4), (2, 5)]
    assert Bateau(2, 3, longueur=3, vertical=True).positions == [(2, 3), (3, 3), (4, 3)]


def test_coulé():
    grid = Grille(4, 4)
    b1 = Bateau(0, 0, 3)
    grid.ajoute(b1)
    grid.tirer(0, 0, "💥")
    grid.tirer(0, 1, "💥")
    grid.tirer(0, 2, "💥")
    grid.__str__()
    assert b1.coulé(grid) == True


def test_types_de_bateaux():
    p = PorteAvion(0, 0)
    c = Croiseur(1, 1, vertical=True)
    t = Torpilleur(2, 2)
    s = SousMarin(3, 3)

    assert p.longueur == 4 and p.marque == "🚢"
    assert c.longueur == 3 and c.marque == "⛴"
    assert t.longueur == 2 and t.marque == "🚣"
    assert s.longueur == 2 and s.marque == "🐟"
