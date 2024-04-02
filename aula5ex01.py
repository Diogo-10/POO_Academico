class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def __repr__(self):
        return '-' * 30 + '\n' + \
               f'Título.: {self.titulo}\n' + \
               f'Autor..: {self.autor}\n' + \
               f'Páginas: {self.num_paginas}\n' + \
               '-' * 30 + '\n' \

livro1 = Livro('Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 264)
print(livro1)

livro2 = Livro('Poeira em alto mar', 'Alan Bida', 133)
print(livro2)