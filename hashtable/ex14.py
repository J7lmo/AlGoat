def dic_none(dic):
    for i in dic.copy():
        temp = dic[i]
        if temp == None:
            del dic[i]
    print(dic)
dic_none({'a': 1, 'b': None, 'c': 3, 'd': None})