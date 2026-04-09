import os
from lecampo import*
from lereg import*

nomearq = open("pessoasGOT.dat","wb")
totalreg = 0

nomearq.write(totalreg.to_bytes(4, byteorder='little'))
totalregform = nomearq.read(4)

opcao = int(input("escolha sua opção: 1(inserir), 2(buscar) ou 3(sair)"))
while (opcao < 3):
    if opcao == 1:
        reg = + leia_campo()
        reg.encode("utf-8").ljust(64, b'\0')
        offset = (totalreg * 64 + 4) 
        nomearq.seek(offset)
        nomearq.write(reg)
        totalreg += 1 

    else:
        if opcao == 2:
            rrn = int(input("digite o rrn desejado"))
            if rrn >= totalreg:
                raise ValueError("o rrn não foi encontrado")
            else:
                offset = (rrn * 64 + 4 )
                nomearq.seek(offset)
                mostrar = nomearq.read(reg)
                print (mostrar)
                alterar = int(input("escolha sua opção: 1, 2 ou 3"))
                if (alterar <3 ):
                    reg = + leia_reg()
                    reg = reg.encode().ljust(64, b'\0')
                    nomearq.seek(offset)
                    nomearq.write(reg)
        escolha = int(input("escolha sua opção: 1, 2 ou 3"))
    nomearq.seek(0)
    nomearq.write(totalreg.to_bytes(4, byteorder='little'))
    nomearq.close()       

    
                    