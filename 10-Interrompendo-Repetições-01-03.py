from random import randint
cont = 1
while cont <=10:
    print(cont , '... ' , end='')
    cont += 1
print('Acabou')


n = 0
s = 0
contador = 0
while n != 999:
    n = int(input('Leia:'))
    contador += 1
    s += n
print(s)
#fazendo o luppin só botar o true no lugar do " n != 999"
while True:
    n = int(input('Leia:'))
    if n == 999:
        break
    contador += 1
    s += n
print(f'A soma é {s} a quantidade de vezes foi {contador}.')

nome = 'Jose'
idade = 33
salario = 1000
print(f'O {nome} tem {idade} anos e ganha {salario} reais.')

#exercicios

while True:
    n = int(input('Quer ver a tabuada de qual valor?:'))
    if n < 0:
            break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('Fim')


#Impar ou Par jogo
v = 0
while True:
    jogador = int(input('Diga um valor:'))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in  'PpIi':
        tipo = str(input('Par ou impar.')).strip().lower()[0]
    print(f'Vc jogou {jogador} e o computador {computador}. total de  {total} ')
    if tipo == 'Pp':
        if total % 2 == 0:
            print('Venceu')
            v += 1
        else:
            print('Pedeu')
            break
    elif tipo == 'Ii':
        if total % 2 == 1:
            print('Veceu')
            break
        else:
            print('Perdeu')
            break
    print('Vamos jogar novamente...')
print(f'Game over! Voce venceu {v} vezes.')
    
#Analise de dados do grupo
total18 = 0
totalM = 0
totalF = 0
while True:
    i = int(input('Idade:'))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo:')).strip().upper()[0]
    if i >= 18:
        total18 += 1
    if s  == 'M':
        totalM += 1
    if s == 'F' and i < 20:
        totalF += 1               
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]   
print('Acabou')
print(totalM)
print(totalF)    

# Estatisticas em produtos



    