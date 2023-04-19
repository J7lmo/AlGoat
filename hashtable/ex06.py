dic = {'nom': 'patas','age': 30, 'prenom': 'jean'}
para = input('rentrez la clef:\n')
j = 0
for i in dic:
    if i == para:
        print(dic[para])
        j =+ 1
if j == 0:
 print("Clé inexistante")