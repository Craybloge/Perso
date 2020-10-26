import string
import random
import tldextract
from class_mdp import Mot_de_Passe as mdp
url = "https://stackoverflow.com/questions/44021846/extract-domain-name-from-url-python"




test = mdp(url)

print(test.nom_site)


# def id_generator(size=6, lettre=string.ascii_uppercase + string.digits):
#     return''.join(random.choice(lettre) for _ in range(size))


# id_generator()
# cherche_site()

# save = {nom_du_site: id_generator()}
# print(nom_du_site)
# print(save[nom_du_site])
