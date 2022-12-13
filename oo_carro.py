class Carro():
    def __init__(self, modelo, cor, consumo):
        self.modelo = modelo
        self.cor = cor
        self.consumo = consumo
        self.litros_tanque = 0
    
    def pintar(self):
        pass

    def mostrar_cor(self):
        pass

    def verifica_tanque(self, valor):
        capacidade_tanque = 50
        if ((self.litros_tanque + valor) <= capacidade_tanque):
            return valor
        else:
            return (capacidade_tanque - self.litros_tanque)
        
    def abastecer(self, litros):
        abastecer = self.verifica_tanque(litros)
        self.litros_tanque += abastecer
        print("Seu tanque foi abastecido com {} litros de combustível e tem {} litros".format(abastecer, self.litros_tanque))

    def pode_andar(self, km):
        consumo = (km / self.consumo)
        return (self.litros_tanque >= consumo)

    def andar(self, km):
        if (self.pode_andar(km)):
            self.litros_tanque -= (km / self.consumo)
        else:
            print(f'Combustível insuficiente para andar {km}Km')

    def mostrar_tanque(self):
        print(f'"Restam {self.litros_tanque} litros no tanque de combustível')

Palio = Carro("ESX", "preta", 12)
Palio.abastecer(5)
Palio.andar(70)
