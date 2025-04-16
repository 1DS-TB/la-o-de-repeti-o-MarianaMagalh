numero = int(input("Insira um número: "))

while True:
    if numero % 1 == 0 and numero % numero == 0:
        print("primo")
        break
    else:
        print("INVALIDO")
        break