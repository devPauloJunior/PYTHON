#faça um codigo que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e pedindo as informações novamente.

tentativas = 1
while tentativas <= 3:
    usuario = input('Informe seu usuário: ')
    senha = input('Informe sua senha: ')
    if senha == usuario:
        print(f'ERROR: essa foi sua tentativa numero { tentativas }')
        if tentativas == 3:
            print(f'Suas tentativas acabram. Tente amanhã')
            break
    else:
        print('Acesso liberado')
        break
    tentativas += 1
