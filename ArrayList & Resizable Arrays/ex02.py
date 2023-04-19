def chaine_la_plus_longue (liste):
    temp = 0
    for i in liste: 
        nb = len(i)
        if nb > temp:
            temp = nb
            res = i
    return res
print(chaine_la_plus_longue(["un", "deux", "trois"]))
