#REPETIÇÃO WHILE
from random import randint
from math import factorial
from tkinter import NUMERIC

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



sexo1 = str(input('Sexo:')).strip().upper()[0]
idade1 = int(input('Idade:'))
while sexo1 not in 'MmFf':
    sexo1 = str(input('dados invalidos, informe o sexo:')).strip().upper()[0]
print('Sexo {} salvo.'.format(sexo1))






#Exercicios 
#Validação de sexo

sexo2 = str(input('Digite o sexo:')).strip().upper()[0]
while sexo2 not in 'MmFf':
    sexo2 = str(input('Digite novamente, invalido:')).strip().upper()[0]
print('Sexo {} salvo.'.format(sexo1))

#Jogo da Adivinhação v2.0
comp = randint (0,10)
print('Acabei de pensar em um numero de 0 até 10. Tente advinhar.')
acetou = False
palpites = 0
while not acetou:
    jogador = int(input('QUal o seu palpite?'))
    palpites += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print('Ta quente.')
        elif jogador > comp:
            print('Ta frio.')
print('Acertou.')
        
#Criando um Menu de Opções       

n1 = int(input('Primeiro Valor:'))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    

    print('''        [1] somar
        [2] Multiplicar
        [3] Maior numero
        [4] Novos numeros
        [5] Sair do Programa''')
    opção = str(input(('Qual é a sua opção:')))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1 , n2 , soma))
    elif opção == 2: 
        produto = n1 * n2
        print('A multiplicação é: '.format(produto))   
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1 , n2 , maior))       
    elif opção == 4:
        print('Digite novamente:')
        n1 = int(input('Digite novamente:'))
        n2 = int(input('Digite novamente:'))
    elif opção == 5:  
        print('Finalizado')
    else:
        print('Opção invalida.')
        
print('Fim do programa')


#calculo do fatorial
n3 = int(input('Digite um numero:'))
f = factorial(n3)
print('O fatorial de {} é {}.'.format(n , f))
#ou 
n4 = int(input('Digite um numero:'))
c4 = n4
f4 = 1
print('Calculando o fatocial de {}! = '.format(n4), end=' ')
while c4 > 0:
    print('{} '.format(c4), end=' ')
    print(' x ' if c4 > 1 else ' = ', end=' ')
    f4 = f4 * c4
    c4 -= 1
print('O fatorial de {}'.format(f4))


#Progressao Aritmetica v2.0
print('Gerador de PA')
print('=-'*10)
primeiro1 = int(input('Primeiro termo:'))
razão1 = int(input('Razão:'))
termo1 = primeiro1
cont1 = 1
fimtermo = int(input('Digite quantos termos: '))
while cont1 <= fimtermo:
    print('{}'.format(termo1), end=' ')
    termo1 += razão1
    cont1 += 1
print('Fim')



#Super PA v3.0

print('Gerador de PA')
print('=-'*10)
primeiro1 = int(input('Primeiro termo:'))
razão1 = int(input('Razão:'))
termo1 = primeiro1
cont1 = 1
mais = 10
while mais != 0:
    total = total + mais
    while cont1 <= 10:
        print('{}'.format(termo1), end=' ')
        termo1 += razão1
        cont1 += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais?'))
print('Fim')

#sequencia de fibonacci 
print('Sequencia de Fibonacci ')
print('-'*20)
n5 = int(input('Quantos termos vc quer mostrar?'))
t1 = 0
t2 = 1
print('{} → {}'.format(t1 , t2))
cont2 = 3
while cont2 <= n5:
    t3 = t1 + t2
    print('→ {}'.format(t3), end=' ')
    t1 = t2 
    t2 = t3 
    cont2 += 1
print('Fim')


#Tratando varios valores v1.0
numst = 0
contnum = 0
somanum = 0
numst = int(input('Digite um numero. Para parar digite 999.'))
while numst != 999:   
    somanum += numst
    contnum += 1
    numst = int(input('Digite um numero. Para parar digite 999.'))
print('Voce digitou {} numeros e a soma é {}.'.format(contnum , somanum ))
print('Acabou')


#maior e menor valores
resp = 'S'
media = 0
mediasoma = 0
quantidade = 0
maior2 = 0
menor2 = 0
while resp in 'Ss':
    numero = int(input('Digite um numero:'))
    mediasoma += numero
    quantidade += 1   
    if quantidade == 1:
        maior2 == menor2 == numero
    else:
        if numero > maior2:
            maior2 = numero
        if numero < menor2:
            menor2 = numero
    resp = str(input('Quer continuar S/N ?')).upper().strip()[0]
media = mediasoma / quantidade
print('Vc digitou {} vezes e a media foi {}.'.format(quantidade , media))
print('O maior numero foi {} e o menor foi {}.'.format(maior2 , menor2))
print('Acabou.')















