def diviseur (nb):
    i = 0
    tab = []
    while i < nb:
        i += 1
        div = nb % i
        if div == 0:
            tab.append(i)
    print(tab)
diviseur(200)
