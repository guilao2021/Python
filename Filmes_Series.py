class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self.nome}  -  {self.likes} likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome}  -  {self.duracao} min  -  {programa.likes} likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome}  -  {self.temporadas} temporadas  -  {programa.likes} likes'


class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def __getitem__(self, item):
        return self.programas[item]

    def __len__(self):
        return len(self.programas)

    @property
    def listagem(self):
        return self.programas

velozes = Filme('velozes e furiosos', 2001, 147)
friends = Serie('friends', 1994, 10)
sempre_lado = Filme('Sempre ao seu lado', 2009, 133)
twd = Serie('The walking dead', 2010, 10)
velozes.dar_likes()
velozes.dar_likes()
twd.dar_likes()
sempre_lado.dar_likes()
sempre_lado.dar_likes()
friends.dar_likes()

playlist = [velozes, friends, twd, sempre_lado]
minha_lista = Playlist('Fim de semana', playlist)

for programa in minha_lista:
    print(programa)
print(f'Tamanho: {len(minha_lista)}')
