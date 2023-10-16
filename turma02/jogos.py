import forca
import adivinhacao
def escolha_seu_jogo():
    print("*"*30)
    print("*"*6,"Escolha seu jogo", "*"*6)
    print("*"*30)

    print("(1) Forca ou (2) Advinhação!")
    jogo = int(input("Qual jogo? "))

    if (jogo ==1):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Advinhação")
        adivinhacao.jogar()

if (__name == "__main__"):
    escolha_seu_jogo()