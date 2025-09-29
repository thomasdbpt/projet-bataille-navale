from bateau import Bateau


def test_contructeur():
    bateau1 = Bateau(1, 3)
    assert isinstance(bateau1, Bateau)


def test_positions():
    assert Bateau(2, 3, longueur=3).positions == [(2, 3), (2, 4), (2, 5)]
    assert Bateau(2, 3, longueur=3, vertical=True).positions == [(2, 3), (3, 3), (4, 3)]
