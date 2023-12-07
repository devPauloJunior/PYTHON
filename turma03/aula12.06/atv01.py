# 1. Crie uma lista de alunos com nome e nota final de cada aluno e coloque em um dicionario, depois imprima.
# lista_de_alunos = [['paulo', 5], ['joao', 7], ['rodrigo', 9]]
# dic = {}
# dic.update(lista_de_alunos)
# print(dic)

# 2. Ainda sobre a questão 1. Inserir mais 04 alunos e notas no seu dicionario.

# 3. faça um codigo que pede a marca e o modelo do carro do cliente insere ele em uma lista e depois transforma em um dicionario. Imprima os dois resultados.

# lista_de_carros = []
# marca = input('informe o MARCA do seu carro: ')
# modelo = input('informe o MODELO do seu carro: ')
# lista_de_carros.append(marca)
# lista_de_carros.append(modelo)

# lista_de_frutas = 'maçã', 4.50
# print(type(lista_de_frutas))

# dic_carros = {}
# dic_carros.update([lista_de_carros])

# print(lista_de_carros)
# print(dic_carros)

# dic_carros['Fiat'] = 'Uno'

# print(dic_carros)

# 4. crie um cadastro de clientes recebendo nome, idade, data de aniversario e endereço completo(rua, numero da residencia e bairro). Adicione todas as informações em um dicionario. Imprima ao final.

# 5. vamos criar um sistema de login e senha. crie um dicionario contendo os acessos dos colaboradores com nome de usuario e senha. em seguida peça as informações e valide o login do usuario.

# dic_acessos = { 
#     'paulo': '123456', 
#     'joao': '121212' 
# }
# usuario_senha = {}
# usuario = input('Informe seu USUARIO: ')
# senha = input('Informe sua SENHA: ')
# usuario_senha[usuario] = senha

# for chave in dic_acessos.keys():
#     if chave == usuario:
#         if dic_acessos[chave] == senha:
#             print("Acesso liberado!")
#             break
#         else:
#             print(f'Senha incorreta para o usuario { usuario }')
#             break
# else:
#     print('usuario')

# MATRIZES EM PYTHON
# matriz = {'inicio': 'Paulo',
#           'meio': [4, 5, 6],
#           'fim': [7, 8, 9],
# }
# print(matriz['inicio'])

# 6. faça um quiz utilizando um dicionario com as seguintes chaves: Perguta, opções e resposta. Faça a validação da opção escolhida com a respota e imprima.

perguntas =[
    {'Pergunta': 'Quanto é 5 x 5?',
     'Opções': [12, 16, 20, 25],
     'Resposta': 25,},

    {'Pergunta': 'Quanto é 12 / 4?',
     'Opções': [6, 13, 3, 2],
     'Resposta': 3,},

    {'Pergunta': 'Quanto é 15 + 15?',
     'Opções': [14, 15, 30, 25],
     'Resposta': 30,},
]
qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i+1})', opcao)
    print()

    escolha = int(input('Escolha sua opção: '))
    acertou = False

    if escolha == int(pergunta['Resposta']):
        acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou 😔')

    print()

print(f'Você acertou { qtd_acertos } de { len(perguntas) }')