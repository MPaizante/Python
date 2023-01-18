

#Dividindo valores em varias listas
n3 = list()
par = list()
impar = list()
while True:
    n3.append(int(input('Digite um numero: ')))
    res = str(input('Quer continuar? [S/N] '))
    if res in 'Nn':
        break
for i , v in enumerate(n3):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista compelta é {n3}')
print(f'A lista de par é {par}')
print(f'A lista de impar é {impar}')