def pairs_liste (liste):
    res = []
    for i in liste:
        pair = i % 2
        if pair == 0:
            res.append(i)
    return res
print(pairs_liste([1, 2, 3, 4, 5, 6]))