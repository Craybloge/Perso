import string
import random
import tldextract
import tkinter
from class_mdp import Mot_de_Passe as mdp
# url = input("Donnez l'URL  :")
url = ("twitter.com")


test = mdp(url)

print(test.nom_site)

