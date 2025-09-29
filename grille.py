class Grille:
    def __init__(self, nombre_lignes, nombre_colonnes):
        self.matrice = [0 * (nombre_lignes * nombre_colonnes)]
        self.nombre_colonnes = nombre_colonnes

    def tirer(self, x, y):
        if self.matrice[self.nombre_colonnes * x + y] == 0:
            self.matrice[self.nombre_colonnes * x + y] = 1
        else:
            return False

    def afficher(self):
        print(self.matrice)
