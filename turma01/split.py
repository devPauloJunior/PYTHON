texto = 'O meu fim evidente era atar as duas pontas da vida, e restaurar na velhice a adolescência. Pois, senhor, não consegui recompor o que foi nem o que fui. Em tudo, se o rosto é igual, a fisionomia é diferente. Se só me faltassem os outros, vá; um homem consola-se mais ou menos das pessoas que perde; mas falto eu mesmo, e esta lacuna é tudo. O que aqui está é, mal comparando, semelhante à pintura que se põe na barba e nos cabelos, e que apenas conserva o hábito externo, como se diz nas autópsias; o interno não aguenta tinta. Uma certidão que me desse vinte anos de idade poderia enganar os estranhos, como todos os documentos falsos, mas não a mim. Os amigos que me restam são de data recente; todos os antigos foram estudar a geologia dos campos-santos. Quanto às amigas, algumas datam de quinze anos, outras de menos, e quase todas crêem na mocidade. Duas ou três fariam crer nela aos outros, mas a língua que falam obriga muita vez a consultar os dicionários, e tal frequência é cansativa.'

palavras = texto.split()
print(palavras)

for palavra in palavras:
    if ',' in palavra:
        print(palavra[:-1])
    else:
        print(palavra)