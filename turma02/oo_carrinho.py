class Carro():
    def __init__(self, modelo, cor, consumo):
        self.modelo = modelo
        self.cor = cor
        self.consumo = consumo
        self.tanque_litros = 0

    def pintar(self):
        sua_cor = int(input("Escolha: [1]PRATA, [2]PRETO, [3]BRANCO: "))
        if sua_cor != 1 and sua_cor != 2 and sua_cor != 3:
            print("Cor invalida na loja!")
        else:
            lista_de_cor = [0, "Prata", "Preto", "Branco"]
            self.cor = lista_de_cor[sua_cor]

    def pintado(self):
        return f'A cor do seu carro é {self.cor}'

    def verificar_tanque(self, litros):
        capacidade_tanque = 40
        if ((self.tanque_litros + litros) <= capacidade_tanque):
            return litros
        else:
            return (capacidade_tanque - self.tanque_litros)

    def abastecer(self, litros):
        abastecer = self.verificar_tanque(litros)
        self.tanque_litros += abastecer
        print(f'Seu tanque foi abastecido com {litros} litros de combustivel e tem {self.tanque_litros} litros.')

    def pode_andar(self, distancia):
        consumo = (distancia/self.consumo)
        return (self.tanque_litros >= consumo)
    
    def andar(self, distancia):
        if (self.pode_andar(distancia)):
            self.tanque_litros -= (distancia/self.consumo)
        else:
            print(f'Combustivel insuficiente para andar {distancia}Km!')

    def mostrar_tanque(self):
        print(f'Restam {self.tanque_litros:,.2f} litros de combustivel no tanque!')



Palio = Carro("ESX", "Branca", 12)
Palio.pintar()
print("="*20)
print(Palio.pintado())
print("="*20)
Palio.abastecer(8)
print("="*20)
Palio.andar(160)
print("="*20)
Palio.mostrar_tanque()
print("="*20)
Palio.abastecer(10)
print("="*20)
Palio.andar(160)
print("="*20)
Palio.mostrar_tanque()