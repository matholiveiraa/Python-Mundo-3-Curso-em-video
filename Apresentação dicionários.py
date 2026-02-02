pessoas = {'nome': 'Matheus', 'sexo': 'M', 'idade': 20}

print(f"O {pessoas['nome']} tem {pessoas['idade']} anos de idade")

print(pessoas.keys()) #Aqui serve para me mostrar as chaves: nome, sexo, idade

print(pessoas.values()) #Aqui me me mostra apenas os valores das chaves, que seria meu nome a idade e o sexo

print(pessoas.items()) #Me mostra tudo

for key in pessoas: #Usei um for para me mostrar as chaves mais limpas, sem tanta poluição visual
    print(key)

print()

for key in pessoas.keys():
    print(key)
print()

for key, values in pessoas.items(): #Aqui me mostra o nome, sexo e idade, com seus respectivos valores
    print(f"{key} = {values}")

#del pessoas['sexo'] usaria para apagar o sexo, ficaria apenas nome e idade

pessoas['peso'] = 86