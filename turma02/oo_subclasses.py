class Forma():
    def __init__(self, lado01, lado02):
        self._lado01 = lado01
        self._lado02 = lado02

    def get_area(self):
        return self._lado01 * self._lado02

    def __str__(self):
        return f'A area desta {self.__class__.__name__} é {self.get_area()}'

class Retangulo(Forma): # Superclass
    def __str__(self):
        return f'A area deste {self.__class__.__name__} é {self.get_area()}'

class Quadrado(Retangulo):
    def __str__(self):
        return f'A area deste {self.__class__.__name__} é {self.get_area()}'

retangulo = Retangulo(4, 6)
print(retangulo.__str__())
print("="*20)
quadrado = Quadrado(8, 8)
print(quadrado.__str__())