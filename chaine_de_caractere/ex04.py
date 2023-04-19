def chaine_fusion():
    ch1 = input("Entrez une première chaîne de caractères : ")
    ch2 = input("Entrez une deuxième chaîne de caractères : ")
    chres = ""
    for i in ch1:
        chres += i
    for i in ch2:
        chres += i
    return chres

print(chaine_fusion())
