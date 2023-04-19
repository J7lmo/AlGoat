def n_present (liste,n):
    for i in liste:
        if i == n:
            return True
    return False
print(n_present([1, 2, 3, 4, 5], 3))