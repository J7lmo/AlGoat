def invert_srot (liste):
    rep = []
    nb = len(liste)
    for i in range(nb):
        rep.append(liste[nb-1-i])
    return rep
print(invert_srot([1, 2, 3, 4, 5]))