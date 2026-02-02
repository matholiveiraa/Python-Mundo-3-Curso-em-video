#Crie um módulo chamado moeda.py que tenha as 
# funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from modulos.utilidadescev import moeda
#fat = uteis.fatorial(num)

while True:
    valor = input("Digite o valor: ") #Sempre retorna string.

    try: #Tentar algo que pode dar erro!
        valor = float(valor) #conversão de "valor" para valor
        print(moeda.resumo(valor))
        break
    except ValueError: #Trata o erro ao invés de quebrar o programa!
        print("Valor invalido")


