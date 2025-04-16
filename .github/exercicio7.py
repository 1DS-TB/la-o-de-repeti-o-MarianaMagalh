n = int(input("Insira um número: "))
m = " "

if n < 0:
    print("INVALIDO")
else:
    while True:
        for i in range(1, n + 1):
            m = m + "*"
            print(m)
        break