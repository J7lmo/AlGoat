def liste_sans_doublons (liste):
    temp = 0
    for i in liste:
        if  temp == i:
            del liste[i]
        else:
            temp = i
    print (liste)
liste_sans_doublons([1, 2, 3, 3, 4, 5])