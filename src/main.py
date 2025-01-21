import pandas as pd


from AutomatoLexico import *
from TabelaSimbolos import *
from Producoes import *
from src.semantico import escolhe_regra, pilha_semantica


def main():

    arq = open('./files/teste.mgol', "r")
    action = pd.read_csv('./files/actions_goto.csv',index_col='state')

    arq_lido = arq.read()
    marcador = 0
    token = {'classe': ''}

    topo_pilha = 0
    pilha = list()
    pilha.append(0)
    estado_t = 0

    token, marcador = scanner(afd, estadosFinais, tabela_simbolos, arq_lido, marcador)
    arq.seek(marcador)
    arq_lido = arq.read()
    token_classe = token['classe']

    while token.get('classe'):


        #sintatico

        topo_pilha = pilha[-1]
        try:
            if "S" in action.at[topo_pilha, token_classe]:

                estado_t = int(''.join(filter(str.isdigit, action.at[topo_pilha,token_classe])))
                pilha.append(estado_t)

                pilha_semantica.append(token)
                #estrutura de chamada do lexico
                token, marcador = scanner(afd, estadosFinais, tabela_simbolos, arq_lido, marcador)

                arq.seek(marcador)
                arq_lido = arq.read()
                token_classe = token['classe']




            elif "R" in action.at[topo_pilha,token_classe]:

                prodnum = int(''.join(filter(str.isdigit, action.at[topo_pilha,token_classe])))
                part = producoes[prodnum].partition('->')
                cardinalidade = len(part[2].split())
                for _ in range(cardinalidade):
                    pilha.pop()

                estado_t = pilha[-1]

                #goto
                aux = int(action.loc[estado_t,part[0]])
                pilha.append(aux)
                print(producoes[prodnum])
## Inicio semantico
                escolhe_regra(prodnum)

            elif 'ACC' in action.at[topo_pilha,token_classe]:
                print(producoes[prodnum-1])
                break

        except Exception:
            #correçao frase
            pilha_aux = pilha.copy()
            token_aux = token_classe
            topo_pilha_aux = pilha_aux[-1]
            producao = get_prod(topo_pilha_aux, action)
            action_rec = 'nan'
            action_rec2 = 'nan'
            for i in producao:
                topo_pilha = pilha[-1]
                pilha_aux = pilha.copy()
                action_rec = action.at[topo_pilha,i]
                estado_rec = int(''.join(filter(str.isdigit, action.at[topo_pilha_aux,i])))
                action_rec_original ='nan'
                action_rec_parcial = ''

                while str(action_rec_original) =='nan' and str(action_rec_parcial) !='nan':

                    if 'R' in action_rec:
                        prodnum = int(''.join(filter(str.isdigit, action_rec)))
                        part = producoes[prodnum].partition('->')
                        cardinalidade = len(part[2].split())
                        for _ in range(cardinalidade):
                            pilha_aux.pop()

                        estado_t = pilha_aux[-1]

                        # goto
                        aux = int(action.loc[estado_t, part[0]])
                        action_rec = action.loc[aux,i]
                        pilha_aux.append(aux)
                        topo_pilha = pilha_aux[-1]
                        action_rec_original = action.loc[topo_pilha,token_classe]

                    elif 'S' in action_rec:
                        action_rec_original = action_rec
                        pilha_aux.append(int(''.join(filter(str.isdigit, action_rec))))

                    action_rec_parcial = action.loc[topo_pilha,i]
                action_rec2 = action.at[pilha_aux[-1], token_aux]
                if str(action_rec2) != 'nan':
                    print('\nErro sintático no token {}, linha {}, col {}'.format(token['lexema'],erro['linha'],erro['colErro']))
                    print('Esperava: {}\n'.format(i))
                    pilha = pilha_aux
                    token_classe = token_aux
                    break
            #panico
            if action_rec == float('nan') or str(action_rec2) == 'nan':
                print('\nErro sintático, token {} não era esperado,linha {}, col {}\n'.format(token['lexema'],erro['linha'],erro['colErro']))

                token, marcador = scanner(afd, estadosFinais, tabela_simbolos, arq_lido, marcador)
                arq.seek(marcador)
                arq_lido = arq.read()
                token_classe = token['classe']
    arq.close()




def get_prod(state, action):
    columns = action.columns.values
    line_state = action.loc[state, 'inicio':'eof']

    prod = list()
    for index, cell in enumerate(line_state):
        if str(cell) != 'nan':
            prod.append(columns[index])
    return prod




if __name__ == '__main__':
  main()

 # for key in tabela_simbolos:
      #print(tabela_simbolos[key])
