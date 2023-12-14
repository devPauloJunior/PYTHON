class Automovel:
    def __init__(self, placa, cor):
        self.__placa = placa
        self.__cor = cor

    def get_placa(self):
        return self.__placa
    
    def get_cor(self):
        return self.__cor

    def set_cor(self, nova_cor):
        self.__cor = nova_cor

    def dirigir(self, velocida):
        print(f'Estou dirigindo a { velocida }km/h.')

#Instancias
carro = Automovel('TYT-0019', 'azul')
moto = Automovel('GJG-1716', 'preta')
caminhao = Automovel('AAP-1122', 'amarelo') 

# Chamadas GET
print(f'A cor do carro é { carro.get_cor()} ')
print(f'A cor da moto é { moto.get_cor()} ')
print(f'A cor do caminhão é { caminhao.get_cor()} ')

print(f'A placa do carro é { carro.get_placa()} ')
print(f'A placa da moto é { moto.get_placa()} ')
print(f'A placa do caminhão é { caminhao.get_placa()} ')

# Chamadas SET
carro.set_cor('branco')
moto.set_cor('azul')
caminhao.set_cor('preto')

carro.__cor = 'verde'


# Novas chamadas GET
print(f'A nova cor do carro é { carro.get_cor()} ')
print(f'A nova cor da moto é { moto.get_cor()} ')
print(f'A nova cor do caminhão é { caminhao.get_cor()} ')