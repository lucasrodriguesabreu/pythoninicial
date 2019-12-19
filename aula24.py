#Listas e dicionários - Parte 1
# -*- coding: utf-8 -*-
minha_lista = ["Abacaxi","Melancia","Abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["Abacaxi", 2, 9.89, True]

print(minha_lista3)

print(minha_lista[0])

for item in minha_lista:
    print(item)

tamanho = len(minha_lista)
print(tamanho)

#Trabalhando com append - adiciona itens na lista
minha_lista.append("Limão")

print(minha_lista)

if 3 in minha_lista2:
    print("3 está na lista")


#Removendo itens da lista
del minha_lista[2:]
print(minha_lista)

#Criando lista em branco e adicionando itens através do código
minha_lista4 = []

minha_lista4.append(57)
print(minha_lista4)