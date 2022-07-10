import string

from AutomatoLexico import *
from TabelaSimbolos import *


def main():

    arq = open('./files/teste.mgol', "r")
    arq_lido = arq.read()
    marcador = 0
    token = {'classe': ''}
    while token.get('classe') != 'EOF':
        token, marcador = scanner(afd, estadosFinais, tabela_simbolos, arq_lido,marcador)
        arq.seek(marcador)
        arq_lido = arq.read()
        print(token)

if __name__ == '__main__':
  main()
