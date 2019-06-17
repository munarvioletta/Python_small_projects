import math

def average(lista):

    return sum(lista) / len(lista)


def median(lista):

    lista.sort()
    half = len(lista) / 2
    if len(lista) % 2 == 0:

          med = (half + (half+1))/2
    else:

          med = half + 0.5

    return med


def variation(lista, average):

    sigma = 0.0
    for g in lista:

        sigma += (g - average)**2

    var = sigma/len(lista)

    return var


def deviation(lista, variation):

    return math.sqrt(variation) # variation from grades