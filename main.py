import string
import random
import tldextract
import tkinter
from class_mdp import Mot_de_Passe as mdp
url = input("Donnez l'URL  :")


test = mdp(url)

print(test.nom_site)

fenetre = tkinter.Tk()
fenetre.title("Projet Dash Lane")

screen_x = fenetre.winfo_screenwidth()
screen_y = fenetre.winfo_screenheight()

window_x = 400
window_Y = 100


posX = (screen_x) - (window_x) - 50
posY = (screen_y) - (window_Y) - 100


geo = "{}x{}+{}+{}".format(window_x, window_Y, posX, posY)

fenetre.geometry(geo)


fenetre.mainloop()
