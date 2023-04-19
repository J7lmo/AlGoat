def dic ():
    i = 1
    mon_dic = {}
    while i <= 3:
        nom = input(f"rentrer le {i} nom")
        prenom = input(f"rentrer le {i} prenom")
        age = input(f"rentrer le {i} age")
        temp_dic = {nom: {'prenom': prenom, 'age': age}}
        mon_dic.update(temp_dic)
        i += 1
    print (mon_dic)
dic ()