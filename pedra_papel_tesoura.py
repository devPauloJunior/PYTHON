#IMPORTAR OS MODULOS 
from random import randint
from time import sleep

#ITENS UTILIZADOS
itens = ("Pedra", "Papel", "Tesoura")

#PERGUNTA DO JOGADOR
jogador = int(input('''Escolha uma opcao para se jogar: 

[0] Pedra
[1] Papel
[2] Tesoura
 
Digite sua escolha: '''))
#CONTAGEM JO KEN PÔ
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
#NUMERO RANDOMICO DO COMPUTADOR
computador = randint(0,2)
#VALIDAR OPCAO ESCOLHIDA
if jogador < 0 or jogador > 2:
    print("Sua opção é invalida, FIM DE JOGO!")
else:
    #COMPARACOES DO JOGO
    print("Computador Jogou: {}".format(itens[computador]))
    print("Você Jogou: {}".format(itens[jogador]))
    if computador == 0:
        if jogador == 0:
            print("Empate!")
        elif jogador == 1:
            print("Jogador perdeu")
        elif jogador == 2:
            print("Computador venceu")
        else:
            print("Operacao invalida")
    elif computador == 1:
        if jogador == 0:
            print("Computador perdeu")
        elif jogador == 1:
            print("Empate!")
        elif jogador == 2:
            print("Jogador venceu")
        else:
            print("Operacao invalida")
    elif computador == 2:
        if jogador == 0:
            print("Jogador venceu")
        elif jogador == 1:
            print("Computador venceu")
        elif jogador == 2:
            print("Empate!")
        else:
            print("Operacao invalida")
    else:
        print("Operacao invalida")