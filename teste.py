""" sexo =""
idade = 0
qtdMulheres = 0
qtdHomens = 0
for i in range(0,5):
    sexo = input("Digite sexo M ou H")
    idade = int(input("Digite a idade"))
    
    if (sexo=="M" or sexo=="m"):
        qtdMulheres+=1
    elif (sexo=="H" or sexo=="h"):
        qtdHomens+=1


print("A qtd de mulheres é: ", qtdMulheres)
print("A qtd de homens é: ", qtdHomens)

contador = 0
notas = 0
while contador < 6:
    notas = float(input("digite a nota do aluno"))
    contador+=1

media = notas/contador

print("A media de notas é: ", media)
maiorNota = 0
contador = 0
nota = 0
somaNotas = 0
while contador < 3:
    nota = float(input("Digite a nota do Aluno"))
    somaNotas = somaNotas + nota
    contador+=1 

    if (contador==1):
        maiorNota = nota
    else:
        if (nota>maiorNota):
            maiorNota = nota
        
media = somaNotas/contador

print("A media de noas ´: ", media)
print("A maior nota foi: ", maiorNota)

x = 10
exp = x**2
if (exp >= (x+200)):
    print(exp)
    print("o valor de exp é maior opu igual a x")
else:
    print(exp)
    print("O valor do exp é menor que x" )"""

x = 5
div = x//2
if (div>=(x-3)):
    print(div)
    print("o valor de div é maior ou igual a x")
else:
    print(div)
    print("o valor de div é menor que x")
