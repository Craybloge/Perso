import string
import random
import tldextract
import tkinter
import csv
from class_mdp import Mot_de_Passe as mdp


def update_nom(*args):
    nom.set(Entry_nom.get())


# ici on ajoute un mdp et on laisse une option temporaire pour skip l'ajout de mdp
url = input("Donnez l'URL  :")
if url != "a":
    test = mdp(url)
    print(test.nom_site)


# ici on initialise les listes
listemdp = []

# la on lit le fichier csv
with open('stockagemdp.csv', newline="") as csvfile:
    liste = csv.reader(csvfile, delimiter=' ', quotechar='|')

    # ici on ajoute les mdp à une liste et on sépare le mdp et le nom du site pour les repérer
    for row in liste:
        listemdp.append(', '.join(row).split(","))


# on demande à l'utilisateur de quel site il veut le mdp et on lui affiche
choix = input('choisissez le site dont vous voulez le mdp:')
for i in listemdp:
    if choix == i[0]:
        print("voici le mdp:", i[1])

# création de la fenetre
fenetre = tkinter.Tk()
fenetre.title("Projet Dash Lane")

# dimension et placement de la fenetre
screen_x = fenetre.winfo_screenwidth()
screen_y = fenetre.winfo_screenheight()
window_x = 400
window_Y = 100
posX = (screen_x) - (window_x) - 50
posY = (screen_y) - (window_Y) - 100
geo = "{}x{}+{}+{}".format(window_x, window_Y, posX, posY)
fenetre.geometry(geo)

nom = tkinter.StringVar()

# création de l'interieur de la fentre
nom.trace("w", update_nom)
Entry_nom = tkinter.Entry(fenetre, bd=3, textvariable=nom)
Entry_nom.pack()


fenetre.mainloop()

print(nom)
print(nom)
print(nom)
