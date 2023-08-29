sexos = []
sexo = str(input('Digite F para feminino, M para masculino e "sair" para sair: ')).lower()
while sexo != 'sair':
    sexo = str(input('Digite F para feminino, M para masculino e "sair" para sair: ')).lower()
    sexos.append(sexo)
print('Foram digitados {} vezes o sexo feminino e {} vezes o sexo masculino'.format(sexos.count('f'), sexos.count('m')))
print('Parou...')