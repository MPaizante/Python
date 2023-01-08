import math , random
num = int(input('Digite um numero:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}. '.format(num , raiz))

#aparecer só o numero sem oque tem nas virgulas
N = float(input('Digite aqui:'))
R = math.trunc(N)
print('NUmero {} é {} '.format(N , R)) #ou fazer isso
print('Valor {} é {}.'.format(N , int(N)))

#Cateto e hipotenusa
co =  float(input('Cateto oposto:'))
ca = float(input('Cateto Adjacente:'))
hi = math.hypot(co,ca)
# ou pode fazer assim 'hi = (co **2 +ca**2)**(1/2)'
print('A hipotenusa é: {:.2f}'.format(hi))

#Seno, Cosseno e Tangente.
angulo = float(input('Digite um angulo:'))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem seno {:.2f}'.format(angulo , seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem cosseno {:.2f}'.format(angulo , cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem tangente {:.2f}'.format(angulo , tangente))

#sorteio aleatorio
a1 = str(input('A1:'))
a2 = str(input('A2:'))
a3 = str(input('A3:'))
a4 = str(input('A4:'))
lista = [a1 , a2 , a3 , a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))



