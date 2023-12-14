# Créé par clement.mathieu, le 14/12/2023 en Python 3.7

from random import*
from constante import*


def tirer_nb_mystère():
    nb_mystère=[]
    for i in range(4):
        ajouter=randrange(1,9)
        nb_mystère.append(ajouter)
    print(nb_mystère)
    return(nb_mystère)


tirer_nb_mystère()