import os

try:
    arq = open("valida.txt", "w", encoding="utf8")
    arq.write("Não é um teste de escrita")
finally:
    arq.close()


with open("valida2.txt", "w", encoding="utf8") as meu_arquivo:
    meu_arquivo.write("Novo teste de Não É o Python")

with open("valida2.txt", "r", encoding="utf8") as meu_arquivo:
    print(meu_arquivo.read())

#os.rename("valida2.txt", "alterado.txt")
#os.remove("valida.txt")

lista = os.listdir()
print(len(lista))
print(lista[10])