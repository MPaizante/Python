from math import factorial

print('Gerador de PA')
print('=-'*10)
primeiro1 = int(input('Primeiro termo:'))
razão1 = int(input('Razão:'))
termo1 = primeiro1
cont1 = 1
fimtermo = int(input('Digite quantos termos:'))
while cont1 <= fimtermo:
    print('{}'.format(termo1), end=' ')
    termo1 += razão1
    cont1 += 1
print('Fim')

