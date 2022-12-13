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
# caso o atraso seja maior que 10 minutos registre uma ocorrencia
# OBS: Lembre-se de fazer os GETs e SETs
# OBS: Não esqueça das validações
# OBS: Faça a impressão dos elementos corretamente
from random import randrange
from datetime import timedelta

class RelogioDePonto():
    def converte(self, horas):
        minutos = horas * 60
        return minutos

    def get_hora_entrada(self):
        # return  str(timedelta(minutes=self.__hora_entrada))
        return  self.__hora_entrada

    def set_hora_entrada(self, entrada):
        if int(entrada[0:2]) >= 0 and int(entrada[0:2]) < 24 and int(entrada[3:5]) >= 0 and int(entrada[3:5]) < 60:
            converte_hora = self.converte(int(entrada[0:2]))
            minutos = converte_hora + int(entrada[3:5])
            self.__hora_entrada = minutos
        else:
            print("Verifique sua batida de ENTRADA!!!")

    def get_hora_saida(self):
        # return  str(timedelta(minutes=self.__hora_saida))
        return  self.__hora_saida
        
    def set_hora_saida(self, saida):
        if int(saida[0:2]) >= 0 and int(saida[0:2]) < 24 and int(saida[3:5]) >= 0 and int(saida[3:5]) < 60:
              converte_hora = self.converte(int(saida[0:2]))
              minutos = converte_hora + int(saida[3:5])
              self.__hora_saida = minutos
        else:
            print("Verifique sua batida de SAÍDA!!!")
        
    def __str__(self):
        return f' Você entrou as {self.get_hora_entrada()} e saiu as {self.get_hora_saida()}! '

    hora_entrada = property(get_hora_entrada, set_hora_entrada)
    hora_saida = property(get_hora_saida, set_hora_saida)

class Funcionarios(RelogioDePonto):
    def __init__(self, nome):
        self.__nome = nome
        self.__matricula = randrange(1000, 10000)
        self.__ocorrencia = 0

    @property
    def nome(self):
        return self.__nome.title()
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self):
        print("Impossivel alterar a matricula. Fale com o ADM.")

    @property
    def ocorrencia(self):
        return self.__ocorrencia

    @ocorrencia.setter
    def ocorrencia(self, nova_ocorrencia):
        self.__ocorrencia = nova_ocorrencia

    def get_expediente_entrada(self):
        # return  str(timedelta(minutes=self.__expediente_entrada))
        return  self.__expediente_entrada

    def set_expediente_entrada(self, ex_entrada):
        if int(ex_entrada[0:2]) >= 0 and int(ex_entrada[0:2]) < 24 and int(ex_entrada[3:5]) >= 0 and int(ex_entrada[3:5]) < 60:
              converte_hora = self.converte(int(ex_entrada[0:2]))
              minutos = converte_hora + int(ex_entrada[3:5])
              self.__expediente_entrada = minutos
        else:
            print("Verifique sua hora do expediente de ENTRADA!!!")

    def get_expediente_saida(self):
        # return  str(timedelta(minutes=self.__expediente_saida))
        return  self.__expediente_saida

    def set_expediente_saida(self, ex_saida):
        if int(ex_saida[0:2]) >= 0 and int(ex_saida[0:2]) < 24 and int(ex_saida[3:5]) >= 0 and int(ex_saida[3:5]) < 60:
              converte_hora = self.converte(int(ex_saida[0:2]))
              minutos = converte_hora + int(ex_saida[3:5])
              self.__expediente_saida = minutos
        else:
            print("Verifique sua hora do expediente de SAÍDA!!!")

    def verifica_atraso(self):
        atraso_entrada = self.hora_entrada - self.expediente_entrada
        atraso_saida = self.hora_saida - self.expediente_saida
        self.gera_ocorrencia(atraso_entrada, atraso_saida)

    def gera_ocorrencia(self, atraso_entrada, atraso_saida):
        if atraso_entrada > 10:
            self.ocorrencia += 1
            print(f'Você teve um atraso de ENTRADA de {str(timedelta(minutes=atraso_entrada))}')
        else:
            print("Sua batida de ENTRADA não gerou OCORRÊNCIA.")

        if atraso_saida < -10:
            self.ocorrencia += 1
            print(f'Você teve uma SAÍDA adiantada de {str(timedelta(minutes=abs(atraso_saida)))}')
        else:
            print("Sua batida de SAÍDA não gerou OCORRÊNCIA.")
            
    expediente_entrada = property(get_expediente_entrada, set_expediente_entrada)
    expediente_saida = property(get_expediente_saida, set_expediente_saida)

    def __str__(self):
        return f'Olá {self.nome}, sua matricula é {self.matricula} e você é um {self.__class__.__name__} \nseu horário de expedinete é das {str(timedelta(minutes=self.expediente_entrada))} às {str(timedelta(minutes=self.expediente_saida))} e seu ponto hoje foi: \nEntrada: {str(timedelta(minutes=self.get_hora_entrada()))} \nSaída: {str(timedelta(minutes=self.get_hora_saida()))} \nVocê teve {self.ocorrencia} ocorrência(s).'      
  
class Operador(Funcionarios):
    def __init__(self, nome):
        super().__init__(nome)

class Repositor(Funcionarios):
    def __init__(self, nome):
        super().__init__(nome)

joao = Funcionarios("João")
joao.set_expediente_entrada("08:00")
joao.set_expediente_saida("17:00")
# print(joao.get_expediente_entrada())
# print("="*20)
# print(joao.get_expediente_saida())
# print("="*20)
joao.set_hora_entrada("08:15")
joao.set_hora_saida("16:49")
# print(joao.get_hora_entrada())
# print("="*20)
# print(joao.get_hora_saida())
print("="*20)
joao.verifica_atraso()
print("="*20)
print(joao)

vicente = Operador("Vicente")
vicente.set_expediente_entrada("08:00")
vicente.set_expediente_saida("17:00")
# print(vicente.get_expediente_entrada())
# print("="*20)
# print(vicente.get_expediente_saida())
# print("="*20)
vicente.set_hora_entrada("08:03")
vicente.set_hora_saida("17:12")
# print(vicente.get_hora_entrada())
# print("="*20)
# print(vicente.get_hora_saida())
print("="*20)
vicente.verifica_atraso()
print("="*20)
print(vicente)

roberto = Repositor("Roberto")
roberto.set_expediente_entrada("08:00")
roberto.set_expediente_saida("17:00")
# print(roberto.get_expediente_entrada())
# print("="*20)
# print(roberto.get_expediente_saida())
# print("="*20)
roberto.set_hora_entrada("08:13")
roberto.set_hora_saida("17:12")
# print(roberto.get_hora_entrada())
# print("="*20)
# print(roberto.get_hora_saida())
print("="*20)
roberto.verifica_atraso()
print("="*20)
print(roberto)