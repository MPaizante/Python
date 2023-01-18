#Listas podem ser mudadas 
XXXXXX = [8 , 5 ,7 ,1 ,2 ,3 ,4 , 0 ,6]
XXXXXX.sort(reverse=True)#organizar do maior para o menor e somento o sort fica do menor para o maior.
print(XXXXXX)



ttt = [2 , 5 , 9, 1]
ttt [2] = 3 #trocou o 5 pelo 2 
ttt.append(7) #vai add o 7
ttt.sort()
ttt.insert(2 , 0)
ttt.pop() #removeu o 2
ttt.remove(3) #ele vai remover o primeiro 3 que encontrar
if 5 in ttt:
    ttt.remove(5)
else: 
    print('N achei o num 5')
print(ttt)
print(f'Essa lista tem {len(ttt)} elementos.')




aaaaa = []
aaaaa.append(5)
aaaaa.append(9)
aaaaa.append(4)
for aaa , bbb in enumerate(aaaaa):
    print(f'Na posição {aaa} encontrei o valor {bbb}!')
print('Cheguei ao final da lista.')



cccccc = list()
for ccc in range(0,5):
    cccccc.append(int(input('Digite os valores:')))
for aaa , bbb in enumerate(cccccc):
    print(f'Na posição {aaa} encontrei o valor {bbb}!')
print('Cheguei ao final da lista.')

#Maior e Menor valores na lista
listanum = []
listmaior = 0
listmenor = 0
for c in range(0 , 5):
    listanum.append(int(input(f'Digite um valor para {c}:')))
    if c == 0:
        listmaior = listmenor = listanum[c]
    else:
        if listanum[c] > listmaior:
            listmaior = listanum[c]
        if listanum[c] < listmenor:
            listmenor = listanum
print(f'Valores que vc digitou {listanum}')
print(f'O maior valor foi {listmaior}')
print(f'O menor valor foi {listmenor} ')
    
    
#Valores unicos em lista
numeros = list()
while True:
    n = int(input('Digite um valor:'))
    r = str(input('Quer continuar ? [N/S]')).strip
    if r in 'N'