def dic_val(dic):
    liste = []
    temp = 0
    for i in dic:
        val = dic.get(i)
        if val >= temp:
            temp = val 
            name = i
    print (name)
dic_val({'a': 2,'b': 5,'c': 3})