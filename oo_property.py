# class Animal():
#     def __init__(self, nome, peso):
#         self._nome = nome
#         self.peso = peso

#     def imprimir(self):
#         print("Meu nome é ", self._nome)
#         print("Meu peso é: ", self.peso)    
    
#     def alimentar(self, comida):
#         self.peso += comida

#     @property
#     def nome(self):
#         print("metodo getter foi chamado")
#         return self._nome

#     @nome.setter
#     def nome(self, new_name):
#         print("metodo setter foi chamado")
#         if type(new_name)==type(str()):
#             self._nome = new_name
#         else:
#             print("Nome deve ser uma string")


class Felino():
    def __init__(self, cor_do_pelo, juba):
        self.cor_do_pelo = cor_do_pelo
        self.juba = False
        self.fome = 0

    def imprimir(self):
        print("Meu nome é: ", self._nome)
        print("")
        if self.fome >= 50:
            print("Minha fome está pouca: ", self.fome)
        else:
            print("Muita fome me alimente: ", self.fome)

        print("Meu pelo tem a cor: ", self.cor_do_pelo)
    
    def alimentar(self, quantidade_de_comida):
        self.fome += quantidade_de_comida

    def get_nome(self):
        print("metodo getter foi chamado")
        return self._nome

    def set_nome(self, new_name):
        print("metodo setter foi chamado")
        if type(new_name)==type(str()):
            self._nome = new_name
        else:
            print("Nome deve ser uma string")

    nome = property(get_nome, set_nome)