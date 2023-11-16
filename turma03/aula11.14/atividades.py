lista_consoantes = []
letra_1 = input("Digite uma letra: ")
letra_2 = input("Digite uma letra: ")

if letra_1 != 'a' and letra_1 != 'e' and letra_1 != 'i' and letra_1 != 'o' and letra_1 != 'u':
    print("É uma consoante")
    lista_consoantes.append(letra_1)

if letra_2 != 'a' and letra_2 != 'e' and letra_2 != 'i' and letra_2 != 'o' and letra_2 != 'u':
    print("É uma consoante")
    lista_consoantes.append(letra_2)

print(lista_consoantes)
