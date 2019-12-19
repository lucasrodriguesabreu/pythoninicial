#String parte 2
# -*- coding: utf-8 -*-

a = "Lucas"
b = "Rodrigues"

concatenar = a + " " + b + "\n"

print(concatenar.lower())
print(concatenar.upper())
#Remove o espaço no final da string
print(concatenar.strip())

minha_string = "O rato roeu a roupa do rei de Roma"
#Retira todos os "r" da string
#minha_lista = minha_string.split("r")
minha_lista = minha_string
print(minha_lista)
#Chamamos de case sensitive

busca = minha_string.find("rei")
print(busca)

minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)