def somme_list (liste):
    val = 0
    for i in liste:
        val = val + i
    return val
print(somme_list([1,2,3,4,5]))