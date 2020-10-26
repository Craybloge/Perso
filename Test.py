import string
import random
from class_mdp import Mot_de_Passe as mdp
import tldextract
url = "https://stackoverflow.com/questions/44021846/extract-domain-name-from-url-python"


def cherche_site(url):
    nom_du_site = tldextract.extract(url)
    return nom_du_site


print(cherche_site(url))


# def id_generator(size=6, lettre=string.ascii_uppercase + string.digits):
#     return''.join(random.choice(lettre) for _ in range(size))


# id_generator()
# cherche_site()

# save = {nom_du_site: id_generator()}
# print(nom_du_site)
# print(save[nom_du_site])
