def intervalo(lista_de_palavras, frase):
    for i in lista_de_palavras:
        x = frase.find(i)
        fim = x + (len(i) -1)
        print(f'O intervalor de { i } vai de { x } até { fim }')
        
lista_de_palavras = []

for i in range(3):
    palavra = input(f"Informe a { i+1 }ª palavra: ")
    lista_de_palavras.append(palavra)


frase = input('informe a frase: ')

intervalo(lista_de_palavras, frase)
