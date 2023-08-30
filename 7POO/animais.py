class Animais():
    def __init__(self,peso,nome):
        self.peso = peso
        self.nome = nome
        print(f'{nome} eh um animal.')
    
class Cachorro(Animais):
    def latir(self):
        print(f'{self.nome} faz auau')
class Gato(Animais):
    def miar(self):
        print(f'{self.nome} faz miauu')

rex = Cachorro(12, 'Rex')
rex.latir()
mel = Gato(3, 'Mel')
mel.miar()