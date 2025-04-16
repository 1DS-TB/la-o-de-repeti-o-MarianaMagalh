num = int(input("Insira um número: "))

fato = 1
i = 1

if num < 0:
    print("INVALIDO")
else:
    while i <= num:
        fato *= i
        i += 1
    print(f"{num}! = {fato}")