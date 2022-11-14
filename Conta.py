class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor

    def trasferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)