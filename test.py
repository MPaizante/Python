v1 = []
while True:
    v1.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar ? [S/N] '))
    if resp in 'Nn':
        break
print(f'Você digitou {len(v1)} elementos.')
v1.sort(reverse=True)
print(f'Os valores de ordem descrecentes {v1}')
