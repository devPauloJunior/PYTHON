# funções são blocos de codigos que são executados somente quando são chamados
# parametro: def
# as funções devem ter prioridade no codigo
def media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) /3
    return media


nota01 = int(input('Informe a primeira nota: '))
nota02 = int(input('Informe a segunda nota: '))
nota03 = int(input('Informe a terçeira nota: '))

print(media(nota01, nota02, nota03))


nota04 = int(input('Informe a primeira nota: '))
nota05 = int(input('Informe a segunda nota: '))
nota06 = int(input('Informe a terçeira nota: '))

print(media(nota04, nota05, nota06))


def calcula_horas_extras(quantidade_horas, valor_hora):
    horas = float(quantidade_horas)
    taxa = float(valor_hora)

    if horas >= 40:
        valor_receber = (horas - 40) * taxa
    
    return valor_receber

quantidade_horas = float(input('Informe o total de horas trabalhadas: '))
valor_da_hora = float(input('Informe o valor da taxa do colaborador: '))

salario = 1400.00
print(salario + calcula_horas_extras(quantidade_horas, valor_da_hora))

#Faça um codigo, com uma função que necessite de um valor. A função retorna o caractere ‘P’, se seu valor for positivo, e ‘N’, se seu valor for zero ou negativo.