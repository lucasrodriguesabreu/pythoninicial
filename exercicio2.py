#Faça um programa que receba duas notas digitas pelo usuário. 
#Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.
# -*- coding: utf-8 -*-
nota1 = float (input("Digite a primeira nota: "))
nota2 = float (input("Digite a segunda nota: "))

media = (nota1+nota2)/2

print ("Sua média é: " + (media))

if media >= 6:
    print ("Aprovado")
else:
    print ("Reprovado")