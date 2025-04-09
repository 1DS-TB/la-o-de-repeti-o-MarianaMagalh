somar = 0
contador = 1

num = int(input("Insira um número: "))

if num <= 0:
    print("INVALIDO")
else:
    while contador <= num:
        somar += contador
        contador += 1
    print(f"A soma do número {num} é {contador}")