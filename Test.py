import string
import random


def cherche_site():
    "fait des trucs compliqué puis nom_du_site ="
    return ''


nom_du_site = cherche_site()


def id_generator(size=6, lettre=string.ascii_uppercase + string.digits):
    return''.join(random.choice(lettre) for _ in range(size))


id_generator()
cherche_site()

save = {nom_du_site: id_generator()}
print(nom_du_site)
print(save[nom_du_site])
