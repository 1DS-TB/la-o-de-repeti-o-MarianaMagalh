contador = 0

numero = int(input("Qual tabuada vc deseja: "))

if numero < 0:
    print("INVALIDO")
else:
    for num in range(11):
        if (numero <= 0) :
            print("INVALIDO")
        else:
            tabua = numero * num
            print(f"{numero} X {num} = {tabua}")