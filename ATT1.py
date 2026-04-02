import os 


nome_arq = input("Digite o nome do arquivo: ")

# abre para escrita (cria ou sobrescreve)
saida =  open(nome_arq, "w")

sobrenome = input("Sobrenome (enter para sair): ")

while sobrenome != "":
    nome = input("Nome: ")
    endereco = input("Endereco: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("CEP: ")

    
    saida.write(sobrenome)
    saida.write("|")
    saida.write(nome)
    saida.write("|")
    saida.write(endereco)
    saida.write("|")
    saida.write(cidade)
    saida.write("|")
    saida.write(estado)
    saida.write("|")
    saida.write(cep)
    saida.write("|\n")  # quebra de linha no final

    sobrenome = input("Sobrenome (enter para sair): ")