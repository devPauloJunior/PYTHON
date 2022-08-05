class Pessoa:
    def __init__(self, nome, idade, altura, genero):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.genero = genero
    # VERICAR SE É DE MAIOR
    def de_maior(self):
        if self.idade > 17:
            print("Voce e de maior!!!")
    #VERIFICA SE ESTATURA É MEDIA
    def estatura_media(self):
        if self.altura > 1.64 and self.altura < 1.76:
            print("Sua estatura e mediana")
        else:
            print("Voce e fora da media")

if __name__ == "__main__":
    pessoa1 = Pessoa("João", 25, 1.65, "M")
    print(pessoa1.nome)
    pessoa1.de_maior()
    pessoa1.estatura_media()