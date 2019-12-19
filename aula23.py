#Manipulando arquivos
# -*- coding: utf-8 -*-

"""
r = Somente leitura
w = Escrita (caso o arquivo já exista, ele será apagado e um novo arquivo vazio será criado)
a = Leitura e escrita (adiciona o novo conteúdo ao fim do arquivo)
r+ = Leitura e escrita
w+ = Escrita (o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo)
a+ = Leitura e escrita (abre o arquivo para atualização)
"""

"""
LENDO ARQUIVOS

* read() = Lê o arquivo inteiro
* realine() = Lê uma linha
* realines() = Lê arquivo e o armazena em uma lista
"""
arquivo = open("arquivo.txt")

linhas = arquivo.readlines()

print(linhas)

for linha in linhas:
    print(linha)

texto_completo = arquivo.read()

print(texto_completo)

#Criando arquivo

w = open("arquivo2.txt", "a")

w.write("Esse é o meu arquivo\n")
w.close()