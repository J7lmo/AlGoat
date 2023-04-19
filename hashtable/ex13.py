def sort_value (dic):
    dic1 = {}
    sorted_dic = sorted(dic, key=dic.get)
    for i in sorted_dic:
        dic1[i] = dic[i]
    print(dic1)
sort_value({'a': 2,'c':4,'b':1})