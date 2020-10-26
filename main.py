import string
import random
import tldextract
import tkinter
from class_mdp import Mot_de_Passe as mdp
url = input("Donnez l'URL  :")


test = mdp(url)

print(test.nom_site)

fenetre = Tk()
champ_label = Label(fenetre,  text="wsh wsh les amis")
champ_label.pack()
fenetre.mainloop()
