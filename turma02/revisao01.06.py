#SUPERCLASSE FUNCIONAROS_POUSADA
class  FuncionariosPousada:
    def __init__(self, nome, cpf, matricula, horario_entrada, horario_saida, contato, data_nascimento, estado_civil, sexo):
        self.nome = nome
        self._cpf = cpf
        self._matricula = matricula
        self._horario_entrada = horario_entrada
        self._horario_saida  = horario_saida
        self.contato = contato
        self.data_nascimento = data_nascimento
        self.estado_civil = estado_civil
        self.sexo = sexo
        self._bonus = 0.0
    #METODOS, SETs e GETs
    @property
    def cpf(self):
        return self._cpf
    @property
    def matricula(self):
        return self._matricula
    @matricula.setter
    def matricula(self, nova_matricula):
        self._matricula = nova_matricula
    @property
    def horario_entrada(self):
        return self._horario_entrada
    @horario_entrada.setter
    def horario_entrada(self, nova_horario_entrada):
        self._horario_entrada = nova_horario_entrada
    @property
    def horario_saida(self):
        return self._horario_saida
    @horario_saida.setter
    def horario_saida(self, nova_horario_saida):
        self._horario_saida = nova_horario_saida
    @property
    def salario(self):
        return self._salario
    @property
    def bonificacao(self):
        return self._bonificacao
    @property
    def bonus(self):
        return self._bonus
    @bonus.setter
    def bonus(self, vendas):
        self._bonus = self._bonificacao * vendas
#CLASSE GERENTE
class Gerente(FuncionariosPousada):
    def __init__(self, nome, cpf, matricula, horario_entrada, horario_saida, contato, data_nascimento, estado_civil, sexo, automovel):
        super().__init__(nome, cpf, matricula, horario_entrada, horario_saida, contato, data_nascimento, estado_civil, sexo)
        self._salario = 3000.00
        self._bonificacao = 0.2
        self.automovel = automovel
    
#CLASSE ATENDENTE
class Atendente(FuncionariosPousada):
    def __init__(self, nome, cpf, matricula, horario_entrada, horario_saida, contato, data_nascimento, estado_civil, sexo):
        super().__init__(nome, cpf, matricula, horario_entrada, horario_saida, contato, data_nascimento, estado_civil, sexo)
        self._salario = 1200.00
        self._bonificacao = 0.1
   
#ESTRUTURADO
atendente01 = Atendente("Angelica", 12345676532, 343536, "08:00", "18:00", 8899696969, "05/05/1995", "solteira", "F")
atendente02 = Atendente("Marcos", 12345676999, 343537, "14:00", "22:00", 88996535352, "01/09/1999", "casado", "M")
gerente01 = Gerente("Bill Gates", 12345675555, 141517, "08:00", "22:00", 88996537755, "11/12/1980", "divorciado", "M", True)

print(atendente01.nome)
print(atendente01.matricula)
print(atendente01.horario_entrada)
print(atendente01.horario_saida)
print("-----------------------")
print(atendente02.nome)
print(atendente02.matricula)
print("=======================")
print(gerente01.nome)
print(gerente01.matricula)
print(gerente01.automovel)
print("=======================")
atendente01.horario_entrada = "07:00"
print(atendente01.horario_entrada)
