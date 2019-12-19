
lista = [500,963,472,9,70,3,2,1]
#Aqui ordena automaticamente com uma função do Python
"""
lista = sorted(lista)
print (lista)
"""
for i in range(len(lista)):
    menor = i
    for j in range (i+1,len(lista)):
        if lista[j] < lista[menor]:
            menor = j
    
    if lista[i] != lista[menor]:
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux
print (lista)