# uma lista é representada pelos []
# len - metodo que retorna a quantidade de itens de uma lista
# append - metodo que insere itens no final da lista
# del - remove pelo indice especifico da lista
# remove - remove um objeto especificado da lista
# pop - remove o ultimo objeto da lista
# insert - adiciona um obejto no inicio da lista
'''
lista = []
print(lista, type(lista))
print(len(lista))
lista = ['front']
print(lista, type(lista))
print(len(lista))
lista = ['back']
print(lista, type(lista))
print(len(lista))
lista.append('front')
print(lista, type(lista))
print(len(lista))
lista.append('data')
print(lista, type(lista))
print(len(lista)) '''
#           0        1      2    3    4
# REVERSE  -5       -4    -3   -2    -1
lista = [ 'back', 'tarde', 21, True, 8.8 ]
print(f' a quantidade de alunas na turma é: {lista[2]}')
lista[2] = 22
print(lista)
lista[1] = False
print(lista)
lista[1] = ['Neyva', 'Alice', 'Lara', 'Paula', 'Geisa']
print(lista[1][2])

print(lista)
del lista[-2]
print(lista)
del lista[-2]
print(lista)
del lista[-2]
print(lista)
lista.remove('back')
lista.append(26)
lista.append(57)
lista.append(900)
print(lista)
valor_do_pop = lista.pop()
print(lista)
print(f' foi removido da lista o cliente de id : {valor_do_pop}')
lista.insert(0, 'Amontada Valley')
print(lista)
lista.insert(2, 'Professor')
print(lista)
lista.insert(200, 'Aluna')
print(lista)
