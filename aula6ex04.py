class Aluno:
    def __init__(self, ra, nome, turma):
        self.ra = ra
        self.nome = nome
        self.turma = turma

    def exibe_notas(self):
        print(f'RA: {self.ra}')
        print(f'Nome: {self.nome}')
        print(f'Turma: {self.turma}')

    def inserir_nota(self, nota):
        self.notas.append(nota) 

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
a1 = Aluno('23062', 'Diogo', '2S.I')
a1.exibe_notas()
    