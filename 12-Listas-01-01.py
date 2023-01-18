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
    if n not in numeros:
        numeros.append(n)
        print('Valor add com sucesso.')
    else:
        print('Valor duplicado')
    r = str(input('Quer continuar ? [N/S]')).strip().upper()
    if r in 'N':
        break
print('Acabou')
print(f'Voce digitou os valores [{numeros}]')
print(numeros.sort())


#Lista ordenada sem repetições
lista = []
for contador in range (0 , 5):
    vari = int(input('Digite um valor:'))
    if contador == 0 or vari > lista[-1]:
        lista.append(vari)
    #elif n > lista[len(lista)-1]: #pegar o ultimo valor ou pode botar lista[-1]:
        #lista.append(vari)
    else:
        pos = 0
        while pos < len(lista):
            if vari <= lista[pos]:
                lista.insert(pos , vari)
                break
            pos += 1
print(f'Os valores digitados foram {lista}')
print('Fim.........................................')



#Extraindo dados de uma lista
v1 = []
while True:
    v1.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar ? [S/N] '))
    if resp in 'Nn':
        break
print(f'Você digitou {len(v1)} elementos.')
v1.sort(reverse=True)
print(f'Os valores de ordem descrecentes {v1}')
if 5 in v1:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 n foi encontrado na lista.')


#Dividindo valores em varias listas
n3 = list()
par = list()
impar = list()
while True:
    n3.append(int(input('Digite um numero: ')))
    res = str(input('Quer continuar? [S/N] '))
    if res in 'Nn':
        break
for i , v in enumerate(n3):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista compelta é {n3}')
print(f'A lista de par é {par}')
print(f'A lista de impar é {impar}')

#Validando expressões matematicas
expr = str(input('Digite uma expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão está errada.')