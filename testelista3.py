a = [1,2,3,4,5]

b = a[:] #b recebe todos os valores de a
#Não podemos fazer b = a, porque qualquer alteração do b ele também altera o a
#razão, porque  o python acaba fazendo uma ligação das duas listas
b[4] = 22

print(f"A lista a: {a}")
print(f"A lista b: {b}, repara o 22 no final")
