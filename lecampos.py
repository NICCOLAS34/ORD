'''
le campos: 
- Esse programa lê os dados gravados no arquivo texto criado
pelo programa escreve_campos
- Os campos devem ser lidos do arquivo um a um e
apresentados em tela, conforme mostrado na figura'''



entrada = open("tet.txt","r")

def leiacampo(entrada):
    campo = ""
    c = entrada.read(1)

    while c != "" and c != "|":
        campo += c 
        c = entrada.read(1)

    return(campo) 

campo = leiacampo(entrada)
while campo != "":
    print(campo)
    campo = leiacampo(entrada)

entrada.close
