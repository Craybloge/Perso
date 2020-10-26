import string
import random


def id_generator(size=32, lettre=string.ascii_letters + string.digits + string.punctuation):
    return''.join(random.choice(lettre) for _ in range(size))


print(id_generator())
