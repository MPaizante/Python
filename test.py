
while True:
    i = int(input('Idade:'))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo:')).strip().upper()[0]
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]   
print('Acabou')

