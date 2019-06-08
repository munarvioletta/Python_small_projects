import cmath

tab = [5, 2, 15, 6, 3, 4, 1, 30, 20, 50, 32]

n = len(tab)
index = 0
zach_wart_przed_przesk = 0

def selectsort(tab):

    for i in range(0, n):

        k = i
        for j in range(i+1, n):

            if tab[k] < tab[j]:

                if j == (n - 1) and k != i:

                    pom2 = tab[i]
                    tab[i] = zach_wart_przed_przesk
                    tab[index] = pom2

            elif tab[k] > tab[j]:

                if j == (n - 1):
                    zach_wart_przed_przesk = tab[j]
                    index = j
                    k = j

                    if j == (n - 1) and k != i:
                        pom2 = tab[i]
                        tab[i] = zach_wart_przed_przesk
                        tab[index] = pom2

                else:
                    zach_wart_przed_przesk = tab[j]
                    index = j
                    k = j
                    j += 1

print('Tablica: {}'.format(tab))
selectsort(tab)
print('Tablica posortowana: {}'.format(tab))