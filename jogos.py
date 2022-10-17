import forca
import adivinhacao

print("*"*30)
print("*"*6,"Escolha seu jogo", "*"*6)
print("*"*30)

print("(1) Forca ou (2) Advinhação!")
jogo = int(input("Qual jogo? "))

if (jogo ==1):
    print("Jogando Forca")
elif (jogo == 2):
    print("Jogando Advinhação")