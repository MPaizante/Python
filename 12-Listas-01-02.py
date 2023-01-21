from random import randint
g = [['J' , 19] , ['A' , 33] , ['Jo', 13] , ['Maria' , 45]]
for p in g:
    print(p)
    print(f'{p[0]} tem {p[1]} anos de idade.  ')
    
gal = list()
d = list()
for c in range(0,3):
    d.append(str(input('Nome:')))
    d.append(int(input('Idade:')))
    gal.append(d[:])
    
print(gal)


#Exercicios
#Lista composta e analise de dados.
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('Peso:')))
    if len(princ) == 0:
        mai = men = temp [1]
    else:
        if temp[1] > mai:
           mai = temp[1] 
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Digite se quer continuar. [S/N]')).upper().strip()
    if resp in 'N':
        break
print(f'Os dados foram {princ}')
print(f'Ao todo, voce cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}kg' , end=' ')
for p in princ:
    if p[1] == mai:
        print(f'p[0]', end=' ')
print(f'O menor peso foi {men}kg', end=' ')
for p[1] in princ:
    print(f'{p[0]}', end=' ')
    

#Lista com pares e impares

num = [[] , []]
valor = 0
for y in range(1,8):
    valor = int(input(f'Digite o {y}º valor:'))
    if valor % 2 ==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Todos os valores foram {valor}')
print(num)
print(f'Os valores impares foram: {num[1]}.')
print(f'Os valores pares foram {num[0]}.')



#Matriz em pyton
matriz = [[0 , 0 , 0] , [0 , 0 , 0] , [0 , 0 , 0]]
for l in range(0,3):
    for coluna in range(0,3):
        matriz[l][coluna] = int(input(f'Digite um numero:'))
for l in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[l][coluna]:^5}]', end=' ')
    print()
    
    
    
    
#Mais Matriz
spar = ss = scol = 0
for l in range(0,3):
    for coluna in range(0,3):
        matriz[l][coluna] = int(input(f'Digite um numero para [{l},{coluna}]:'))
for l in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[l][coluna]:^5}]', end=' ')
        if matriz[l][coluna] % 2 ==0:
            spar += matriz[l][coluna]
    print()
print(f'A soma dos valores pares é {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma da  terceira coluna é {scol}')
for coluna in range(0,3):
    if coluna == 0:
        ss = matriz[1][coluna]
    elif matriz[1][coluna]>ss:
        ss = matriz[1][coluna]
print(f'O maior valor da coluna linha é {ss}.')


#Palpites para a Mega Sena
lista1 = list()
jogos = list()
cont = 0
quant = int(input('Quantos jogos você quer?:'))
totj = 1
while totj <= quant:
    cont = 0
    while True:
        n1 = randint(1,60)
        if n1 not in lista1:
            lista1.append(n1)
            cont += 1
        if cont >= 6:
            break
    lista1.sort()
    jogos.append(lista1[:])
    lista1.clear()
    totj += 1
    print(f'Os numero sorteados foram {lista1}.')
    
# Boletim com listas compostas
ficha = list()
while True:
    nome6 = str(input('Nome:'))
    nota5 = float(input('Nota1:'))
    nota4 = float(input('Nota2:'))
    media = (nota4 + nota5) / 2
    ficha.append([nome6 , [nota4 , nota5] , media])
    re = str(input('Quer continuar ? [S/N]: ')).strip().upper()
    if re in 'N':
        break
print(f'{"No.":<4}{"NOME6":<10}{"MEDIA":>8}')
for i , a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if opc == 999:
        print('Finalizado')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]}')
print('Volte sempre.')
