class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = float(saldo)
    def depositar(self,deposito):
        self.saldo += deposito
        print(f'Voce agora tem {self.deposito}')
    def sacar(self,saque):
        self.saldo -= saque
        print(f'Voce agora tem {self.saldo}')
caio = Conta('Caio', 1200)
print(caio.saldo)
caio.sacar(329)
