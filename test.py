listanum = []
listmaior = 0
listmenor = 0
for c in range(0 , 5):
    listanum.append(int(input(f'Digite um valor para {c}: ')))
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