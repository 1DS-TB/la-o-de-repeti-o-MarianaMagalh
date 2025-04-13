contador = 0

numeros = int(input("Qual tabuada vc deseja: "))

for num in range(11):
    if numeros <= 0 :
        print("INVALIDO")
    else:
        tabua = numeros * num
        print(f"{numeros} X {num} = {tabua}")