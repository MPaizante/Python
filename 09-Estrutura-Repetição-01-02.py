#REPETIÇÃO WHILE

c = 1
while c <10:
    print (c)
    c = c + 1
print('fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor'))
    r = str(input('Quer continuar S/N?')).upper()
print('Fim')

nu = 1
par = impar = 0
while nu != 0:
    nu = int(input('Digite um valor: '))
if n != 0:
    if n % 2 == 0:
       par += 1
    else:
        impar += 1
print('Acabou')
print('{} par {} impar.'.format(par , impar))