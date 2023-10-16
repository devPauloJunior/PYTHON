class Veiculo:
    def teste(self):
        return f'Veiculo'

class Moto(Veiculo):
    def __str__(self):
        super().teste()
        return f'Moto'

class Carro(Veiculo):
    def __str__(self):
        super().teste()
        return f'Carro'
moto01 = Moto()
carro01 = Carro()
meus_veiculos = [moto01, carro01]
for car in meus_veiculos:
    car.__str__()


