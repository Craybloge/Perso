import string
import random
import tldextract
from class_mdp import Mot_de_Passe as mdp
import tldextract
url = input("Donnez l'URL  :")




test = mdp(url)

print(test.nom_site)


# def id_generator(size=6, lettre=string.ascii_uppercase + string.digits):
#     return''.join(random.choice(lettre) for _ in range(size))


# id_generator()
# cherche_site()

# save = {nom_du_site: id_generator()}
# print(nom_du_site)
# print(save[nom_du_site])
