class Televisao:
    def __init__(self):
        self.canal = None
        self.volume = 0
        self.ligada = False
        self.muda = False

    def __repr__(self):
        if self.ligada:
            return '-' * 20 + '\n' + \
                   f'Canal.: {self.canal}\n' + \
                   f'Volume: {self.volume}\n' + \
                   '-' * 20 + '\n'
        else:
            return '-' * 20 + '\n' + \
                   f'TV desligada!\n' + \
                   '-' * 20 + '\n'

    def mutar(self):
        self.muda = not self.muda
        if self.muda:
            print('Televisão muda')
        else:
            print(f'Volume: {self.volume}')

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def alterar_canal(self, canal):
        self.canal = canal

    def power(self):
        self.ligada = not self.ligada

tv = Televisao()
print(tv)
tv.power()
tv.alterar_canal(7)
print(tv)
for _ in range(20):
    tv.aumentar_volume()
print(tv)
tv.mutar()
tv.mutar()
tv.power()
print(tv)