from time import sleep
#Crie uma classe que modele um Tamagushi(Bichinho Eletrônico)
class BichinhoVirtual:
    # Nome, Energia, Sede, Saúde, Experiência, Humor e Idade
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100
        self.sede = 0
        self.saude = 100
        self.exp = 0
        self.humor = 100
        self.idade = 0

    def sono(self):
        if self.energia < 20 or self.saude < 30:
            print("E dormiu....")
            time.sleep(10)            
            self.energia += 40

    def brincar():
        print("Brincou")
    def crescer():
        print("cresceu")
    def hidratar():
        print("hidratou")
    def medicar():
        print("medicou")
    def alimentar():
        print("comeu")
    def morrer():
        print("morreu")

if __name__ == "__main__":
    tamagoshi = BichinhoVirtual("Tomate")
    print(tamagoshi.nome)
    