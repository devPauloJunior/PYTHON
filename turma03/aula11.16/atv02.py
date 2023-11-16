# com meus_numeros = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# imprima na tela os multiplos de 3 em uma lista chamada multiplos_ok
# remova de meus_numeros os multiplos de 5   

meus_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

multiplos_ok = []
multiplos_ok = meus_numeros[0::3]
multiplos_ok.remove(0)
print(multiplos_ok)

meus_numeros.remove(5)
meus_numeros.remove(10)
meus_numeros.remove(15)
meus_numeros.remove(20)

print(meus_numeros)