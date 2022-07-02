
from AutomatoLexico import *
from TabelaSimbolos import *


def scanner(arq_string,tabela_simbolos,afd,estados_finais):
  classe =reconhecedor(afd,0,estados_finais,arq_string)
  print (classe)
    #return token

scanner('eai',tabela_simbolos,afd,estadosFinais)