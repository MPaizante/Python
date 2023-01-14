#REPETIÇÃO WHILE
from random import randint

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
