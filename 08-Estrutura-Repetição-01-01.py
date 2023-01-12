from time import sleep
for c in range(1,6):
    print('oi')
print('Fim')

for c in range(1,7):
    print(c)
print('fim')

for c in range(6, 0 , -1):
    print(c)
print('fim')

n = int(input('fala numero:'))
for c in range(0 , n+1):
    print(c)
print('Fim')

i = int(input('I:'))
f = int(input('F:'))
p = int(input('P:'))
for c in range(i , f+1 , p):
    print(c)
print('Fim')


#Contagem regressiva
contador = int(input('digite um numero:'))
for c in range(contador , -1 , -1):
    print(c)
    sleep(1)
print('🎆')


#Só numero par
for par in range(2, 51 , 2):
    print('..' , end='')
    print(par, end=' ')
print('Acabou')

#Soma de impares multiplos de 3
simpar = 0
cimpar = 0
for impar in range(1, 501 , 2):
    if impar % 3 == 0:
        cimpar = cimpar + 1
        simpar = simpar + impar
        print(impar , end=' ')
print('A soma de {} valores foi de {}'.format(simpar))

#Tabuada v2.0
num85 = int(input('Digite um numero>'))
for num86 in range(1 , 11):
    print('{} x {:2} = {}'.format(num85 , num86 , num85*num86))
    
    
    
# Soma dos pares
spar = 0
cpar = 0
for par5 in range(1 ,7):
    par88 = int(input('Digite o {} valor :'.format(par5)))
    if par88 % 2 ==0:
        spar += spar 
        cpar += 1
print('Vc informou {} numero e a soma foi de {}'.format(cpar , spar))
