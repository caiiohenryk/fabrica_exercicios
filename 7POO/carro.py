class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def acelerar(self,velocidadeatual,acel):
        velocidadeatual += acel
        print(f'Acelerando o carro, agora voce esta a {velocidadeatual}Km/h')
        return velocidadeatual
uno = Carro('fiat', 'uno', 2012)
uno.acelerar(80, 15)