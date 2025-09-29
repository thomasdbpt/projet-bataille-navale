class Grille:
    def __init__(self, nombre_lignes, nombre_colonnes):
        self.vide = "~"
        self.shot = "x"
        self.matrice = [self.vide] * (nombre_lignes * nombre_colonnes)
        self.nombre_colonnes = nombre_colonnes

    def calcul_position(self, x, y):
        return self.nombre_colonnes * x + y

    def tirer(self, x, y):
        if self.matrice[self.calcul_position(x, y)] == self.vide:
            self.matrice[self.calcul_position(x, y)] = self.shot
        else:
            return False

    def afficher(self):
        print(self.matrice)

    def __str__(self):
        c = self.nombre_colonnes
        for i in range(int(len(self.matrice) / self.nombre_colonnes)):
            print("".join(self.matrice[i * c:(i + 1) * c]))
