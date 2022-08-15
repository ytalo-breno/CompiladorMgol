from TabelaSimbolos import *

letra = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
numero = tuple("0123456789")
aritm = tuple("+-/*")
espacos = tuple('\t ')
alfabeto = letra + numero + aritm + espacos + tuple("\'\"{}()<=>;,:\\\n_")
erro = {'linha':1,'colAt':0,'colErro':0}

# tabela de transição de estados
afd = {
    0: {espacos: 0,
        tuple('\"' + '\''): 1,
        letra: 2,
        aritm: 4,
        '{': 5,
        '$': 8,
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
        (letra + numero + aritm + tuple(' ' + '<' + '(' + ')' + ';' + ',' + '>' + '=' + '.' + ':'+'/' + '\\')+espacos):1,
        tuple('\"' + '\''): 3
    },
    2: {
        letra + numero + tuple('_'): 2,
    },
    5: {
        (letra + numero + aritm + tuple(' ' + '<' + '(' + ')' + ';' + ',' + '>' + '=' + '.' + ':' + '/'+'\\')+espacos):5,
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
    4: 'opm',
    6: 'erro',
    7: 'comentario',
    8: 'eof',
    9: 'opr',
    10: 'opr',
    11: 'opr',
    12: 'rcb',
    13: 'ab_p',
    14: 'fc_p',
    15: 'pt_v',
    16: 'vir',
    17: 'opr',
    18: 'opr',
    19: '=',
    20: 'num',
    22: 'num',
    26: 'num',

}


def scanner(automato, aceitacao,tab_simb, entrada, marcador):
    estado = 0
    lexema =''
    tipo = ''
    tipoErro = ''
    chaveAberta = False
    aspasAbertas = 0


    for c in entrada:
        erro['colAt'] += 1
        marcador += 1
        if c =='{':
            chaveAberta = True
        elif c =='}':
            chaveAberta = False
        if c == '\'' or c =='\"':
            aspasAbertas += 1


        try:
            estado = next(automato[estado][key] for key in automato[estado] if c in key)

            if c in espacos:
                if estado == 5 or estado == 1:
                    lexema += c
            else:
                lexema += c



        except Exception:
            marcador -= 1
            if c == ' ':
                erro['colAt']-=1

            if c == '\n':
                erro['linha'] += 1
                erro['colErro'] = erro['colAt']
                erro['colAt'] = 0


            if c in alfabeto and estado in aceitacao:
                classe = aceitacao[estado]

                if busca_tabela_simbolos(tabela_simbolos, lexema):
                    return tabela_simbolos[lexema], marcador

                if estado == 20 or estado == 26:
                    tipo = 'inteiro'

                elif estado == 22:
                    tipo = 'real'

                elif estado == 2:
                    if busca_tabela_simbolos(tabela_simbolos, lexema):
                        return tabela_simbolos[lexema], marcador
                    else:
                        tipo = 'nulo'
                        inserir_tabela_simbolos(tab_simb, classe, lexema, tipo)

                else:
                    tipo ='nulo'

                if estado == 7:
                    marcador += 1
                    lexema = ''
                    estado = 0
                    continue

                return {
                    'classe': classe,
                    'lexema': lexema,
                    'tipo': tipo
                }, marcador

            else:
                marcador +=1

                if c =='\n':
                    erro['linha']-=1

                if not lexema:

                    erro['colErro'] = erro['colAt']

                    if c not in alfabeto:
                        erro['colAt']-=1
                        tipoErro = 'caracter invalido: {}'.format(c)
                        print("ERRO LÉXICO:{} \n LINHA: {} \n COLUNA: {} ".format(tipoErro, erro['linha'], erro['colErro']))

                    continue

                if c not in alfabeto:
                    erro['colErro'] = erro['colAt']
                    tipoErro ='caracter invalido: {}'.format(c)

                if chaveAberta == True and c == '\n':
                    tipoErro = 'Não fechou chaves'
                    erro['colErro']-=1
                    # print("ERRO LÉXICO:{} \n LINHA: {} \n COLUNA: {} ".format(tipoErro, erro['linha'], erro['colErro']))

                if aspasAbertas %2 != 0 and c == '\n':

                    tipoErro = 'Não fechou aspas'


                    erro['colErro']-=1
                    # print("ERRO LÉXICO:{} \n LINHA: {} \n COLUNA: {} ".format(tipoErro, erro['linha'], erro['colErro']))

                if estado == 21 or estado == 23 or estado == 24 or estado == 25:


                    tipoErro = 'Expressão incompleta'


                print("ERRO LÉXICO:{} \n LINHA: {} \n COLUNA: {} ".format(tipoErro, erro['linha'], erro['colErro']))

                estado = 0
                lexema=''
                continue

    if busca_tabela_simbolos(tabela_simbolos, lexema):
        return tabela_simbolos[lexema],marcador

    if estado in aceitacao:
        classe = aceitacao[estado]

        return {
                   'classe': classe,
                   'lexema': lexema,
                   'tipo': tipo
               }, marcador



    if not entrada:
        estado = 8
        classe = aceitacao[estado]
        return {
            'classe': classe,
            'lexema': 'EOF',
            'tipo': 'EOF'
        },marcador
