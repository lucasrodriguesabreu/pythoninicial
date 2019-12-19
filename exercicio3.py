#Faça um programa que resolva uma equação de segundo grau.
# -*- coding: utf-8 -*-
from math import sqrt

a = int (input("Digite o valor de a: "))
b = int (input("Digite o valor de b: "))
c = int (input("Digite o valor de c: "))

delta = b**2 - 4*a*c
raiz_delta = sqrt(delta)

x1 =(-b + raiz_delta)/(2*a)
x2 =(-b - raiz_delta)/(2*a)

print ("X1 = %d" %x1)
print ("X2 = %d" %x2)