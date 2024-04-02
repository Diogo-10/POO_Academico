class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print('Animal Comendo')


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def comer(self):
        print('Cachorro', self.nome, 'comendo')

class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def comer(self):
        print('Gato', self.nome, 'comendo')

def misterio(a):
    a.comer()


#cachorro = Cachorro('Rex', 'Rottweiler')
#cachorro.comer()

x = Cachorro('Billy', 'Maltês')
y = Gato('Félix', 'Siames')
z = Animal('Junior meu filho')
misterio(z)