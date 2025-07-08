import random

L = []
def hauteur(long, h_dep, h_max,h_min):
    for i in range(long):
        #si premier bloc alors ajouter hauteur début choisi 
        if len(L) == 0:
            L.append(h_dep)
        elif len(L) == 1:
            L.append(L[-1])
        elif L[-1] <= h_min +3:
            L.append(random.randint(L[-1],L[-1]+1))
        elif L[-1] >= h_max -3:
            L.append(random.randint(L[-1]-1,L[-1]))
        else:
            n_alea = random.randint(0,99)
            if n_alea < 20:
                L.append(L[-1]-1)
                
            elif n_alea >=20 and n_alea <=80:
                L.append((L[-1]))
            elif n_alea >80:
                if L[-2] < L[-1]:
                    L.append((L[-1]))
                else:
                    L.append((L[-1]+1)) 
    return L




   