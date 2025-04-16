soma = 0
cont = 1

num = int(input("Insira um número: "))

if num <= 0:
    print("INVALIDO")
else:
    while cont <= num:
        soma += cont
        cont += 1
    print(f"A soma do número {num} é {cont}")