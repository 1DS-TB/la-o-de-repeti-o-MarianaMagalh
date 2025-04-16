k = []

inicio = int(input("Insira o começo do intervalo: "))
fim = int(input("Insira o final do intervalo: "))

for num in range(inicio, fim + 1):
    verificacao = "{:02d}".format(num ** 2)

    esquerda = verificacao[0:len(verificacao)//2]
    direita = verificacao[len(verificacao)//2:len(verificacao)]

    soma = int(esquerda) + int(direita)

    if soma == num:
        k.append(soma)
    else:
        print("O número não é Kaprekar.")

print(f"Os números Kaprekar {k}")