def dic_moy (dic):
    j = 0
    y = 0
    val = dic.values()
    print (val)
    for i in val:
        y =  y + i
        j = j + 1
    moy = y / j
    print (moy, dic)
dic_moy({'a': 4,'b':2, 'c':3})