#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Crie uma super classe RelogioDePonto, uma subclasse Funcionarios e uma sub-subclasse Operador e Repositor:
# trabalhe com os atributos: hora_entrada, hora_saida, nome, matricula, expediente, ocorrencia 
# todos atributos encapsulados OK
# defina uma correta dsitribuição dos atributos entre as classes
# defina as nomenclaturas dos metodos e com base na explicação abaixo faça:
# você deve fazer os funcionários registrem a entrada e a saida com base no seu expediente
# você informar caso ele entre atrasado ou saia adiantado e mostrar quanto foi esse atraso ou adiantamento
# caso o atraso e adiantamento seja maior que 10 minutos registre uma ocorrencia
# OBS: Lembre-se de fazer os GETs e SETs
# OBS: Não esqueça das validações
# OBS: Faça a impressão dos elementos corretamente

class RelogioDePonto():
    def converte(self, horas):
        minutos = horas * 60
        return minutos

    def get_hora_entrada(self):
        return self.__hora_entrada

    def set_hora_entrada(self, entrada):
        if int(entrada[0:2]) >= 0 and int(entrada[0:2]) < 24 and int(entrada[3:5]) >= 0 and int(entrada[3:5]) < 60:
            converte_hora = self.converte(int(entrada[0:2]))
            minutos = converte_hora + int(entrada[3:5])
            self.__hora_entrada = minutos
        else:
            print("Verifique sua batida de ENTRADA!!!")

    def get_hora_saida(self):
        return self.__hora_saida

    def set_hora_saida(self, saida):
        if int(saida[0:2]) >= 0 and int(saida[0:2]) < 24 and int(saida[3:5]) >= 0 and int(saida[3:5]) < 60:
            converte_hora = self.converte(int(saida[0:2]))
            minutos = converte_hora + int(saida[3:5])
            self.__hora_saida = minutos
        else:
            print("Verifique sua batida de SAIDA!!!")

    hora_entrada = property(get_hora_entrada, set_hora_entrada)
    hora_saida = property(get_hora_saida, set_hora_saida)

    def __str__(self):
        return f'Você entrou às {self.hora_entrada} e saiu às {self.hora_saida}!'

class Funcionarios(RelogioDePonto):
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__ocorrencia  = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self):
        print("Impossivel alterar. Fale com o ADM!")

    @property
    def ocorrencia(self):
        return self.__ocorrencia
    
    @ocorrencia.setter
    def ocorrencia(self, nova_ocorrencia):
        self.__ocorrencia = nova_ocorrencia

    def get_expediente_entrada(self):
        return self.__expediente_entrada

    def set_expediente_entrada(self, ex_entrada):
        if int(ex_entrada[0:2]) >= 0 and int(ex_entrada[0:2]) < 24 and int(ex_entrada[3:5]) >= 0 and int(ex_entrada[3:5]) < 60:
            converte_hora = self.converte(int(ex_entrada[0:2]))
            minutos = converte_hora + int(ex_entrada[3:5])
            self.__expediente_entrada = minutos
        else:
            print("Verifique sua hora de expediente de ENTRADA!!!")

    def get_expediente_saida(self):
        return self.__expediente_saida

    def set_expediente_saida(self, ex_saida):
        if int(ex_saida[0:2]) >= 0 and int(ex_saida[0:2]) < 24 and int(ex_saida[3:5]) >= 0 and int(ex_saida[3:5]) < 60:
            converte_hora = self.converte(int(ex_saida[0:2]))
            minutos = converte_hora + int(ex_saida[3:5])
            self.__expediente_saida = minutos
        else:
            print("Verifique sua hora de expediente de SAIDA!!!")

    def verifica_atraso(self):
        atraso_entrada = self.hora_entrada - self.expediente_entrada
        atraso_saida = self.hora_saida - self.expediente_saida
        self.gera_ocorrencia(atraso_entrada, atraso_saida)

    def gera_ocorrencia(self, atraso_entrada, atraso_saida):
        if atraso_entrada > 10:
            self.ocorrencia += 1
            print(f'Você teve ATRASO de ENTRADA de {atraso_entrada}')
        else:
            print("Sua batida de ENTRADA não gerou OCORRÊNCIA!")

        if atraso_saida< -10:
            self.ocorrencia += 1
            print(f'Você teve uma saída adiantada de {atraso_saida}')
        else:
            print("Sua batida de SAÍDA não gerou OCORRÊNCIA!")

    expediente_entrada = property(get_expediente_entrada, set_expediente_entrada)
    expediente_saida = property(get_expediente_saida, set_expediente_saida)

class Operador(Funcionarios):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)

class Repositor(Funcionarios):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)

paulo = Funcionarios("paulo", 1723)
paulo.hora_entrada = "07:20"
paulo.hora_saida = "16:49"
paulo.expediente_entrada = "07:00"
paulo.expediente_saida = "17:00"
print("*"*20)
print(paulo)
paulo.verifica_atraso()
print("Você tem ",paulo.ocorrencia," ocorrencia")
print("*"*20)