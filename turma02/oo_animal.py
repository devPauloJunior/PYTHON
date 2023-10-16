#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Na Super classe Animal abaixo sabemos que ela tem:
# duas subclasses: Pessoa e Cao
# você deve definir onde e como serão criados os atributos e os métodos dessas SUPER e SUBs
# atributos: nome, idade, peso e altura
# métodos abaixo:
# envelhecer - esse método aumenta a idade de "Pessoa" em 1 ano e de "Cao" em 7 anos
# engordar - aumenta o peso de "Pessoa" em 300g por 1 kilo e "Cao" 150g por 1Kg comido 
# correr – marque com tempo
# emagrecer – diminui o peso de "Pessoa" em 400g a cada 1h corrida e "Cao" 500g a cada 1h corrida
# crescer – cada ano que passar "Pessoa" cresce 0,5cm e "Cao" cresce 3,5cm
# OBS: Deve ser criado o POLIMORFISMO do ambiente
# OBS: Pessoa só cresce até 21 anos e Cao até 14 anos
# OBS: Lembre-se de fazer os GETs e SETs
# OBS: Não esqueça das validações
# OBS: Fique atento aos impedimentos dos métodos
# OBS: Faça a impressão dos elementos
from datetime import timedelta
class Animal:
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        
    def envelhecer(self, anos):
        self.idade += anos
        self.altura += self.crescer(anos)
        print(f'Você ficou {anos} ano(s) mais velho e agora tem {self.idade} ano(s), com isso agora sua altura é {self.altura}m')

    def converter_kg(self, kg):
        gramas = kg * 1000
        return gramas

    def converter_gr(self, gr):
        quilos = gr/1000
        return quilos

    def comer(self, kg):
        if kg > 0.00 and kg < 3.00:
            converte_kg = self.converter_kg(kg)
            engordou = self.engordar(converte_kg)
            self.peso += self.converter_gr(engordou)
            print(f'Você comeu {converte_kg:.0f}g e engordou {engordou:.0f}g e seu peso subiu para {self.peso:.2f}Kg')
        else:
            print(f'O valor informado de {kg:.2f}kg não condiz com uma alimentação normal.')
    
    def engordar(self, gramas):
        if self.__class__.__name__ == "Pessoa":
            engordou = (300 * gramas) / 1000
            return engordou
        elif self.__class__.__name__ == "Cao":
            engordou = (150 * gramas) / 1000
            return engordou
        else:
            engordou = (300 * gramas) / 1000
            return engordou
    
    def converte(self, horas):
        minutos = horas * 60
        return minutos

    def corer(self, horas):
        if int(horas[0:2]) >= 0 and int(horas[0:2]) < 24 and int(horas[3:5]) >= 0 and int(horas[3:5]) < 60:
            converte_hora = self.converte(int(horas[0:2]))
            minutos = converte_hora + int(horas[3:5])
            emagreceu = self.emagrecer(minutos)
            self.peso -= self.converter_gr(emagreceu)
            print(f'Você correu {str(timedelta(minutes=minutos))} e emagreceu {emagreceu:.0f}g e seu peso diminuiu para {self.peso:.2f}Kg')
        else:
            print("Verifique sua marcação. Tempo de corrida invalido!!!")

    def emagrecer(self, horas):
        if self.__class__.__name__ == "Pessoa":
            emagreceu = (400 * horas) / 60
            return emagreceu
        elif self.__class__.__name__ == "Cao":
            emagreceu = (500 * horas) / 60
            return emagreceu
        else:
            emagreceu = (400 * horas) / 60
            return emagreceu

    def crescer(self, anos):
        if self.__class__.__name__ == "Pessoa":
            if self.idade > 21:
                crescimento = 0.0 
                return crescimento        
            else:
                crescimento = 0.5 * anos / 100 
                return crescimento        
        elif self.__class__.__name__ == "Cao":
            if self.idade > 14:
                crescimento = 0.0 
                return crescimento        
            else:
                crescimento = 3.5 * anos / 100 
                return crescimento
        else:
            crescimento = 0.5 * anos / 100 
            return crescimento        

    def __str__(self):
        return f'Olá {self.nome}, informando que você tem {self.idade}ano(s) de idade, sua altura é de {self.altura}m, seu peso atual é {self.peso:.2f}kg.'

class Pessoa(Animal):
    def __init__(self, nome, idade, peso, altura):
        super().__init__(nome, idade, peso, altura)

class Cao(Animal):
    def __init__(self, nome, idade, peso, altura):
        super().__init__(nome, idade, peso, altura)

joao = Pessoa("Joao", 17, 62.7, 1.70)
print("*"*20)
print(joao)
print("*"*20)
joao.comer(0.45)
print("*"*20)
joao.corer("00:45")
print("*"*20)
print(joao)
print("*"*20)
joao.envelhecer(2)
print("*"*20)
print(joao)

billy = Cao("billy", 7, 15.6, 1.18)
print("*"*20)
print(billy)
print("*"*20)
billy.comer(1.20)
print("*"*20)
billy.corer("01:30")
print("*"*20)
print(billy)
print("*"*20)
billy.envelhecer(2)
print("*"*20)
print(billy)