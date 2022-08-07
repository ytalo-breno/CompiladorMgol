import pandas as pd


from AutomatoLexico import *
from TabelaSimbolos import *


def main():

    arq = open('./files/teste.mgol', "r")
    action = pd.read_csv('./files/actions.csv',index_col=0)
    goto = pd.read_csv('./files/goto.csv',index_col=0)

    arq_lido = arq.read()
    marcador = 0
    token = {'classe': ''}

    s = 0
    pilha = []

    while token.get('classe') != 'EOF':
        #estrutura de chamada do léxico
        token, marcador = scanner(afd, estadosFinais, tabela_simbolos, arq_lido,marcador)
        arq.seek(marcador)
        arq_lido = arq.read()

        #sintatico
        #if (action[])


    print(action)
    print(goto)
if __name__ == '__main__':
  main()

 # for key in tabela_simbolos:
      #print(tabela_simbolos[key])