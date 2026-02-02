#Python 092: 
#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o 
# (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from time import sleep
from datetime import date
import datetime

data_atual = datetime.date.today().year


dados = {}

for C in range(1):
    dados['nome'] = str(input("Nome: "))

    sleep(1)

    dados['ano de nascimento'] = int(input("Ano de nascimento: "))

    sleep(1)

    dados['carteira'] = int(input("CTPS: "))

    if dados['carteira'] == 0:
        print("=" * 30)
        for keys, values in dados.items():
            print(F"{keys}: {values}")
    
    else:
        dados['carteira'] != 0 
        dados['ano de contratação'] = int(input("Ano de Contração: "))
        dados['salario'] = int(input("Salário: "))
        print("=" * 30)
        for keys, values in dados.items():
            print(f"{keys}: {values}")

        anoaposentadoria = dados['ano de contratação'] + 35 #Calculei ano da aposentadoria com ano da contratação mais 35 anos 
        print(f"Ano de aposentadoria: {anoaposentadoria}")

        #Parte de calculo da idade e ano

        idadeaposentar = anoaposentadoria - dados['ano de nascimento'] #Idade de se aposentar é igual ao ano de aposentaria - menos o ano de nascimento

        print(f"Você irá se aposentar com {idadeaposentar} anos")

    
