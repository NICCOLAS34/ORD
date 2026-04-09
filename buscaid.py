'''

buscaid:
Inicialmente, o programa deve solicitar o identificador a ser buscado
- Se o registro correspondente for encontrado, o mesmo deve ser
apresentado em tela, finalizando a execução.
- Caso contrário, o programa deve imprimir uma mensagem de registro não
encontrado e terminar.

'''

import os 
from leregprof import*

entrada = open("pessoasGOT.dat","rb")
chave = input("digite o que deseja procurar:")
achou = False

reg = leia_reg(entrada)

while reg != "" and achou == False:
    id = reg.split(sep = "|")[0]
    if id == chave:
        achou = True 

    else:
        reg = leia_reg(entrada)

if achou == True:
    for campo in reg.split(sep="|"):
        print(campo)

else:
    raise ValueError("a chave não foi encontrada dentro do arquivo !") 
entrada.close()