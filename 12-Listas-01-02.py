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
        
