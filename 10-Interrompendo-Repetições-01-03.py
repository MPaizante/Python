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
    