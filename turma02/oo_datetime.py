from datetime import timedelta, time

class Aluno():
    def __init__(self, nome, materia):
        self.nome = nome
        self.materia = materia
        self.tempo_sem_dormir = 0

    def converte(self, horas):
        minutos = horas * 60
        return minutos

    def estudar(self, hora_estudar, minuto_estudar):
        converte_hora = self.converte(hora_estudar)
        minuto_estudar += converte_hora
        self.tempo_sem_dormir += minuto_estudar
        return str(timedelta(minutes=self.tempo_sem_dormir))

    def dormir(self, hora_dormir, minuto_dormir):
        converte_hora = self.converte(hora_dormir)
        minuto_dormir += converte_hora
        if self.tempo_sem_dormir > minuto_dormir:
            self.tempo_sem_dormir = self.tempo_sem_dormir - minuto_dormir
        else:
            self.tempo_sem_dormir = minuto_dormir - self.tempo_sem_dormir

        return str(timedelta(minutes=self.tempo_sem_dormir))

    def __str__(self):
        return f'O aluno {self.nome} estudou {self.materia} e passou {str(timedelta(minutes=self.tempo_sem_dormir))} sem dormir'

aluno = Aluno("Roberto", "geografia")
aluno.estudar(1, 15)
aluno.dormir(3, 50)
print(aluno.__str__())