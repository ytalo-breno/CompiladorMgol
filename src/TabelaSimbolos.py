from AutomatoLexico import *

tabela_simbolos = {
    'inicio': {
        'classe': 'inicio',
        'lexema': 'inicio',
        'tipo': 'inicio',
    },
    'varinicio': {
        'classe': 'varinicio',
        'lexema': 'varinicio',
        'tipo': 'varinicio',
    },
    'varfim':{
        'classe': 'varfim',
        'lexema':'varfim',
        'tipo': 'varfim',


    },
    'escreva':{
        'classe':'escreva',
        'lexema': 'escreva',
        'tipo': 'escreva',
    },
    'leia':{
        'classe':'leia',
        'lexema':'leia',
        'tipo':'tipo',
    },
    'se':{
        'classe':'se',
        'lexema':'se',
        'tipo':'se',
    },
    'entao':{
        'classe':'entao',
        'lexema':'entao',
        'tipo':'entao',
    },
    'fimse':{
        'classe':'fimse',
        'lexema':'fimse',
        'tipo':'fimse',
    },
    'repita':{
        'classe':'repita',
        'lexema':'repita',
        'tipo':'repita',
    },
    'fimrepita':{
        'classe':'fimrepita',
        'lexema':'fimrepita',
        'tipo': 'fimrepita',
    },
    'fim':{
        'classe':'fim',
        'lexema':'fim',
        'tipo':'fim',
    },
    'inteiro':{
        'classe':'inteiro',
        'lexema':'inteiro',
        'tipo':'inteiro',
    },
    'literal':{
        'classe':'literal',
        'lexema':'literal',
        'tipo':'literal',
    },
    'real':{
        'classe':'real',
        'lexema':'real',
        'tipo':'real',
    }
}


def inserir_tabela_simbolos(tabela_simbolos, classe, lexema, tipo):
    tabela_simbolos[lexema] = {
        'classe': classe,
        'lexema': lexema,
        'tipo': tipo
    }
def busca_tabela_simbolos(tabela_simbolos,lexema):
    for key in tabela_simbolos:
        if lexema == key:
            return True
    else:
        return False


if __name__ == '__main__':
    x = busca_tabela_simbolos(tabela_simbolos, 'se')
    print(x)