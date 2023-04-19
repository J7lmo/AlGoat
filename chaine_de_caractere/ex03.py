def split_chaine ():
    ch1 = "Hello World"
    ch2 = ""
    ch3 = ""
    nbch1 = len(ch1)
    for i in range(nbch1):
        if i <= nbch1 / 2:
            ch2 += ch1[i]
        if i > nbch1 / 2:
            ch3 += ch1[i]
    print(ch2)
    print(ch3)
split_chaine()    