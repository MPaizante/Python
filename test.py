maiorp = 0
menorp = 0
for pesoq in range(1 , 6):
    peso1 = float(input('Digite o {}ª peso:'.format(pesoq)))
    if pesoq == 1:
        maiorp = peso1
        menorp = peso1
    else:
        if peso1 > maiorp:
            maiorp = peso1
        if peso1 < menorp:
            menorp = peso1
print('O maior foi {} kg.'.format(maiorp))
print('O menor peso foi {} kg'.format(menorp))
