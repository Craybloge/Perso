import string
import random
import csv
import tldextract
import tkinter


class Mot_de_Passe:

    # on définit les variables à la création de l'objet
    def __init__(self, nom_site):
        self.nom_site = self.cherche_site(nom_site)
        self.mdp = self.id_generator()
        self.save()

    # on utilise l'url entrée pour trouver le nom du site
    def cherche_site(self, url):
        nom_du_site = tldextract.extract(url)
        return nom_du_site.domain

    # on génère un mdp
    def id_generator(self, size=32, lettre=string.ascii_letters + string.digits + string.punctuation):
        return''.join(random.choice(lettre) for _ in range(size))
    # on stocke le mdp et le site sur un fichier csv

    def save(self):
        with open('stockagemdp.csv', 'a', newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([self.nom_site] + [self.mdp])


# si jamais le fichier est éxécuté directement on affiche juste ça pour prévenir l'utilisateur
if __name__ == "__main__":
    print("ya un soucis")
