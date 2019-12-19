#Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade
# -*- coding: utf-8 -*-

idade = int (input("Digite sua idade: "))
if idade >= 18:
    print ("Você é maior de idade!")

elif idade > 0 and idade < 18:
    print ("Você é menor de idade")

else:
    print ("Digite uma idade válida!")