from time import sleep
import math 
from random import randint
tempo = int(input('Tempo:'))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
    print('fim')
    
#elogio a indentação importa

n = str(input('Qual seu nome?'))
if n  == 'Matheus':
    print('Que nome lindo!')
else:
    print('legal')
    
#Media
n1 = float(input('Digite a nota:'))
n2 = float(input('Digite a nota:'))
m = (n1 + n2)/2
print('A media foi {}'.format(m))
if m >= 6.0:
    print('Aprovado')
else:
    print('Reprovado')
    
#Pensando numero aleatorio
c = randint(0,5)#soteia
print('-=-'*20)
print('Vou pensar em um numero de 0 a 5, divinhe.')
print('-=-'*20)
jogador = int(input('Em que numero pensei?'))
sleep(2)
if jogador == c:
    print('Parabens!')
else:
    print('Pedeu!')
 
 
    
#Radar eletrônico
velocidade = float(input('Qual velocidade do carro?'))
multa = (velocidade-80) * 7
if velocidade > 80:
    print('Multado!')
    multa = (velocidade-80) * 7
    print('Vc vai pagar {:.2f}R$'.format(multa))
    print('dirija com segurança')
else:
    print('Tenha um bom dia.')

