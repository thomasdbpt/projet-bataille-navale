# chevauchement

from bateau import Bateau


b1 = Bateau(1, 1, 3)
b2 = Bateau(0, 2, 2, True)

for e in b1.positions:
    if e in b2.positions:
        print("Chevauchement")
