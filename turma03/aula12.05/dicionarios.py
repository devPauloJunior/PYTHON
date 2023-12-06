# possuem CHAVE(KEYS) e VALOR(VALUES)
# parametro: {} ou dict()
# 

pessoa = {  'nome': 'Paulo',
            'sobrenome': 'Junior 2',
            'nome 2': 'Rodrigo',
            'sobrenome': 'Junior 1',
            'sobrenome 4': 'Junior',
             'idade': 23 }

print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())

k = pessoa.keys()
v = pessoa.values()

for chave in k:
    print(chave)

print("="*20)

for valor in v:
    print(valor)

print("="*20)

for chave in pessoa:
    print(chave)

print("="*20)

for valor in pessoa.values():
    print(valor)

print("="*20)

for chave, valor in pessoa.items():
    print(chave, valor)

print("="*20)

i = pessoa.items()
print(i)

print("="*20)

print(pessoa['sobrenome 4'])
print(pessoa['sobrenome'])
print(pessoa['idade'])

print("="*20)


d1 = { 'valor1': 100,
       'valor2': 200,
       'valor3': 300, }

d2 = d1.copy()

print(d1)

d2['valor2'] = 'Jefferson'

print(d1)

print(d2)

print(d2.get('valor2'))

d3 = d1.pop('valor3')

print(d1)

outro_nome = {'valor5': 5,
              'valor6': 6  }

d1.update(outro_nome)

print(d1)

print(d1.has_key("valor5"))

