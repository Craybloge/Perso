import string
import random
from class_mdp import Mot_de_Passe as mdp

nom_du_site = "https://www.amazon.com"


def cherche_site():
    "fait des trucs compliqué puis nom_du_site ="
    pass


mdp_amazon = mdp(nom_du_site)
print(mdp_amazon.mdp, mdp_amazon.nom_site)
# def id_generator(size=6, lettre=string.ascii_uppercase + string.digits):
#     return''.join(random.choice(lettre) for _ in range(size))


# id_generator()
# cherche_site()

# save = {nom_du_site: id_generator()}
# print(nom_du_site)
# print(save[nom_du_site])
