def triabulle (tab):
    nb = len(tab) -1
    if nb <= 0:
        return tab
    j = 1
    while j != 0:
        j = 0
        for i in range(nb):
            if tab[i] > tab[i+1]:
                temp = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = temp
                j += 1
    return tab
print(triabulle([5, 7, 12,-5, 16]))
