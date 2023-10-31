## criar um arquivo chamado notas.txt em sua pasta python, contendo o seguinte conteudo:
## nome:nota
## criar um codigo que leia o arquivo e mostre em tela a relação de aliunos e suas notas ordenados pela maior nota.

## esta função foi criada para ser utilizada com o parametro KEY do SORTED. pois o parametro KEY só aceita ITERAVEIS
def segundo_item(item):
    return item[1]
## essas duas listas foram criadas para complementar a ordenação
nova_lista = []
altera_tipo = []
## with é a manipulação de arquivos em alto nivel
with open("notas.txt", "r", encoding="utf8") as notas:
## aogra vamos ler todas as linhas do arquivo
    lista_notas = notas.readlines()
## o FOR é a implementação da ordenação
    for linha in lista_notas:
## retiramos o \n e cortamos a linha gerando uma lista de dois indices
        nova_linha = linha.replace('\n', '').split(':')
## temos que alterar o tipo de dado do segundo indice para INT
        altera_tipo = (nova_linha[0] , int(nova_linha[1]))
## apendamos a nova linha na nova lista
        nova_lista.append(altera_tipo)
## mostra as notas ordenadas utilizando uma função no KEY e REVERSE True
    print(sorted(nova_lista, key=segundo_item, reverse=True))