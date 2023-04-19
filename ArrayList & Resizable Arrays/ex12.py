def add_list (liste):
    somme = 0
    for i in range(len(liste)):
        somme += liste[i]
    return somme
print(add_list( [1, 2, 3, 4, 5]))