# crie abstração para uma super classe funcionario com duas subclasses. Imprima todos do dados.

class Funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = 0.0
    
    def get_nome(self):
        return self.nome 
    
    def get_salario(self):
        return self.salario
    
    
    
class Gerente(Funcionarios):
    pass

class Desenvolvedor(Funcionarios):
    pass




