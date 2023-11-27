# count - função é contar quantas vezes um determinado caractere aparece em uma string
# upper e a lower - dois metodos que deixam a string toda em maiuscula ou a string toda em minuscula
#find - busca por uma experssão dentro da frase
#replace - é utilizado para realiar alterações dentro das strings
#capitalize - deixa a primeira lera das palavra maiusculas
#split - transforma sua string em uma lista
frase = "A banana é amarela e o abacate é verde. ".lower()
letra = 'e'
email = ' paulo.junior@gmail.com  '
print(f'A letra "{ letra }" aparece { frase.count(letra)} vezes na frase "{ frase }".')
achei = frase.find('é')
if achei >= 0:
    print(f'A expressão foi encontrada no indice { achei }')
else:
    print(f'A expressão NÃO foi encontrada na frase')


nova_frase = frase.replace('banana', 'maracuja')
nova_frase2 = frase.replace('abacate', 'manga')
nova_frase2 = frase.replace(' ', '')
print(frase)
print(nova_frase)
print(nova_frase2)
print(email.replace(' ', ''))
print(frase.capitalize())
print(frase.split())


# 1. Faca um programa que peça uma string e a imprima.
# 2. Crie um programa que imprima o comprimento de uma string.
# 3. faça um programa que peça um nome e imprima as 4 primeiras letras desse nome
# 4. faça um programa que peça duas strings e compare as duas, imprima o resultado
# 5. faça um programa que peça um nome e imprima quantas vogais tem nesse nome
# 6. Faca um programa que peça um nome do usuario. O programa imprime o nome sem suas vogais
# 7. Faca um programa que peça uma palavra e a imprima de tras-para-frente

nome = input('Digite um nome'); print(nome[::-1])