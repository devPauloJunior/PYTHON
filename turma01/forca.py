import random

def jogar():

    mensagem_abertura()    



    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta ]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(len(palavra_secreta)-erros))

        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim de Jogo!")

def mensagem_abertura():
    print("*"*30)
    print("Bem vindo ao jogo da Forca!")
    print("*"*30)

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

if (__name__ == "__main__"):
    jogar()