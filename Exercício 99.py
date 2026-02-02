#Faça um programa que tenha uma função chamada maior(), 
#que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(lista_valores):
    print(lista_valores)
    print(f"O maior valor é {max(lista_valores)}")




lista_valores = []
contador = 0 
while True:
    contador += 1
    numero = int(input(f"Digite o {contador}º valor: "))
    lista_valores.append(numero)
    perguntar_contunuidade = str(input("Deseja continuar? [s/n]: ")).lower()
    if perguntar_contunuidade == "n":
        break
    elif perguntar_contunuidade == "s":
        pass  # não precisa fazer nada, o loop continua
    else:
        print("Opção inválida, assumindo continuídade")
        pergunta_novamente = str(input("Deseja continuar? [s/n]")).lower()
        if pergunta_novamente == "n":
            break

    
maior(lista_valores)
        