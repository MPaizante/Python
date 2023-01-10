from time import sleep
import math 
from random import randint
from datetime import date
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


#impar ou par 
nnn = int(input('Me diga um numero:'))
res = nnn % 2
print('O resultado foi {}'.format(res))
if res == 0:
    print('Resultado {} é PAR'.format(nnn))
else:
    print('Resultado {} é ÍMPAR'.format(nnn))


#custo de uma viagem
d = float(input('Qual distancia?'))
print('Você está preste a começar uma viagem de {}Km'.format(d))
if d <= 200:
    pre1 = d * 0.50
    print('O preço vai ser R${:.2f}'.format(pre1))
else:
    pre = d * 0.45
    print('O preço vai ser R${:.2f}'.format(pre))
    
    
#Ano Bissexto
An = int(input('Que ano analizar? 0 vc bota o ano da maquina.'))
if An == 0:
    An = date.today().year#ano atual
if An % 4 == 0 and An % 100 !=0 or An % 400 ==0:
    print('Ano {} é Bissexto.'.format(An))
else:
    print('Ano {} n é bissexto.'.format(An))
    
    
#Maior e menor
a = int(input('Valor:'))
b = int(input('Valor:'))
c1 = int(input('Valor:'))
#Verificando o menor.
if a < b and a < c1:
    men = a
if b < c1 and b < a:
    men = b
if c1 < a and c1 < b:
    men = c
#Verificando o Maior.
    mai = a
if b > a and b > c:
    mai = b  
if c > a and c > b:
    mai = c
    print('Menor digitiro {}'.format(men))
    print('Maior digito {}'.format(mai))