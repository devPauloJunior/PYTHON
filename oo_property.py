class Felino():
    def __init__(self, idade, juba):
        self.__idade = 0
        self.juba = juba

    def imprimir(self):
        print("Meu nome é: ", self.nome)
        print("Minha idade é: ", self.idade)
        if self.juba == False:
            print("Eu não tenho juba!")
        else:
            print("Eu tenho juba!!!")
        if self.fome >= 50:
            print("Estou com pouca fome")
        else:
            print("Estou com fome!!!")

    def get_nome(self):
        print("Entrou no metodo GETTER")
        return self.__nome

    def set_nome(self, novo_nome):
        print("Entrou no metodo SETTER")
        if type(novo_nome) == type(str()):
            self.__nome = novo_nome
        else:
            print("Nome deve ser uma STRING!")

    def get_fome(self):
        print("Entrou no metodo GETTER!")
        return self._fome
    
    def set_fome(self, comida):
        print("Entrou no metodo SETTER!")
        if type(comida) == type(int()):
            self._fome = comida
        else:
            print("Comida deve ser um numero inteiro")

    @property
    def idade(self):
        print("Entrou no metodo GETTER!")
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        print("Entrou no metodo SETTER!")
        if type(nova_idade) == type(int()):
            self.__idade = nova_idade
        else:
            print("Idade deve ser um numero inteiro")

    # nome = property(get_nome, set_nome)
    fome = property(get_fome, set_fome)
    nome = property()
    nome = nome.getter(get_nome)
    nome = nome.setter(set_nome)