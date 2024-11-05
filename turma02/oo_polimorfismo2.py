class FormasGeometricas():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def get_area(self):
        return self.base* self.altura

    def set_area(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura

    def __str__(self):
        return f'A area deste {self.__class__.__name__} é {self.get_area()}'

class Retangulo(FormasGeometricas):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def get_area(self):
        return self.base* self.altura

    def __str__(self):
        return f'A area deste {self.__class__.__name__} é {self.get_area()}'


class Triangulo(FormasGeometricas):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def get_area(self):
        return self.base* self.altura

    def __str__(self):
        return f'A area deste {self.__class__.__name__} é {self.get_area()}'

retangulo = Retangulo(10, 6)
print(retangulo.__str__())
print("="*20)
retangulo2 = FormasGeometricas(15, 7)
print(retangulo2.__str__())
print("="*20)
triangulo = Triangulo(5, 9)
print(triangulo.__str__())