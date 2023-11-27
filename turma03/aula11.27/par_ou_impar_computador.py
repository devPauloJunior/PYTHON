from random import randint
placar_jogador = 0
placar_computador = 0
while True:
        jogador = input('Escolha par ou impar: ').lower()
        numero_jogador = int(input('Escolha seu numero: '))
        numero_computador = randint(0, 10)
        resultado = numero_jogador + numero_computador
        if resultado % 2 == 0:
            if jogador == 'par':
                placar_jogador += 1
                print(f'Você ganhou e o computador colocou o  numero { numero_computador }!')
            else:
                placar_computador += 1
                print(f'O computador ganhou com o numero { numero_computador }.')
        else:
            if jogador == 'impar':
                placar_jogador += 1
                print(f'Você ganhou e o computador colocou o  numero { numero_computador }!')
            else:
                placar_computador +=1
                print(f'O computador ganhou com o numero { numero_computador }.')
        print(f'O placar atual é jogador: { placar_jogador } computador: { placar_computador }')
        saida = input('Digite "s" para sair: ').lower()
        if saida == 's':
             if placar_computador > placar_jogador:
                  confirma_saida = input('Você está perdendo. Tem certeza que vai sair? Frango!!! digite "cocoo" para sair. ').lower()
                  if confirma_saida == 'cocoo':
                       break
                  else:
                       continue
             print('Volte sempre!')
             break