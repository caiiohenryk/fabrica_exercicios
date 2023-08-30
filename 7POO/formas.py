class Formas():
    def __init__(self):
        pass
class Circulo(Formas):
    def circulo(self,raio):
        Circulo.area = 2*raio**2
        print(f'A area do circulo eh {self.area}')
class Quadrado(Formas):
    def quadrado(self, lado):
        self.area = lado**2
        print(f'A area do quadrado eh {self.area}')
class Retangulo(Formas):
    def retangulo(self, base, altura):
        self.area = base*altura
        print(f'A area do retangulo é {self.area}')

circulo = Circulo()
circulo.circulo(20)