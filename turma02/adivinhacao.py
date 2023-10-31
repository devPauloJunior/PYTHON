import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil ", numero_secreto)

    while(True):
        nivel = int(input("Defina o nível: "))
        if(nivel == 1):
            total_de_tentativas = 20
            break
        elif(nivel == 2):
            total_de_tentativas = 10
            break
        elif(nivel == 3):
            total_de_tentativas = 5
            break
        print("Seu numero foi invalido. Tente outra vez!")

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        while(True):
            chute = int(input("Digite um número entre 1 e 100: "))
            if (chute > 0 and chute < 101):
                print("Você digitou " , chute)
                break
            print("Você deve digitar um número entre 1 e 100!")

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
