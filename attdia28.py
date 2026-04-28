from sys import argv

arq = open('dados.dat', "rb")

def leiaregistros(arq) -> list[tuple[int, bytes]]:
    
    registros = []
    arq.seek(4)
    tam = arq.read(2)

    while tam:

        id = arq.read(2)
        tamint = int.from_bytes(tam, byteorder='little')
        idint = int.from_bytes(id, byteorder='little')

        buffer = arq.read(tamint)
        bufferstr = buffer.decode()
        bufferformatado = bufferstr.split('|')

        registros.append((idint, bufferformatado))

        
        tam = arq.read(2)

    return registros

def escreveregsord (arq: str, registros: list[tuple[int,bytes]]) -> None:
        




def ordenearqporid (arq: str, arqsaida:str)-> None:








def main() -> None:
    if len(argv) < 3:
        raise TypeError('Numero incorreto de argumentos \n')
    
    ordenearqporid(argv[1], argv[2])

if __name__ == '__name__':
    main()