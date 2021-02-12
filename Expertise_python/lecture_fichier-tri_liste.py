import random
import statistics


def ecriture():
    rngliste= []
    for number in range (10):
        rngliste.append(str(random.randint(0,100)))
    with open("Expertise_python/liste.txt", "w") as fichier:
        for number in rngliste:
            fichier.write("{}\n".format(number))


def lecture():
    liste_lecture = []
    with open("Expertise_python/liste.txt", 'r') as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            liste_lecture.append(int(ligne))

    print(liste_lecture)
    return liste_lecture

def minimum(liste):
    return min(liste)

def maximum(liste):
    return max(liste)

def tri(liste):
    liste.sort()
    return liste

def moyenne(liste):
    somme=0
    for nombre in liste:
        somme+=nombre
    return somme/len(liste)

def ecart_type(liste):
    return statistics.pstdev(liste)


ecriture()
liste = lecture()
print(maximum(liste))
print(minimum(liste))
print(moyenne(liste))
print(ecart_type(liste))

liste = tri(liste)
print(liste)
