from colorama import Fore, Style


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
            return ("Tir en dehors de la grille !")

        index = self.calcul_position(x, y)

        if self.matrice[index] == "⛵":
            self.matrice[index] = touche
            return "Touché !"
        elif self.matrice[index] == "~":
            self.matrice[index] = "o"
            return "Raté !"
        elif self.matrice[index] in ("x", "o"):
            return "Cette case a déjà été tirée."
        else:
            return ("Erreur inconnue.")

    def afficher(self, debug=False):
        # Fonction interne pour colorer les cases
        def colorer_case(case):
            if case == "x":
                return Fore.RED + "x" + Style.RESET_ALL
            if case == "o":
                return Fore.BLUE + "o" + Style.RESET_ALL
            if case == "⛵":
                # on affiche le bateau seulement si debug=True
                return Fore.YELLOW + "⛵" + Style.RESET_ALL if debug else "~"
            return case

    # Ligne d'en-tête avec les numéros de colonnes
        header = "   " + " ".join(str(i + 1) for i in range(self.nombre_colonnes))
        print(header)

    # Corps de la grille
        for i in range(self.nombre_lignes):
            lettre = chr(ord("A") + i)
            ligne = self.matrice[i * self.nombre_colonnes: (i + 1) * self.nombre_colonnes]
            ligne_coloree = " ".join(colorer_case(c) for c in ligne)
            print(f"{lettre}  {ligne_coloree}")

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

    def tous_bateaux_coules(self):
        """
        Retourne True si toutes les cases avec un bateau ont été touchées.
        """
        return "⛵" not in self.matrice