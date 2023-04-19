def add_dic (dic):
    somme = 0
    for i in dic:
        somme += dic[i]
    return somme
print(add_dic({"a": 1, "b": 2, "c": 3}))