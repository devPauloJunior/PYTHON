#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Na classe BombaCombustivel abaixo sabemos que é uma bomba de gasolina e:
# atributos: valor_do_litro e quantidade_de_combustivel
# todos atributos encapsulados fortemente
# métodos abaixo:
# abastecer_a_bomba - esse método abastece a bomba para iniciar a venda
# abastecer_veiculo_valor – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
# abastecer_veiculo_litro – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente
# alterar_valor – altera o valor do litro do combustível
# alterar_quantidade_combustivel – altera a quantidade combustível restante na bomba
# OBS: Lembre-se de fazer os GETs e SETs
# OBS: Não esqueça das validações
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
# OBS: Faça a impressão dos elementos

class BombaCombustivel:
    def __init__(self, valor_do_litro):
        self.__valor_do_litro = valor_do_litro
        self.__quantidade_de_combustivel = 0.0

    @property
    def valor_do_litro(self):
        return self.__valor_do_litro

    @property
    def quantidade_de_combustivel(self):
        return self.__quantidade_de_combustivel

    @valor_do_litro.setter
    def valor_do_litro(self, novo_valor):
        if type(novo_valor) == type(float()):
            self.__valor_do_litro = novo_valor
        else:
            print("Preço deve ser do tipo float!")
    
    @quantidade_de_combustivel.setter
    def quantidade_de_combustivel(self, nova_quantidade):
        if type(nova_quantidade) == type(float()):
            self.__quantidade_de_combustivel = nova_quantidade
        else:
            print("Quantidade de combustivel deve ser um numro inteiro!")
    
    def abastecer_bomba(self, quantidade_litros):
        calcula_quantidade = self.__quantidade_de_combustivel + quantidade_litros
        if  calcula_quantidade < 1000.00:
            print(f'Foi abastecido {quantidade_litros:.2f}L na bomba')
            self.quantidade_de_combustivel += quantidade_litros
        else:
            print(f'Impossivel abastecer {quantidade_litros:.2f} litros')

    def abastecer_veiculo(self, valor = 0.00, litros = 0.00):
        if self.quantidade_de_combustivel != 0.00:
            if valor != 0.00:
                abastecer_veiculo_valor = valor/self.valor_do_litro
                self.quantidade_de_combustivel -= abastecer_veiculo_valor
                print(f'Você pagou R${valor:.2f} e seu abastecimento é de {abastecer_veiculo_valor:.2f}L. A bomba atualizada tem {self.quantidade_de_combustivel:.2f}L')
            elif litros != 0:
                abastecer_veiculo_litro = litros * self.valor_do_litro
                self.quantidade_de_combustivel -= litros
                print(f'Você solicitou {litros:.2f}L e vai pagar R${abastecer_veiculo_litro:.2f} pelo seu abastecimento. A bomba atualizada tem {self.quantidade_de_combustivel:.2f}L')
            else:
                print("Verifique as informações, não conseguimos processar sua solicitação.")
        else:
            print(f'Impossivel abastercer. A bomba está com {self.quantidade_de_combustivel:.2f} litros, favor abastercer a bomba.')
    
    def __str__(self):
        return f'Na bomba tem {self.quantidade_de_combustivel:.2f} litros e o valor do litro de gasolina é R${self.valor_do_litro:.2f}.'

posto01 = BombaCombustivel(5.00)
print("*"*20)
print(posto01)
posto01.abastecer_veiculo(valor = 50.00)
print("*"*20)
posto01.abastecer_bomba(300.0)
print("*"*20)
print(posto01)
print("*"*20)
posto01.abastecer_veiculo(valor = 20.00)
print("*"*20)
posto01.abastecer_bomba(400.0)
print("*"*20)
print(posto01)
posto01.abastecer_bomba(300.0)
print("*"*20)
posto01.abastecer_veiculo(valor = 32.00)
print("*"*20)
print(posto01)
posto01.abastecer_bomba(300.0)
print("*"*20)
print(posto01)
print("*"*20)
posto01.abastecer_veiculo(litros = 10.00)
print("*"*20)
print(posto01)