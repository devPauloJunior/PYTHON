class Pet_Shop():
    def __init__(self, nome_do_animal, idade):
        print(nome_do_animal, 'tem a cor branca e tem ', idade, ' meses')

class Gatos(Pet_Shop):
    def __init__(self):
        print('O seu gato se Chama Milu e tem 4 meses.')
        super().__init__('Milu', 0.4)
    
objeto = Gatos()