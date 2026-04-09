'''
leiareg:
Esse programa lê os dados gravados no arquivo criado pelo programa
escreve_registros. Os registros devem ser lidos do arquivo um a um e apresentados em tela.
'''


import os

entrada = open("lereg.txt","rb")

def leiareg(entrada):
    tam = entrada.read(2)
    tamint = int.from_bytes(tam, byteorder='big')

    if tamint > 0:
        buffer = entrada.read(tamint)
        bufferstr = buffer.decode('utf-8')
        return bufferstr
    
    else:
        return ""


buffer = leiareg(entrada)
while buffer != "":
    lista = list(buffer)
    for campo in lista:
        print(campo)
    buffer = leiareg()
entrada.close()