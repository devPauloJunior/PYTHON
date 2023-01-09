class MeuCrivo():
    def __init__(self, num_verificador):
        if type(num_verificador) == type(int()):
            self.num_verificador = num_verificador
            self.primos = set()
        else:
            raise TypeError("O numero informado não atende a solicitação.")

    def verifica_primo(self, num):
        for i in range(2, num):
            if num % i == 0:
                # print(num)
                return False
        return True

    def eratostenes(self):
        for i in range(2, self.num_verificador+1):
            if self.verifica_primo(i):
                self.primos.add(i)
        return self.primos

    def imprime(self): 
        print(f'Primos entre 2 e {self.num_verificador}:')
        for numero, candidato in enumerate(self.primos):
            if candidato in self.primos:
                if (numero+1) != len(self.primos):
                    print(candidato, end=", ")
                else:
                    print(candidato)
        return None

# Criação do Objeto
meu_primo = MeuCrivo(int(input("Diga o valor: ")))
meu_primo.eratostenes()
meu_primo.imprime()
