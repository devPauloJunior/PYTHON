termo = int(input("Informe um numero: "))
num1, num2 = 0, 1
contador = 0
while contador < termo:
    num3 = num1 + num2
    if num3 == termo:
        print("Termo encontrado")
        break

    num1 = num2
    num2 = num3
    contador += 1
