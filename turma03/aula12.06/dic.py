# CRUD - Created, Readed, Updated e Deleted
dic = { 'nome': 'Paulo' } # Created
dic2 = dict(idade=23) # Created
dic['nome'] # Readed
reading = dic2.get('idade') # Readed

dic.update(sobrenome='Junior') #Updated
dic.update({ 'idade': 23 }) #Updated
tupla = ('peso', 72.12), #Updated
lista = ['data', '13/04/1996'],['numeros', [1, 2, 3, 4, 5, 6, 7, 8, 9]] #Updated
dic.update(tupla)
dic.update(lista)
print(dic)
print(dic2)

dic.clear() # Deleted

print(f'Dados do dicionario: { dic }')