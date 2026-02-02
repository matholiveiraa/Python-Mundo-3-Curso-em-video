#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import datetime

def voto(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    
    if idade >= 18 and idade < 70:
        print("Voto obrigatório")
    
    elif 16 <= idade <= 17:
        print("Voto opcional")
    elif idade < 16:
        print("Não vota")
    elif idade >= 70:
        print("Voto opcional")
    



ano_nascimento = int(input("Digite o ano de nascimento: "))

voto(ano_nascimento)