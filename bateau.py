class Bateau:
    def __init__(self, ligne, colonne, longueur=1, marque="⛵", vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.marque = marque
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

    def coulé(self, grille):
        for (x, y) in self.positions:
            if grille.matrice[grille.calcul_position(x, y)] != "💥":
                return False
        return True
