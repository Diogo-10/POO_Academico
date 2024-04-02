class Carro:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def exibir_dados(self):
        print('-' * 30)
        print(f'Marca:. {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Placa:. {self.placa}')
        print('-' * 30)

c1 = Carro('Honda', 'Civic', 'DIH2025')
c1.exibir_dados()

c2 = Carro('Porsche', 'Macan', 'DIH2028')
c2.exibir_dados()
