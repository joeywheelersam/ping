# Comando para Executar:
# python ping.py [url] [quantidade_pings]
# Obs.: url sem o www, apenas o dominio.
# Exemplo de url: uol.com.br

import os
import sys

# Le os Argumentos do Comando
argumentos = sys.argv
try:
    host = argumentos[1]
    quantidade = argumentos[2]
except:
    print("Faltam argumentos no comando")
    sys.exit(1)

def myping(host):
    response = os.system("ping -c " + quantidade + " " + host)
 
print(myping(host))
