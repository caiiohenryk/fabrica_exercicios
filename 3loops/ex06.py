numeros = []
num = int(input('Digite um numero: '))

if num != 0:
    print('Número inserido não é 0. Insira 0 para sair')
    while num != 0:
        num = int(input('Digite outro numero: '))
        numeros.append(num)
        print(sum(numeros))
else:
    print('Parou')