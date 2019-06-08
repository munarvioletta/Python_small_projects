# Sortowanie przez Wstawianie - Bubble Sort

import cmath

x = 0
pom = 0
ile = 0
liczba = 0
#tab = [10, 5, 7, 20, 37, 29, 3]
tab = []
ile = int(input('Ile liczb chcesz wpisac do tablicy:'))

for i in range(0, ile):
    print('Wpisz liczby do tablicy:')
    liczba = float(input())
    tab.append(liczba)


n = len(tab)

while x < n:

    for i in range(n - 1):
        if tab[i] > tab[i+1]:

            pom = tab[i]
            tab[i] = tab[i+1]
            tab[i+1] = pom

    x += 1

print("koniec")

print('Tablica: {} '.format(tab))
