import string
import random
import tldextract
import tkinter as tk
from class_mdp import Mot_de_Passe as mdp
url = input("Donnez l'URL  :")



test = mdp(url)

print(test.nom_site)

fenetre = tk.Tk()
champ_label = tk.Label(fenetre,  text="wsh wsh les amis")
champ_label.pack()
fenetre.mainloop()
