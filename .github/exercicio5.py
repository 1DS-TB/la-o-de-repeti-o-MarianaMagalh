num = int(input("Insira um número: "))

while True:
    if num % 1 == 0 and num % num == 0:
        print("primo")
        break
    else:
        print("INVALIDO")
        break