from grille import Grille


def test_constructeur():
    grid = Grille(5, 4)
    assert isinstance(grid, Grille)


def test_zeros():
    grid = Grille(5, 4)
    for i in grid.matrice:
        assert i == 0
