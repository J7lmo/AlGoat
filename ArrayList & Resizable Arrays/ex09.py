def k_plus_grands (liste,k):
    res_liste = []
    j = 0
    liste_sorted = sorted(liste)
    nb = len(liste_sorted)
    for i in range(nb):
        j = j + 1
        if j == k+1:
            break
        res_liste.append(liste_sorted[nb-1-i])
    return res_liste
print(k_plus_grands([1, 7, 3, 5, 9, 2], 3))