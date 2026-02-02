def linha():
    print("=" * numero)
    print(msg)
    print("=" * numero)

msg = str(input("Digite a mensagem: "))
msg = (f" {msg}")
msglida = len(msg)

numero = msglida+1

linha()
