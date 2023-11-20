# i - variavel de controle
for i in range(5):
    print(i)

x = range(5)
for i in x:
    print(i)

maior = 0
for x in range(5):
    numero = int(input('Informe um numero: '))
    if maior < numero:
        maior = numero

print(f'O maior numero É: { maior }.')