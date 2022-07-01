
# definindo letra e número
letter = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
number = tuple("0123456789")
aritm = tuple("+-/*")

#definicao de estados


#AUTOMATO (EU ACHO)
dfa = {
    0: {' ': 0,
        tuple('\"'+'\''): 1,
        letter: 2,
        aritm: 4,
        '{': 5,
        '$': 8, #mudar essa parada depois EOF
        '<': 9,
        '(': 13,
        ')': 14,
        ';': 15,
        ',': 16,
        '>': 17,
        '=': 19,
        number: 20
        },
    1: {
        (letter + number + tuple(' ')): 1,
        tuple('\"'+'\''): 3
    },
    2: {
        letter + number + tuple('_'): 2,
    },
    5:{
        (letter + number + aritm + tuple(' '+ '<'+'(' +')' + ';' + ',' + '>' + '=' + '.'+':')): 5,
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
        number: 20,
        '.': 21,
        tuple('E'+'e'): 23
    },
    21: {
        number: 22
    },
    22: {
        number: 22
    },
    23: {
        '+': 24,
        '-': 25,
    },
    24: {
        number: 26
    },
    25: {
        number: 22
    },
    26: {
        number: 26
    }
}

#def estados finais
finalStates = {
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


def teste(trans, init, aceitacao ,string):
    #breakpoint()
    estado = init
    for c in string:
        estado = next(trans[estado][key] for key in trans[estado] if c in key) #como eu vou explicar essa merda??
    if estado in aceitacao:
        print(aceitacao[estado])
        return aceitacao[estado]


teste(dfa,0 , finalStates,)
#print(dfa[0])

