#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas
#– A maior nota
#– A menor nota
#– A média da turma
#– A situação (opcional)


def notas(lista_notas):
    contador = 1
    final_notas = dict()
    lista_notas = list()

    #Parte de repetição
    while True:
        notas = int(input(f"Digite a {contador}º nota: "))
        lista_notas.append(notas)

        contador += 1

        continuidade = str(input("Digite se quer continuar [s/n]: ")).lower()
        if continuidade == "n":
            break

    final_notas["notas"] = lista_notas
    final_notas["maior"] = max(lista_notas)
    final_notas['menor'] = min(lista_notas)
    final_notas['media'] = (sum(lista_notas)) /len(lista_notas)

    if (sum(lista_notas)) /len(lista_notas) >= 6:

        final_notas['situação'] = "Aprovado"
    else:
        final_notas['situação'] = "Reprovado"
    
    print(f"Sua lista de notas{lista_notas}")
    print()
    print(f"Sua situação {final_notas}")

#Programa principal
executar = list()
notas(executar)



    