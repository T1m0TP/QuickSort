import numpy as np
import time

print('''
                 ((((( ☻ )))))
     ______   ____|_|_____
    | ♥    \ /|_||_||_||_|\  Instagram: @codeur.tim
    |_______|_|_||_||_||_|_| Github: T1m0TP
            /___\    /___\

''')

# On définit une variable
toSort = np.random.randint(0, 2000, 1000)
print(toSort)

# On relève l'heure
t1 = time.time()

# On crée la fonction de tri rapide


def quick_sort(toSort):
    # Si la variable est vide
    if len(toSort) == 0:
        return toSort
    # On définit le premier élément qui sera le pivot
    pivot = toSort[0]
    # On définit tous les éléments plus petits que le pivot
    minor = []
    # On définit tous les élements plus grands que le pivot
    major = []

    for i in range(1, len(toSort)):
        # Si l'élément est plus petit que le pivot
        if toSort[i] < pivot:
            # On le rajoute aux éléments
            minor.append(toSort[i])
        # S'il est égal
        if toSort[i] == pivot:
            # On le rajoute soit aux nombres plus petits soit aux plus grands
            minor.append(toSort[i])
        # S'il est supérieur
        if toSort[i] > pivot:
            major.append(toSort[i])

    return quick_sort(minor) + [pivot] + quick_sort(major)


print(quick_sort(toSort))

t2 = time.time()
t3 = t2-t1
print("Le temps est de : ", t3)

t4 = time.time()

toSort = np.random.randint(0, 2000, 1000)
# On crée 2 boucles
for i in range(len(toSort)):
    for j in range(len(toSort)):
        # On crée une condition qui donne l'ordre de rangement des nombres
        if toSort[i] <= toSort[j]:
            # On classe les nombres
            toSort[i], toSort[j] = toSort[j], toSort[i]
print(toSort)


t5 = time.time()
t6 = t5-t4
print("Le temps est de : ", t6)

print("le décalage est de : ", t6-t3)
