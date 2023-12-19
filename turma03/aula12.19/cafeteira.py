class Cafeteira:
    compartimento_filtro = False
    compartimento_agua = False
    cafe_pronto = False
    ligada = False

    def ligar(self):
        self.ligada = True
        print('Cafeteira Ligada')

    def desligar(self):
        self.ligada = False
        self.compartimento_agua = False
        self.compartimento_filtro = False
        self.cafe_pronto = False
        print('Cafeteira Desligada')

    def colocar_agua(self):
        if self.ligada == True:
            self.compartimento_agua = True

    def colocar_filtro(self):
        if self.ligada == True:
            if self.compartimento_filtro == False:
                self.compartimento_filtro = True

    def fazer_cafe(self):
        if self.ligada == True and self.compartimento_filtro == True and self.compartimento_agua == True:
            self.cafe_pronto = True
        else:
            print('Verifique os compartimentos')

    def valida_cafe(self):
        if self.cafe_pronto == True:
            return 'Pronto'
        else:
            return 'Aguarde...'

    def valida_ligada(self):
        if self.ligada == True:
            return 'Ligada'
        else:
            return 'Desligada'

    def valida_filtro(self):
        if self.compartimento_filtro == True:
            return 'com filtro'
        else:
            return 'sem filtro'
    
    def valida_agua(self):
        if self.compartimento_agua == True:
            return 'com agua'
        else:
            return 'sem agua'
          
    def __str__(self):
        return f'A cafeteira está { self.valida_ligada() }, o compartimento de agua está { self.valida_agua() }, o compartimento do filtro está { self.valida_filtro() }. E o café: { self.valida_cafe() },'
    

minha_cafeteira = Cafeteira()

print(minha_cafeteira)

minha_cafeteira.ligar()

print(minha_cafeteira)

minha_cafeteira.fazer_cafe()

minha_cafeteira.colocar_agua()

print(minha_cafeteira)

minha_cafeteira.colocar_filtro()

print(minha_cafeteira)

minha_cafeteira.fazer_cafe()

print(minha_cafeteira)