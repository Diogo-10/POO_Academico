class Funcionario:
    def __init__(self, nome, sobrenome, salario_mensal):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario_mensal = salario_mensal

    def aumentar_salario(self, porcetagem):
        self.salario_mensal += porcetagem/100 * self.salario_mensal

nome = input('Nome: ')
sobrenome = input('Sobrenome: ')
salario = float(input('Sálario: '))
aumento = float(input('Aumento %: '))

f = Funcionario(nome, sobrenome, salario)
f.aumentar_salario(aumento)

print(f'Sálario atual = R$ {f.salario_mensal:.2f}')



    