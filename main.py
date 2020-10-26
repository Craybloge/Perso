import string
import random
import tldextract
import tkinter as tk
import csv
from class_mdp import Mot_de_Passe as mdp


# ici on ajoute un mdp
url = input("Donnez l'URL  :")
test = mdp(url)
print(test.nom_site)


# ici on initialise les listes
liste2 = []
listemdp = []


# la on lit le fichier csv
with open('stockagemdp.csv', newline="") as csvfile:
    liste = csv.reader(csvfile, delimiter=' ', quotechar='|')

    # ici on ajoute les mdp à une liste
    for row in liste:
        liste2.append(', '.join(row))

# ici on sépare les mdp des sites pour pouvoir les repérer
    for i in liste2:
        i = i.split(',')
        listemdp.append(i)
print(listemdp)


# on demande à l'utilisateur de quel site il veut le mdp et on lui affiche
choix = input('choisissez le site dont vous voulez le mdp:')
for i in listemdp:
    if choix == i[0]:
        print("voici le mdp:", i[1])


fenetre = tk.Tk()
champ_label = tk.Label(fenetre,  text="wsh wsh les amis")
champ_label.pack()
fenetre.mainloop()
