def liste_decroissante (liste):
    rep = []
    nb = len(liste)
    for i in range(nb):
        rep.append(liste[nb-1-i])
    return rep
print(liste_decroissante([1, 2, 3, 4, 5]))