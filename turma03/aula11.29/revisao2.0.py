# estruturas condicionais
variavel = 120
if variavel < 20:
    print('menor que 20')
elif variavel == 20:
    print('Igual a 20')
elif variavel > 20 and variavel < 50:
    print('Está no intervalo entre 21 e 49')
else:
    print('Qualquer outra coisa')

# estruturas de repetição
# FOR e WHILE
for i in range(1, 10, 2):
    print(f'print o numero { i }') 

contador = 5
while contador > 0:
    print(f'Esse é o print do numero { contador } ')
    contador -= 1

# monte uma data valida com a lista abaixo join - unir strings
lista = ['2023', '23', '12']
nome = '/'.join(lista)
print(nome)
