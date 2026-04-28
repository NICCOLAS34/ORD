nomearq = input("digite o nome do arquivo: ")
entrada = open(nomearq, "rb")
saida = open("menosb.txt", "wb")

tam_bytes = entrada.read(2)

while tam_bytes != b"":

    ponteiro = entrada.tell() - 2

    tam = int.from_bytes(tam_bytes, "little")

    id = b""
    c = entrada.read(1)

    while c != b"|":
        id += c
        c = entrada.read(1)

    ponteiro_texto = str(ponteiro).encode()

    saida.write(id)
    saida.write(b"|")
    saida.write(ponteiro_texto)
    saida.write(b"\n")

    entrada.seek(ponteiro + 2 + tam)

    tam_bytes = entrada.read(2)

entrada.close()
saida.close()



    


    