from grille import Grille


def test_constructeur():
    grid = Grille(5, 4)
    assert isinstance(grid, Grille)


def test_calcul_position():
    grid = Grille(5, 4)
    assert grid.calcul_position(3, 2) == grid.nombre_colonnes * 3 + 2


def test_zeros():
    grid = Grille(5, 4)
    for i in grid.matrice:
        assert i == "~"


def test_tir():
    grid = Grille(3, 4)
    grid.tirer(2, 3)
    assert grid.matrice[grid.calcul_position(2, 3)] == "x"


def test___str___vide(capsys):
    grid = Grille(2, 3)
    grid.__str__()
    captured = capsys.readouterr()  # récupère stdout et stderr
    attendu = "~~~\n~~~\n"
    assert captured.out == attendu


def test___str___tiré(capsys):
    grid = Grille(2, 3)
    grid.tirer(1, 2)
    grid.__str__()
    captured = capsys.readouterr()  # récupère stdout et stderr
    attendu = "~~~\n~~x\n"
    assert captured.out == attendu
