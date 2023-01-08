numi = int(input('Numero:'))
nums= str(numi)
peleu = numi // 1 % 10
peled = numi // 10 % 10
pelec = numi // 100 % 10
pelem = numi // 1000 % 10

print('Analisando um numero {}.'.format(numi))
print('Unidade: {}'.format(peleu))
print('Dezena: {}'.format(peled))
print('Centena: {}'.format(pelec))
print('Milhar: {}'.format(pelem))
