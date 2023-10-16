"""
Você foi convidado(a) para uma viagem para o Rio de Janeiro. No passeio aos 04 principais pontos turisticos do Rio devem ser coletadas as cotas de cada um dos 30 participantes.
"""
nome = []
marcana = []
pao_de_acucar = []
for x in range(3):
    nome.append(input("nome: "))
    marcana.append(input("maracana: "))
    pao_de_acucar.append(input("pao de acucar: "))

contador = 0
for y in nome:
    print("o participante {} escolhei {} para maracana e escolheu {} para o pao de acucar".format(y, marcana[contador], pao_de_acucar[contador]))
    contador += 1
    
#mulher01,idade,estado_civil,cidade
#mulher02,idade,estado_civil,cidade

mulher01_idade = 34
mulher01_estado_civil = "solteira"
mulher01_cidade = "Amontada"

mulher02_idade = 21
mulher02_estado_civil = "solteira"
mulher02_cidade = "São Paulo"

print("A maior idade é: ", mulher01_idade)
print("As duas são: ",mulher01_estado_civil)
print("As duas moram no Brasil")

"""
valor01 = 78
valor02 = 78

if valor01 > valor02:
    print("O maior valor entre as duas variaveis é {}".format(valor01))
elif ( valor01 == valor02):
    print("Os dois valores são iguais")
else:
    print("O maior valor entre as duas variaveis é {}".format(valor02))


a = [2,4,6,8,10,12,14,16,18,20]
b = [1,4,8,12,16,18,20]

for x in a:
    if x in b:
        print("valor igual {}".format(x))
"""