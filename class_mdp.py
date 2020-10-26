import string
import random
import csv
import tldextract
import tkinter


class Mot_de_Passe:
    
    def __init__(self, nom_site):
        self.nom_site = self.cherche_site(nom_site)
        self.mdp = self.id_generator()
        self.save()

    def cherche_site(self, url):
        nom_du_site = tldextract.extract(url)
        return nom_du_site.domain

    def id_generator(self, size=32, lettre=string.ascii_uppercase + string.digits):
        return''.join(random.choice(lettre) for _ in range(size))

    def save(self):  # on les stocke (ici par défaut mais on peut le faire à la demande)
        with open('S:\Documents\GitHub\Projet cyriaque\stockagemdp.csv', 'w', newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([self.nom_site] + [self.mdp])


if __name__ == "__main__":
    print("ya un soucis")
