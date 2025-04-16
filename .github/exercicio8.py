n = int(input("Insira os números: "))

contador = 1

if n < 0:
    print("INVALIDO")
else:
    while contador <= n:
        contador += 1
        s = 1 + (1/n)
print(f"Serie harmonica: {s:.2f}")
