def dic_sorted(dic):
    rep = []
    for i in dic:
        rep.append(i)
    rep = sorted(rep)
    return rep
print(dic_sorted({"banane": 3, "pomme": 2, "orange": 1}))