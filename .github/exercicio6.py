num = int(input("Insira um número: "))

f =[]

somar = 0
contador = 1
if num < 0:
    print("INVALIDO")
else:
    while contador <= num:
        somar += 1
        contador += 1
        fabonacci = contador + contador
        f.append(fabonacci)
    print(f"{f}")