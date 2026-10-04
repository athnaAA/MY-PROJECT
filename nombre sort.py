nombre = [4,8,6,2,7,1,3,5,10,9]
longueur = len(nombre)
for i in range (longueur-1):
    ok = True
    for j in range (longueur-1-i):
        if nombre[j]>nombre[j+1]:
            nombre[j], nombre[j+1] = nombre[j+1],nombre[j] #on echange la place des 2 valeurs
            ok = False
    if ok :
        break
print(nombre)