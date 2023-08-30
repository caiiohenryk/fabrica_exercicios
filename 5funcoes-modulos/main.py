def calculadora():
    def soma(a,b):
        return a+b
    def div(a,b):
        return a/b
    def sub(a,b):
        return a-b
    def multi(a,b):
        return a*b
    escolha = input('Digite a operação desejada: ')
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    match escolha:
        case 'soma':
            print(soma(a,b))
        case 'div':
            print(div(a,b))
        case 'sub':
            print(sub(a,b))
        case 'multi':
            print(multi(a,b))