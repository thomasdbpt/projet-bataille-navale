import fctn as fctn
from unittest.mock import patch


def test_demander_coordonnees():
    # Simule l'entrée "B7"
    with patch("builtins.input", return_value="B3"):
        x, y = fctn.demander_coordonnees()
        assert x == 1  # ligne B -> index 1
        assert y == 2  # colonne 7 -> index 6
