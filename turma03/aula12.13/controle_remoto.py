class ControleRemoto:
    def __init__(self, cor, marca, qtd_pilhas):
        self.botao = None
        self.cor = cor
        self.marca = marca
        self.qtd_pilhas = qtd_pilhas
        self.painel = False
        self.temperatura = 0

    # METODOS
    def ligar(self):
        self.painel = True

    def desligar(self):
        self.painel = False 

    def set_temperatura(self, nova_temperatura):
        if self.painel == False:
            print('Temperatura não pode ser alterada.Ar Desligado')
        else:
            self.temperatura = nova_temperatura
    
    def get_temperatura(self):
        return self.temperatura
    
    def precionar_botao(self, tipo_de_botao):
        self.botao = tipo_de_botao
        if self.botao == 'Ligar' and self.temperatura == 0:
            print('Ar está ligado')
            self.ligar()
        elif self.botao == 'Desligar':
            print('Ar está desligado')
            self.set_temperatura(0)
            self.desligar()

controle = ControleRemoto('branca', 'elgin', 2)

controle.precionar_botao('Ligar')

controle.set_temperatura(20)

print(controle.get_temperatura())

controle.precionar_botao('Desligar')

controle.set_temperatura(20)

print(controle.get_temperatura())