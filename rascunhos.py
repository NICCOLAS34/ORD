import os


campos = ["idade :", "cidade :"]

arq = open("teste.txt", "+a")
n = str(input("nome: <ou pressione enter para sair do loop>:"))


while n != "":
    arq.write(n + "|")
    for i in campos:
        camposs = input(i)
        arq.write(camposs +"|")

    arq.write("\n")
    n = str(input("nome: <ou pressione enter para sair do loop>:"))

arq.close()


