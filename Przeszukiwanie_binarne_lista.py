import random
import math

n = int(input("Podaj max:"))

#liczba_los = random.randrange(1, 100, 1)

min = 1
max = n
pyt = 'nic'
srednia = math.floor((min + max)/2)
odp = 'no'

while odp == 'no':

    if pyt == 'm':
        max = srednia-1
        print('Zakres:{0} - {1} '.format(min, max))
    if pyt == 'w':
        min = srednia+1
        print('Zakres:{0} - {1} '.format(min, max))

    srednia =  math.floor((min + max) / 2)

    odp = input('Czy zgadlem: {} (yes/no)? '.format(srednia))
    if odp =='yes':

        print('Odgadl liczbe: {} '.format(srednia))
        break
    if odp =='no':
        pyt = input('Czy liczba wieksza, czy mniejsza od wymyslonej (w,m): ')
        print('liczba jest: {} '.format(pyt))

print(srednia)