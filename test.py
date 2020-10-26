import string
import random

#mon test est terminé tu peux supprimer et faire un autre test si tu veux
def id_generator(size=32, lettre=string.ascii_letters + string.digits + string.punctuation):
    return''.join(random.choice(lettre) for _ in range(size))


print(id_generator())
