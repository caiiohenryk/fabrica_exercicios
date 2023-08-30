class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        print(f'Ola, meu nome eh {nome}, tenho {idade} anos e sou {profissao}.')
    
Caio = Pessoa('Caio', 17, 'estudante')