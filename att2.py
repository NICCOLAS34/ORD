import os

nomearq = input("digite o nomre do arquivo:")
arq = open(nomearq, 'r')
ler = arq.read()

def concatena(ler: str):
    campo = ""
    i = 0

    while i < len(ler):
        while i < len(ler) and ler[i] != "|":
            campo += ler[i]
            i += 1

        print(campo)
        campo = ""
        i += 1



concatena(ler)