import string
import random


class Mot_de_Passe:
    def __init__(self, nom_site):
        self.nom_site = nom_site
        self.mdp = self.id_generator()

    def id_generator(self, size=6, lettre=string.ascii_uppercase + string.digits):
        return''.join(random.choice(lettre) for _ in range(size))


if __name__ == "__main__":
    print("ya un soucis")
