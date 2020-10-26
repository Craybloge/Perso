import string
import random
import tldextract
import tkinter as tk
import csv
from class_mdp import Mot_de_Passe as mdp


url = input("Donnez l'URL  :")                                   #ici on ajoute un mdp 
test = mdp(url)
print(test.nom_site)

liste2 = []
listemdp = []                                                   #ici on initialise les listes

with open('stockagemdp.csv', newline="") as csvfile:
    liste = csv.reader(csvfile, delimiter=' ', quotechar='|')   #la on lit le fichier csv
    for row in liste:
        liste2.append(', '.join(row))                           # ici on ajoute les mdp à une liste


    for i in liste2:                                            # ici on sépare les mdp des sites pour pouvoir les repérer
        i = i.split(',')
        listemdp.append(i)
print(listemdp)                                             



choix = input('choisissez le site dont vous voulez le mdp:')    # on demande à l'utilisateur de quel site il veut le mdp et on lui affiche
for i in listemdp:
    if choix == i[0]:
        print("voici le mdp:", i[1])


fenetre = tk.Tk()
champ_label = tk.Label(fenetre,  text="wsh wsh les amis")
champ_label.pack()
fenetre.mainloop()
