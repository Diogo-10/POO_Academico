class Triangulo:
    def __init__(self, a, b, c):
        self.lado_a = a
        self.lado_b = b
        self.lado_c = c

    def __repr__(self):
        return f'Triângulo: {self.lado_a} | {self.lado_b} | {self.lado_c}'

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c
    
a = float(input('Lado A? '))
b = float(input('Lado B? '))
c = float(input('Lado C? '))

t = Triangulo(a, b, c)
print(t)

print(f'Perímetro = {t.calcular_perimetro():.2f}')