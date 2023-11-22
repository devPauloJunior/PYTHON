# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
# 1 2 3 4 5 6 7 8 9 10 11

numero = int(input('Favor informar um numero inteiro: '))
intervalo = range(1, numero+1)
contador = 0
for i in intervalo:
    if numero % i == 0:
        print(f'foi divisivel por { i }')
        contador += 1

if contador == 2 or contador == 1:
    print(f'O numero { numero } é primo')