# dunder metodo => __metodo__
class Estudante:
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula
        self.nome_classe = self.__class__.__name__
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    cpf = property(get_cpf, set_cpf)

class EstudanteGraduacao(Estudante):
    def __init__(self, curso, nome, matricula):
        self.curso = curso
        super().__init__(nome, matricula)
        
    
    def __str__(self):
        return f'A sua classe é { self.nome_classe }. Olá, { self._nome } seu CPF é: { self.get_cpf() } seu curso de Graduação é o de { self.curso } e sua matricula de acesso é { self._matricula }'

class EstudantePos(Estudante):
    nivel = 1
    orientador = 'Prof Carlos Alberto'

    def __str__(self):
        return f'A sua classe é { self.nome_classe }.Olá, { self._nome } seu nivel é { self.nivel }° e seu Tutor será o { self.orientador }. para seu acesso utilize a matricula { self._matricula }'

aluno1 = EstudanteGraduacao('ADS', 'Paulo Junior', 353637)
# aluno2 = EstudantePos('Paulo Junior', '565758')


aluno1.set_cpf(123456789)
print(aluno1.get_cpf())
print(aluno1)
# print(aluno2)
