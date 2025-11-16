from grille import Grille
from bateau import Bateau
from colorama import Fore, Style


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


def test_tirer():
    grid = Grille(4, 4)
    grid.ajoute(Bateau(0, 0, 2))
    grid.tirer(0, 0, "💥")
    grid.tirer(1, 0, "💥")
    grid.__str__()
    assert grid.matrice[grid.calcul_position(0, 0)] == "💥"
    assert grid.matrice[grid.calcul_position(1, 0)] == "o"


def test___str___vide(capsys):
    grid = Grille(2, 3)
    grid.__str__()
    captured = capsys.readouterr()
    attendu = "~~~\n~~~\n"
    assert captured.out == attendu


def test___str___tiré(capsys):
    grid = Grille(2, 3)
    grid.tirer(1, 2)
    grid.__str__()
    captured = capsys.readouterr()
    attendu = "~~~\n~~o\n"
    assert captured.out == attendu


def test_ajoute(capsys):
    grid = Grille(4, 4)
    grid.ajoute(Bateau(1, 1, 3))
    grid.__str__()
    captured = capsys.readouterr()
    attendu = "~~~~\n~⛵⛵⛵\n~~~~\n~~~~\n"
    assert captured.out == attendu


def test_ajoute_impossible_horizontal(capsys):
    grid = Grille(4, 4)
    grid.ajoute(Bateau(2, 2, 3))
    captured = capsys.readouterr()  # récupère stdout et stderr
    attendu = "Le bateau ne peut pas être positionné à cet endroit,il dépasse\n"
    assert captured.out == attendu


def test_ajoute_impossible_vertical(capsys):
    grid = Grille(4, 4)
    grid.ajoute(Bateau(1, 1, 4))
    captured = capsys.readouterr()  # récupère stdout et stderr
    attendu = "Le bateau ne peut pas être positionné à cet endroit,il dépasse\n"
    assert captured.out == attendu


def test_afficher(capsys):
    grid = Grille(4, 4)
    grid.tirer(1, 2)
    grid.ajoute(Bateau(2, 1, 3, True))
    grid.tirer(2, 1)
    grid.afficher()
    captured = capsys.readouterr()  # récupère stdout et stderr
    attendu = (
        "   1 2 3 4\n"
        "A  ~ ~ ~ ~\n"
        "B  ~ ~ " + Fore.BLUE + "o" + Style.RESET_ALL + " ~\n"
        "C  ~ " + Fore.RED + "x" + Style.RESET_ALL + " ~ ~\n"
        "D  ~ ~ ~ ~\n"
    )
    assert captured.out == attendu


def test_tous_bateaux_coules():
    grid = Grille(3, 3)
    grid.ajoute(Bateau(0, 0, 2))
    grid.tirer(0, 0)
    grid.tirer(0, 1)
    assert grid.tous_bateaux_coules()