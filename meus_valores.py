valor = open('valores.txt', 'r')
pag_valor = open('pagamento.txt', 'w')

for linha in valor:
    nome = input("Digite um nome: ")
    pag_valor.write(nome + ":" + linha)

valor.close()
pag_valor.close()

pag_valor = open("pagamento.txt", 'r')
for linha in pag_valor:
    print(linha)
