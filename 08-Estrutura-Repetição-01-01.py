from time import sleep
from datetime import date
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


#Progressão aritmetica
proga = int(input('Primeiro termo:'))
progar = int(input('Razão:'))
progat = int(input('Termo:'))
for proga1 in range(proga , progat , progar):
    print('{}'.format(proga1), end=' > ')
print('Acabou!')


#Numeros primos
Nprimo = int(input('Digite um numero:'))
tot = 0
for primo in range(1 , Nprimo + 1):
    if Nprimo % primo == 0:
        print('\033[34m' , end=' ')
        tot += 1
    else:
        print('\033[m' , end=' ' )
    print('{}'.format(primo), end=' ')
print('O numero {} foi divisivel {} vezes'. format (Nprimo , tot))
if tot == 2 :
    print('É por isso ele é primo')
else:
    print('Por isso n é primo.')
    
    
#Detector de Palindromo
frasep = str(input('Digite a frase:')).strip().upper()
palavrasp = frasep.split()
juntop = '*'.join(palavrasp)
inversop = ''
for letrap in range(len(juntop) -1, -1 ,-1):
    inversop += juntop[letrap]
if inversop == juntop:
    print('Temos um palindromo!')
else:
    print('A frase n é um palindromo.')


#grupo maior idade
AnAtual = date.today().year
totmaior = 0 
totmenor = 0
for pess in range(1 , 8):
    nascimentog = int(input('Nascimento:'))
    idadeg = AnAtual - nascimentog
    print('Essa pessoa tem {} anos.'.format(idadeg))
    if idadeg > 17:
        totmaior += 1
        print('Maior de idade')
    else:
        totmenor += 1
        print('Menor de idade')
print('Tivemos {} maior de idade e tivemos {} menor de idade.'.format(totmaior , totmenor))
print('Fim.')

#maior menor sequencia 
maiorp = 0
menorp = 0
for pesoq in range(1 , 6):
    peso1 = float(input('Digite o {}ª peso:'.format(pesoq)))
    if pesoq == 1:
        maiorp = peso1
        menorp = peso1
    else:
        if peso1 > maiorp:
            maiorp = peso1
        if peso1 < menorp:
            menorp = peso1
print('O maior foi {} kg.'.format(maiorp))
print('O menor peso foi {} kg'.format(menorp))


#Analisador completo
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for pessoas in range( 1 , 5):
    print('----------------- {}ª pessoa ----------------'.format(pessoas))
    nomepessoa = str(input('Nome:' )).strip()
    idadepessoa = int(input('Idade:'))
    sexopessoa = str(input('Sexo:')).strip()
    somaidade += idadepessoa
    if pessoas == 1 and sexopessoa in 'Mm' :
        maioridadehomem = idadepessoa
        nomevelho = nomepessoa
    if sexopessoa in 'Mm' and idadepessoa > maioridadehomem:
        maioridadehomem = idadepessoa
        nomevelho = nomepessoa
    if sexopessoa in 'Ff' and idadepessoa < 20:
        totmulher20 += 1 
mediaidade = somaidade / 4
print('A media de idade do grupo é de  {} anos'.format(mediaidade))
print(' O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem , nomevelho))
print('Ao todo tem {} mulheres de 20 anos. '.format(totmulher20))
 
