'''
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
'''


k = []

num = int(input("Inserir: "))

verificacao = "{:02d}".format(num ** 2)

esquerda = verificacao[0:len(verificacao)//2]
direita = verificacao[len(verificacao)//2:len(verificacao)]

soma = int(esquerda) + int(direita)

if soma == num:
    k.append(soma)
else:
    print("Não é k")

print(k)
