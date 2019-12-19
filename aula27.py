#Dicionários
# -*- coding: utf-8 -*-
#Dicionário é declarado entre {} e não []

meu_dicionário = {"A":"AMEIXA", "B":"BOLA", "C":"CACHORRO"}

#Abre o dicionário inteiro
print(meu_dicionário)

#Abre somente determinada chave, nesse caso é a chave A
print(meu_dicionário["A"])

#Navegando no dicionário

#Imprimindo somente as chaves
for chave in meu_dicionário:
    print(chave)

#Imprimindo todos os valores
for chave in meu_dicionário:
    print (meu_dicionário[chave])

#Imprimindo a chave e os valores
for chave in meu_dicionário:
    print(chave+": "+meu_dicionário[chave])

#Convertendo as listas em tuplas (são objetos imutáveis)
for i in meu_dicionário.items():
    print(i)