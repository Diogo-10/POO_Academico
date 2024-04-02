class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, porcentagem):
        self.salario += porcentagem/100 * self.salario

nome = input('Nome? ')
salario = float(input('Salário? R$ '))
aumento = float(input('Aumento (%)? '))

f = Funcionario(nome, salario)
f.aumentar_salario(aumento)

print(f'Salário atual = R$ {f.salario:.2f}')