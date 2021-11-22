# Instalar: pip install ping3
# Upgrade: pip install --upgrade ping3
# Desinstalar: pip uninstall ping3

from ping3 import ping , verbose_ping

def myping(host):
    verbose_ping(host)
    print ("")
    resp = ping(host)
    if resp == False:
        return False
    else:
        return True

endereco = input("Digite o endereço: ")
print(myping(endereco))
