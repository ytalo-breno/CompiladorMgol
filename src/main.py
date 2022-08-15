import pandas as pd


from AutomatoLexico import *
from TabelaSimbolos import *
from Producoes import *

def main():

    arq = open('./files/teste.mgol', "r")
    action = pd.read_csv('./files/automatoLR(1).csv',index_col='state')
    #goto = pd.read_csv('./files/goto.csv', index_col='state')

    # action.set_index('state')
    # goto.set_index('state')

    arq_lido = arq.read()
    marcador = 0
    token = {'classe': ''}

    s = 0
    pilha = list()
    pilha.append(0)
    t = 0
    # a ='inicio'

    token, marcador = scanner(afd, estadosFinais, tabela_simbolos, arq_lido, marcador)
    arq.seek(marcador)
    arq_lido = arq.read()
    a = token['classe']

    while token.get('classe'):


        #sintatico

        s = pilha[-1]
        try:
            if "S" in action.at[s, a]:

                t = int(''.join(filter(str.isdigit, action.at[s,a])))
                pilha.append(t)
                #print(action.at[s,a])
                #print(token['classe'])

                #estrutura de chamada do lexico
                token, marcador = scanner(afd, estadosFinais, tabela_simbolos, arq_lido, marcador)
                arq.seek(marcador)
                arq_lido = arq.read()
                a = token['classe']



            elif "R" in action.at[s,a]:

                prodnum = int(''.join(filter(str.isdigit, action.at[s,a])))
                part = producoes[prodnum].partition('->')
                cardinalidade = len(part[2].split())
                for _ in range(cardinalidade):
                    pilha.pop()

                t = pilha[-1]
                #goto
                aux = int(action.loc[t,part[0]])
                pilha.append(aux)
                print(producoes[prodnum])

            elif 'ACC' in action.at[s,a]:
                print(producoes[prodnum-1])
                break

        except Exception:
            #correçao frase
            pilha_aux = pilha.copy()
            token_aux = a
            s1 = pilha_aux[-1]
            producao = get_prod(s1, action)
            action_rec = 'nan'
            action_rec2 = 'nan'
            for i in producao:
                s = pilha[-1]
                pilha_aux = pilha.copy()
                action_rec = action.at[s,i]
                estado_rec = int(''.join(filter(str.isdigit, action.at[s1,i])))
                action_rec_original ='nan'
                action_rec_parcial = ''
                if i =='fc_p':
                    pass
                while str(action_rec_original) =='nan' and str(action_rec_parcial) !='nan':

                    if 'R' in action_rec:
                        prodnum = int(''.join(filter(str.isdigit, action_rec)))
                        part = producoes[prodnum].partition('->')
                        cardinalidade = len(part[2].split())
                        for _ in range(cardinalidade):
                            pilha_aux.pop()

                        t = pilha_aux[-1]
                        # goto
                        aux = int(action.loc[t, part[0]])
                        action_rec = action.loc[aux,i]
                        pilha_aux.append(aux)
                        s = pilha_aux[-1]
                        action_rec_original = action.loc[s,a]

                    elif 'S' in action_rec:
                        if action_rec == 'S70':
                            pass
                        action_rec_original = action_rec
                        pilha_aux.append(int(''.join(filter(str.isdigit, action_rec))))


                    action_rec_parcial = action.loc[s,i]
                action_rec2 = action.at[pilha_aux[-1], token_aux]
                if str(action_rec2) != 'nan':
                    print('Erro sintático no token {}, linha {}, col {}'.format(token['lexema'],erro['linha'],erro['colErro']))
                    print('Esperava: {}'.format(i))
                    pilha = pilha_aux
                    a = token_aux
                    break

            if action_rec == float('nan') or str(action_rec2) == 'nan':
                print('erro')

                token, marcador = scanner(afd, estadosFinais, tabela_simbolos, arq_lido, marcador)
                arq.seek(marcador)
                arq_lido = arq.read()
                a = token['classe']




def get_prod(state, action):
    columns = action.columns.values
    line_state = action.loc[state, 'inicio':'eof']

    prod = list()
    for index, cell in enumerate(line_state):
        if str(cell) != 'nan':
            prod.append(columns[index])
    return prod




    print(action)

if __name__ == '__main__':
  main()

 # for key in tabela_simbolos:
      #print(tabela_simbolos[key])