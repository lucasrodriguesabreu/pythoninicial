#Números aleatórios
# -*- coding: utf-8 -*-
import random

#Forçar o python a escolher sempre o mesmo número
#random.seed(1)

numero = random.randint(0, 10)
print(numero)

#O método choice seleciona um número/item de uma lista
lista = [6, 45, 9]
numero = random.choice(lista)
print(numero)