# Alguns cuidados com dados mutaveis
# mutaveis - são dados que podem ter seu valor alterado na memoria do dispositivo
# imutaveis - são dados que só podem ser copiados da memoria do dispositivo

lista = ['João', 'Paulo']
lista = [ 'Francisco', 'Jose' ]
lista[1] = 'Pedro'
print(lista)
nome = 'Paulo' # seu endereço de memoria é 71y2jk3ghgqjheg
# nome = 'João'
# print(nome[2])
# nome[2] = 'a'
novo_nome = nome # seu endereço de memoria é 9123ehsadahdio
nome = 'João' # seu endereço de memoria é 71y2jk3ghgqjheg
print(nome)
print(novo_nome)

lista_a = [ 'João', 'Paulo' ] # endereço de memoria 19i3e345345qw
lista_b = lista_a
lista_c = lista_b
lista_b[1] = 'Jose'
print(lista_a)
print(lista_b)
print(lista_c)