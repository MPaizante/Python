num = [[] , []]
valor = 0
for y in range(1,8):
    valor = int(input('Digite um valor:'))
    if valor % 2 ==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Todos os valores foram {valor}')
print(num)