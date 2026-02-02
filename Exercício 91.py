#Exercício Python 091: 
#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
#sabendo que o vencedor tirou o maior número no dado.
#Sem entrada de dados
#jogador sempre vai no dicionário
#resultado sempre na lista
from random import randint
import time
from operator import itemgetter
lista = {"Jogador 1": randint(1,6),
         "Jogador 2": randint(1,6),
         "Jogador 3": randint(1,6),
         "Jogador 4": randint(1,6)}

listaordenarada = sorted(lista.items(), key=itemgetter(1), reverse=True)

for keys, values in lista.items():
    print(f"{keys}, tirou: {values}")
    time.sleep(1)

print()



for colocacao, jogador in enumerate(listaordenarada):
    print(f"{colocacao+1}º lugar: {jogador[0]}, com {jogador[1]}") #jogador[0] seria apenas o nome dele, jogador[1] o resultado dele

  


    