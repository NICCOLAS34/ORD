import os


nomearq = input("qual o nome do arquivo:")
arq = open(nomearq , 'a+')

sobrenome = input("digite seu sobrenome:")
while sobrenome != "":

    nome = input("qual é o seu nome: ")
    idade = input("qual é a sua idade: ")

    arq.write(nome)
    arq.write("|")
    arq.write(sobrenome)
    arq.write("|")
    arq.write(idade)
    arq.write("|")
    arq.seek(0)
    tamanho = arq.read()
    arq.write(str(len((tamanho))))
    arq.write("|")
    arq.write("\n")

    sobrenome = input("digite seu sobrenome ")
arq.close()
            
            


