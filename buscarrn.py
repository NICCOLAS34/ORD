'''
buscarrn:
- busca_sobrenome também faz uma busca sequencial no
arquivo pessoasGOT.dat, porém utiliza o campo Sobrenome
como chave
– Sobrenome é uma chave secundária, então a lógica da busca deve ser
outra: todos os registros devem ser lidos sempre, para garantir que
todas as ocorrências da chave buscada foram localizadas

'''

entrada = open("pessoasGOTfixo.dat","rb")

cab = entrada.read(4)
totalreg = int.from_bytes(cab, byteorder="little")

rrn = int(input("digiteo rrn a ser recuperado:"))

if rrn >= totalreg:
    raise ValueError("erro")

offset = rrn * 64 + 4 
entrada.seek(offset)
reg = entrada.read(64)
reg = reg.decode()
reg.split(sep= "|")

for campo in reg.split(sep ="|"):
    print(campo)

entrada.close()


