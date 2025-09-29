class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    @property
    def positions(self):
        """Retourne la liste des positions occupées par le bateau"""
        positions = []
        for i in range(self.longueur):
            if self.vertical:
                # Bateau vertical → on incrémente la ligne
                positions.append((self.ligne + i, self.colonne))
            else:
                # Bateau horizontal → on incrémente la colonne
                positions.append((self.ligne, self.colonne + i))
        return positions
