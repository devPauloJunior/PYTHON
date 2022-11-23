class Super():
    def bom_dia(self):
        print("Bom dia, eu sou a superclasse!")
  
class Sub(Super):
    def bom_dia(self):
        print("Bom dia, eu sou a subclasse!")

objeto = Sub()
objeto.bom_dia()
print("="*20)
objeto2 = Super()
objeto2.bom_dia()