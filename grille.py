class Grille:
    def __init__(self, nombre_lignes, nombre_colonnes):
        self.vide = "~"
        self.shot = "x"
        self.matrice = [self.vide] * (nombre_lignes * nombre_colonnes)
        self.nombre_colonnes = nombre_colonnes
        self.nombre_lignes = nombre_lignes

    def calcul_position(self, x, y):
        return self.nombre_colonnes * x + y

    def tirer(self, x, y, touche="x"):
        # Vérifier que le tir est dans les bornes
        if x < 0 or x >= self.nombre_lignes or y < 0 or y >= self.nombre_colonnes:
            print("Tir en dehors de la grille !")
            return

        index = self.calcul_position(x, y)

        if self.matrice[index] == "⛵":
            self.matrice[index] = touche
        elif self.matrice[index] == "~":
            self.matrice[index] = "o"
        else:
            print("Cette case a déjà été tirée.")

    def afficher(self):
        print(self.matrice)

    def __str__(self):
        nb_colonnes = self.nombre_colonnes
        for i in range(self.nombre_lignes):
            print("".join(self.matrice[i * nb_colonnes:(i + 1) * nb_colonnes]))

    def ajoute(self, bateau):
        if bateau.positions[-1][0] <= (self.nombre_lignes - 1) and bateau.positions[-1][1] <= (self.nombre_colonnes - 1):
            for (x, y) in bateau.positions:
                self.matrice[self.calcul_position(x, y)] = "⛵"
        else:
            print("Le bateau ne peut pas être positionné à cet endroit,il dépasse")
