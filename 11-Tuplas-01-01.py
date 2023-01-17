from random import randint
lanche = ('Hamburguer' , 'Suco' , 'Pizza' , 'Pudim')
#Tuplas são imutaveis
print(lanche [1])
for comida in lanche:
    print(f'Vou comer {comida}.')
print('Comi bastante')
print(sorted(lanche))
a = (2 , 5 , 4)
b = (5 , 8, 1 ,2)
c = a + b
print(sorted(c))
print(c.count(2))#contar 
print(c.index(5))

pessoa = ('Gustavo' , 39 , 'M' , 99.88)
print(pessoa)


#Numero por extenso
cont = ('zero' , 'um ' , 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete' , 'oito', 'nove' , 'dez')

while True:
    num = int(input('Digite um numero de 0 ate 10  :'))
    if 0 <= num <= 10:
        break
    print('tente novamente.', end='')
print(f'Voce digitou o numero {cont[num]}')

#Tuplas com Times de Futebol
times  = ('c','p','s','cr','f','v','ch','atlmg','b','atpr','ba','Sp','flu','spt','vit','cot','ava','pp','atgo',) 
print(f'Lista de times: {times}')
print(f'Os cinco primeiros são {times[:5]}')
print(f'Os quatro ultimos são {times[-4:]}')
print(f'times em ordem alfabetica: {sorted(times)}')
print(f'O chapeconse esta na {times.index("ch")+1}ª')

#Maior e menor valores em Tupla
n1 = (randint(1,10) , randint(1,10) , randint(1,10) , randint(1,10) , randint(1,10))
print(f'Eu sorteei o valor {n1}', end=' ')

for n2 in n1:
    print(f'{n1}' , end='')
print(f'O maior valor sorteado foi {max(n1)}')
print(f'O menor valor foi {min(n1)}')
