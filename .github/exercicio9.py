perfeitos = []

for num in range(10000):
    divisores = []
    for i in range(1, num):
        if num % i == 0:
            divisores.append(i)

    soma = 0

    for x in divisores:
        soma += x

    if soma == num and num != 0:
        perfeitos.append(soma)

print(perfeitos)

