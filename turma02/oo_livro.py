# Crie uma classe Livro que possui os atributos nome, qtdPaginas, autor e preço(encapsulado).
# Crie o método getPreco para obter o valor do preço
# Crie o método setPreco para setar um novo valor do preço

class Livro():
    def __init__(self, nome, quantidade_de_paginas, autor):
        self.nome = nome
        self.quantidade_de_paginas = quantidade_de_paginas
        self.autor = autor

    def get_preco(self):
        return self.__preco
    
    def set_preco(self, novo_preco):
        if type(novo_preco) == type(float()):
            self.__preco = novo_preco
        else:
            print("Proço deve ser do tipo float")

    def __str__(self):
        return f' O {self.__class__.__name__} {self.nome} do autor {self.autor} tem {self.quantidade_de_paginas} páginas e custa R${self.get_preco()} '

    preco = property(get_preco, set_preco)

Gibi = Livro("Turma da Monica", 22, "Mauricio de Sousa")
print("="*20)
Gibi.set_preco(7.50)
print(Gibi.get_preco())
print("="*20)
print(Gibi)
print("="*20)