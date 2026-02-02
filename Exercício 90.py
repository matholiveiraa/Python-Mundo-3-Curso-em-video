aluno = {}

for c in range(1):
    aluno['nome'] = str(input("Nome: "))

    aluno['media'] = int(input("Média: "))

    aluno['condição'] = ""

    if aluno["media"] >= 6:
        aluno['condição'] = "Aprovado!"
    elif aluno['media'] < 6:
        aluno['condição'] = "Reprovou"

print()
print(f"O nome é: {aluno['nome']}")
print(f"A média é igual a: {aluno['media']}")
print(f"A condição do aluno é: {aluno['condição']}")





