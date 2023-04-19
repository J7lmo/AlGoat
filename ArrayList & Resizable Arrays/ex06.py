def fusion_listes(liste1,liste2):
    liste3 = []
    for i in liste1:
        liste3.append(i)
    for j in liste2:
        liste3.append(j)
    liste3 = sorted(liste3)
    return liste3
        
print(fusion_listes([1, 3, 5], [2, 4, 6]))
