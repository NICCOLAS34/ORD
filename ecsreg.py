import os 

saida = open("tet.txt","wb")
campo = input("digite o seu sobrenome:")

while campo != "":
    buffer = ""
    buffer += campo + "|"

    for i in range(2):
            campo = input("digite o proximo campo:")

            if campo != "":
                buffer += campo + "|"

            
    convbyytes = buffer.encode()
    tam = len(convbyytes)
    tamby = tam.to_bytes(2, byteorder='big')
    saida.write(tamby)
    saida.write(convbyytes)
    campo = input("digite seu sobrenome:")

saida.close()


'''

V2: 

mensagens = ["nome", "cidade"]

    for m in mensagens:
        valor = input(f"digite {m}: ")

        if valor != "":
            buffer += valor + "|"    
            
'''