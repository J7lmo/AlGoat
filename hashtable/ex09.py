def dic_liste (dic):
    liste =[]
    for i in dic:
        val = dic.get(i, "error")
        liste.append(val)
    print (liste)
dic_liste({'nom': 'patas', 'age': 30, 'prenom': 'jean'})