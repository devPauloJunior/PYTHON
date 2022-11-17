class Felino():
    cor_do_pelo = ''
    juba = False

    def imprimir(self):
        print("Meu nome é: ", self.nome)
        print("Meu pelo é: ", self.cor_do_pelo)
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

    nome = property(get_nome, set_nome)
    fome = property(get_fome, set_fome)