class Super():
    def __init__(self, hora):
        self.__hora = 0

    def bom_dia(self):
        print("Bom dia, eu sou a superclasse!")

    @property
    def hora(self):
        print("GET")
        return self.__hora

    @hora.setter
    def hora(self, nova_hora):
        print("SET")
        self.__hora = nova_hora
  
# class Sub(Super):
#     def bom_dia(self):
#         print("Bom dia, eu sou a subclasse!")

# objeto = Sub()
# objeto.bom_dia()
print("="*20)
objeto2 = Super(12)
# objeto2.bom_dia()
print(objeto2.hora)
objeto2.hora = 12
print(objeto2.hora)