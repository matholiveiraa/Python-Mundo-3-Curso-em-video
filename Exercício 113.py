#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
#incluindo agora a possibilidade da digitação de um número de tipo inválido.
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
class Cores:
    VERMELHO = '\033[31m'
    VERDE = '\033[32m'
    AMARELO = '\033[33m'
    AZUL = '\033[34m'
    MAGENTA = '\033[35m'
    CIANO = '\033[36m'
    RESET = '\033[0m'  # Importante: reseta a cor para o padrão


def leiaInt(inteiro):
    while True:
        try:
            inteiro = int(input(inteiro))
            inteiro = int(inteiro)  # conversão de "valor" para valor
            print()
            print(f"O numero inteiro é: {inteiro}")
            break
        except ValueError:  # Trata o erro ao invés de quebrar o programa!
            print(Cores.VERMELHO + ' O valor inserido não é inteiro!' + Cores.RESET)

def leiaFloat(floati):
    while True:
        try:
            floati = float(input(floati))
            floati = float(floati)  # conversão de "valor" para valor
            print()
            print(f"O numero float é: {floati}")
            break
        except ValueError:  # Trata o erro ao invés de quebrar o programa!
            print(Cores.VERMELHO + ' O valor inserido não é float!' + Cores.RESET)



valor_inteiro = leiaInt("Digite um valor inteiro!: ")
valor_real = leiaFloat("Digite um valor real!: ")



