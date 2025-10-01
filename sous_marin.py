from bateau import Bateau


class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, marque="🐟", vertical=vertical)
