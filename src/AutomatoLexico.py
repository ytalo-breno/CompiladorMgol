from typing import Dict, Any, Tuple
from TabelaSimbolos import *
letra = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
numero = tuple("0123456789")
aritm = tuple("+-/*")
espacos = tuple('\n\t ')
erro= {'linha':0,'colAt':0,'colErro':0}

# tabela de transição de estados
afd = {
    0: {espacos: 0,
        tuple('\"' + '\''): 1,
        letra: 2,
        aritm: 4,
        '{': 5,
        '$': 8,  # mudar essa parada depois EOF
        '<': 9,
        '(': 13,
        ')': 14,
        ';': 15,
        ',': 16,
        '>': 17,
        '=': 19,
        numero: 20
        },
    1: {
        (letra + numero + aritm + tuple(' ' + '<' + '(' + ')' + ';' + ',' + '>' + '=' + '.' + ':'+'/'+' ')): 1,
        tuple('\"' + '\''): 3
    },
    2: {
        letra + numero + tuple('_'): 2,
    },
    5: {
        (letra + numero + aritm + tuple(' ' + '<' + '(' + ')' + ';' + ',' + '>' + '=' + '.' + ':' + '/'+' ')): 5,
        '}': 7,
    },
    9: {
        '=': 10,
        '>': 11,
        '-': 12,
    },
    17: {
        '=': 18
    },
    20: {
        numero: 20,
        '.': 21,
        tuple('E' + 'e'): 23
    },
    21: {
        numero: 22
    },
    22: {
        numero: 22
    },
    23: {
        '+': 24,
        '-': 25,
    },
    24: {
        numero: 26
    },
    25: {
        numero: 22
    },
    26: {
        numero: 26
    }
}

# def estados finais
estadosFinais = {
    2: 'id',
    3: 'lit',
    4: 'OPM',
    7: 'comentario',
    8: 'EOF',
    9: 'OPR',
    10: 'OPR',
    11: 'OPR',
    12: 'RCB',
    13: 'AB_P',
    14: 'FC_P',
    15: 'PT_V',
    16: 'VIR',
    17: 'OPR',
    18: 'OPR',
    19: '=',
    20: 'num',
    22: 'num',
    26: 'num',

}


def scanner(automato, aceitacao,tab_simb, entrada, marcador):
    estado = 0
    lexema =''
    tipo = ''
    for c in entrada:
        erro['colAt'] += 1
        marcador += 1
        try:
            estado = next(automato[estado][key] for key in automato[estado] if c in key)

            if c in espacos:
                if estado == 5 or estado == 6 or estado == 1:
                    lexema += c
            else:
                lexema += c

        except Exception:
            marcador -= 1
            erro['colErro'] = erro['colAt']

            if c == '\n':
                erro['linha'] += 1
                erro['colAt'] = 1


            if estado in aceitacao:
                classe = aceitacao[estado]

                if busca_tabela_simbolos(tabela_simbolos, lexema):
                    return tabela_simbolos[lexema], marcador

                if estado == 20 or estado == 26:
                    tipo = 'inteiro'

                elif estado == 22:
                    tipo = 'real'

                elif estado == 2:
                    if busca_tabela_simbolos(tabela_simbolos, lexema):
                        print(tabela_simbolos[lexema])
                    else:
                        tipo = 'nulo'
                        inserir_tabela_simbolos(tab_simb, classe, lexema, tipo)

                else:
                    tipo ='nulo'

                return {
                    'classe': classe,
                    'lexema': lexema,
                    'tipo':tipo
                }, marcador
            else:
               print("ERRO LÉXICO \n LINHA: {} \n COLUNA: {} ".format(erro['linha'], erro['colErro']))
    #return {
              # 'classe': classe,
              # 'lexema': lexema,
              # 'tipo': tipo
          # }, marcador


def limpa (estado,lexema):
    estado = 0
    lexema =''

    return estado, lexema
def main ():

    arq = open('files/teste.mgol', "r")
    arq_lido = arq.read()
    marcador = 0
    while True:
        token, marcador = scanner(afd, estadosFinais, tabela_simbolos, arq_lido,marcador)
        arq.seek(marcador)
        arq_lido = arq.read()
        print(token)
if __name__ == '__main__':
  main()



