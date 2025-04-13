num = int(input("Insira um número: "))

somar = 0
contador = 1

while contador <= num:
    somar += 1
    contador += 1
    fabonacci = contador + contador
    print(f"{contador} + {somar} = {fabonacci}")