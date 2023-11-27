preco = float(input('Informe o preço do seu produto: '))

desconto01 = 0.2
desconto02 = 0.5
desconto03 = 0.8

if preco < 100:
    valor = preco * desconto01
    print(valor)
elif preco >= 100 and preco <=500:
    valor = preco * desconto02
    print(valor)
elif preco > 500:
    valor = preco * desconto03
    print(valor)
else:
    print(f'O preço { preco } não se aplica em nenhuma faixa de desconto')