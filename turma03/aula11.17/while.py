# while = enquanto

# loop infinito
# while True:

# contador =  0
# while contador < 300:
#     contador += 1 # contador = contador + 1
#     print(contador)
#     if contador == 12:
#         print("Cheguei no 12")

#     if contador == 290:
#         break
    
# print("Saiu do While")

#Peça a idade de 20 alunos. Faça um codigo que avisa quando o aluno tem mais de 13 anos.

# contador = 0
# while contador < 5:
#     idade_aluno = int(input('Informe sua idade: '))
#     if idade_aluno > 13:
#         print(f'O aluno { contador } tem mais de 13 anos')
#     contador += 1

#faça um codigo que peça uma nota, entre zero e dez. Se a nota for menor que 0 e maior que 10 saia do codigo

# contador = 0
# while contador <= 10:
# #enquanto o contador for menor ou igual a 10 faça:
#     nota = float(input('Informe uma nota: '))
#     if nota < 0 or nota > 10:
#         print('Sua nota não foi sufucuente para continuar')
#         break 
#     contador = contador + 1

# while True:
#     nota = int(input('informe a nota: '))
#     if nota < 0 or nota > 10:
#         break


#Peça a idade de 20 alunos. Faça um codigo que avisa quando o aluno tem mais de 13 anos.

aluno = 1
while aluno <= 20:
    idade = int(input(f'Qual idade do aluno { aluno }?'))
    if idade > 13:
        print(f'A idade do aluno { aluno } é { idade }. E maior que 13.')
    aluno = aluno + 1
print('Fim da questão 01')


