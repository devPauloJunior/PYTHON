# condição ternaria acontece em formato de linha

salario = float(input('Informe o valor do seu salario: '))

if salario >= 2500.00:
    print("IR será cobrado")
else:
    print('Ir não será cobrado')

variavel_controle = 'IR será cobrado' if salario >= 2500.00 else 'IR não será cobrado'

print(variavel_controle)


vr_controle = 'OK 1' if True else 'Ok 2' if False else 'Fim'

print(vr_controle)

if True:
    print('Ok 1')
elif False:
    print('OK 2')
else:
    print('Fim')