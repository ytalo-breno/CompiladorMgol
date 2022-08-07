import pandas as pd


from AutomatoLexico import *
from TabelaSimbolos import *
from Producoes import *

def main():

    arq = open('./files/teste.mgol', "r")
    action = pd.read_csv('./files/actions.csv',index_col='state')
    goto = pd.read_csv('./files/goto.csv', index_col='state')

    # action.set_index('state')
    # goto.set_index('state')

    arq_lido = arq.read()
    marcador = 0
    token = {'classe': ''}

    s = 0
    pilha = []
    t = 0
    while token.get('classe') != 'EOF':
        #estrutura de chamada do léxico
        token, marcador = scanner(afd, estadosFinais, tabela_simbolos, arq_lido,marcador)
        arq.seek(marcador)
        arq_lido = arq.read()

        #sintatico

        s = t
        a = token['classe']
        if "s" in action.at[s, a]:
            print('ok! shift')
            t = int(''.join(filter(str.isdigit, action.at[s,a])))
            pilha.append(t)

        elif "r" in action.at[s,a]:
            prodnum = int(''.join(filter(str.isdigit, action.at[s,a])))
            part = producoes[prodnum].partition('->')
            cardinalidade = len(part[2].split())
            for _ in range(cardinalidade):
                pilha.pop()

            t = pilha[-1]
            aux = int(goto.loc[t,part[0]])
            pilha.append(aux)


            print('ok, reduce')

            #print(t)




    print(action)
    print(goto)
if __name__ == '__main__':
  main()

 # for key in tabela_simbolos:
      #print(tabela_simbolos[key])