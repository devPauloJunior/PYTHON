class Filmes:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao

class Series:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas

vingadores = Filmes('vingadores - ultimato', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}')

bigbang = Series("bigbang a teoria", 2005, 12)
print(f'Nome: {bigbang.nome} - Ano: {bigbang.ano} - Temporadas: {bigbang.temporadas}')