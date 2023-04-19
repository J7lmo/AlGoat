def popu ():
    gen = 0
    populations = {'Paris': 2187526, 'Marseille': 863310, 'Lyon': 515695, 'Toulouse': 479553}
    for i in populations:
     if populations[i] > gen:
         gen = populations[i]
    print(f"la population max est {gen}")  
popu ()