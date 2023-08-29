velocidade = float(input('Velocidade do veículo: '))

if velocidade > 80:
    print(f'Você foi multado em R${((velocidade-80)*7)} por ultrapassar a velocidade permitida')
else:
    print('Tá de boa, meu bom :)')