def dic_count (dic):
    for i in dic:
        temp = dic[i]
        nb = len(temp)
        dic[i] = nb
    print (dic)
dic_count ({'fruit': 'pomme', 'couleur': 'rouge', 'prix': 'dixeuro'})