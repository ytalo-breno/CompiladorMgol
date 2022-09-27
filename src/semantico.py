from TabelaSimbolos import *

pilha_semantica = []
nao_terminais = {
    'TIPO': None,
    'L': None,
    'D': None
}
def r5():
    arqobj.write('\n\n\n')

def r6():
    for _ in range(3):
        pilha_semantica.pop()

    pilha_semantica.append(nao_terminais['D'])


def r7():
    for _ in range(3):
        token = pilha_semantica.pop()
        atualizar_tabela_simbolos(tabela_simbolos,token['lexema'],nao_terminais['L']['tipo'])
        #token['tipo'] = nao_terminais['L']

    pilha_semantica.append(nao_terminais['L'])
    if tabela_simbolos[token['lexema']]['tipo'] == 'literal':
        write('literal')
    elif tabela_simbolos[token['lexema']]['tipo'] == 'inteiro':
        write('int')
    else:
        write('double')
    write(f" {token['lexema']} ;\n")


def r8():
    token = pilha_semantica.pop()
    atualizar_tabela_simbolos(tabela_simbolos, token['lexema'], nao_terminais['L']['tipo'])
    #token['tipo'] = nao_terminais['L']

    pilha_semantica.append(nao_terminais['L'])
    write(f"{token['lexema']} ;\n")


def r9():
    nao_terminais['TIPO'] = pilha_semantica.pop()
    nao_terminais['L']= nao_terminais['TIPO']
    pilha_semantica.append(nao_terminais['TIPO'])


    write("int ")


def r10():
    token = pilha_semantica.pop()
    nao_terminais['TIPO'] = token
    nao_terminais['L'] = nao_terminais['TIPO']
    pilha_semantica.append(nao_terminais['TIPO'])

    write("double ")



def r11():
    nao_terminais['TIPO'] = pilha_semantica.pop()
    nao_terminais['L']= nao_terminais['TIPO']
    pilha_semantica.append(nao_terminais['TIPO'])

    write(f"{nao_terminais['TIPO']['tipo']} ")

def r13 ():
    pilha_semantica.pop()
    token = pilha_semantica.pop()
    pilha_semantica.pop()
    tipo = tabela_simbolos[token['lexema']]['tipo']
    if tipo == 'literal':
        write(f"scanf(\"%s\",{tabela_simbolos[token['lexema']]['lexema']});\n")
    elif tipo == 'inteiro':
        write(f"scanf(\"%d\",&{tabela_simbolos[token['lexema']]['lexema']});\n")
    elif tipo == 'real':
        write(f"scanf(\"%lf\",&{tabela_simbolos[token['lexema']]['lexema']});\n")
    else:
        print('\nERRO SEMANTICO: VARIÁVEL NÃO DECLARADA BOCÓ\n')


regras = [None,None,None,None,None,r5,r6,r7,r8,r9,r10,r11,None,r13]

arqobj = open('prog.c', 'w')







def write(coisapraescrever):
    arqobj.write(coisapraescrever)

def escolhe_regra (numregra):
    try:
        if regras[numregra]:
            f = regras[numregra]
            f()
        elif numregra == 2:
            arqobj.close()
    except Exception:
        print('foi de caixa')


