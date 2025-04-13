num = int(input("Insira um número: "))

fatorial = 1
i = 1

while i <= num:
    fatorial *= i
    i += 1
print(f"{num}! = {fatorial}")