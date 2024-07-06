#Bismillah !

import numpy as np
import matplotlib.pyplot as plt



#Rappels : 
#On définit un ensemble de julia de la façon suivante : 
#On fixe un nombre complexe c et on associe la suite (zn), n>= 0 définie par :
# zn+1 = zn**2 + c
#En balayant toutes les valeurs de zo, on cherche à dessiner tous les zo pour lesquels la suite est bornée. Le critère sera le non dépassement de 2 en terme de module.

# Fonction julia, qui prend en argument de complexes, z et c et renvoie un booléen. Elle vérifie entre autre si un certain complexe z appartient à l'ensemble de Julia.
def julia(z:complex,c:complex)->bool:
    z = z**2 + c
    if abs(z) < 2:
        pass
    else:
        return False
    for i in range(1,100):
        z = z**2 + c
        if abs(z) < 2:
            pass
        else:
            return False
    return True
#Fonction qui représente à l'écran les complexes qui sont dans l'ensemble de Julia. En noir ceux qui y sont, en blanc ceux qui n'y sont pas.
def trace_julia(c:complex, I1:tuple, I2:tuple, pix):
    image = np.zeros((pix,pix,3), dtype=np.uint8)
    inter_1 = np.linspace(I1[0], I1[1], pix)
    inter_2 = np.linspace(I2[0], I2[1], pix)
    noir = [0,0,0]
    blanc = [255,255,255]
    liste_c = []
    for i in range(len(inter_1)):
        for y in range(len(inter_2)):
            complexe = inter_1[i] + inter_2[y]*1j
            liste_c.append(complexe)
            if julia(complexe, c):
                image[i,y] = noir
            else:
                image[i,y] = blanc
    return image

#plt.imshow(trace_julia(-0.85 + 0.2j, (-1.25, 1.25),(-1.25, 1.25),400))
#plt.show()
#nouvelle fonction julia qui à ceci pret renvoie le nombre d'itérations qu'il faut avant que le module du complexe dépasse 2, en + de si le complexe est dans l'ensemble de julia.
def new_julia(z,c)->(bool, int):
    z = z**2 + c
    if abs(z) < 2:
        pass
    else:
        return False,0
    for i in range(1,100):
        z = z**2 + c 
        if abs(z) < 2:
            pass
        else:
            return False, i
    return True, 100
#print(new_julia(1 + 1j, -0.85 + 0.2j))
def trace_julia_couleur(c:complex, I1:tuple, I2:tuple, pix:int):
    image = np.zeros((pix,pix,3), dtype=np.uint8)
    inter_1 = np.linspace(I1[0], I1[1], pix)
    inter_2 = np.linspace(I2[0], I2[1], pix)
    for i in range(len(inter_1)):
        for y in range(len(inter_2)):
            complexe = inter_1[i] + inter_2[y]*1j
            image[i,y] = [10*new_julia(complexe,c)[1] + 2, 15*new_julia(complexe,c)[1] - 10, 255-20*new_julia(complexe,c)[1]]
    return image
#quelques exemples de tests.
#plt.imshow(trace_julia_couleur(0.25+0.2j, (-2, 0.5),(-1.25, 1.25),500))
#plt.show()


# liste de valeurs de c plutot intéressantes à tester : -0.414-0.612j sur [-1,1], 0.284 - 0.0122j sur [-1.5, 1.5],  0.382 + 0.147j  sur [-1.5, 1.5], et pleins d'autres...