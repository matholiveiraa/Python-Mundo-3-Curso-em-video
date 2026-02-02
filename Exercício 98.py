#Faça um programa que tenha uma função chamada contador()
#que receba três parâmetros: início, fim e passo. 
#Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            
# a) de 1 até 10, de 1 em 1                                                                                                                                              
# b) de 10 até 0, de 2 em 2                                                                                                                                            
# c) uma contagem personalizada

import time
def contador(inicio, final, passo):

    for teste in range(inicio,final+1,passo):
        print(f"{teste} ", end="")

        time.sleep(0.2)

def pula():
    print('-=' * 30)


contagem = (1,10,1)
contagem1 =(10,-2,-2)
contador(*contagem)
print()
contador(*contagem1)

contagem_custom = []

inicio_custom = int(input("\nDigite o inicio: "))
contagem_custom.append(inicio_custom)

final_custom = int(input("Digite o final: "))
contagem_custom.append(final_custom)

passo_custom = int(input("Digite o passo: "))
contagem_custom.append(passo_custom)

contador(*contagem_custom)

