from modulos import usuarios
from modulos.usuarios import sair
from modulos.usuarios import cadastrar
from modulos.usuarios import lerpessoas


class Cores:
    RESET = '\033[0m'
    NEGRITO = '\033[1m'
    VERMELHO = '\033[31m'
    VERDE = '\033[32m'
    AMARELO = '\033[33m'
    AZUL = '\033[34m'
    MAGENTA = '\033[35m'
    CIANO = '\033[36m'
    BRANCO = '\033[37m'

    # Cores de Fundo
    FUNDO_VERMELHO = '\033[41m'
    FUNDO_VERDE = '\033[42m'


#Parte Principal

print("-="*30)
print("                    Menu Principal")
print("-="*30)
print(Cores.AZUL + "1" + Cores.RESET + "- Ver pessoas cadastradas")
print(Cores.AZUL + "2" + Cores.RESET + "- Cadastrar pessoas")
print(Cores.VERMELHO + "3" + Cores.RESET + "- Sair")

choise = int(input("Digite sua escolha: "))
if choise == 3:
    sair(choise)
elif choise == 2:
    cadastrar(choise)
else:
    choise == 1
    lerpessoas(choise)




