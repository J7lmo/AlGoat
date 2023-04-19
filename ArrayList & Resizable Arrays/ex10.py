def pairs_liste_triee (liste):
    pair_liste = []
    res = []
    for i in liste:
        nb = i % 2
        if nb == 0:
            pair_liste.append(i)
    res = sorted(pair_liste)
    return res

print(pairs_liste_triee([1, 2, 3, 4, 5, 6])) 