total18 = 0
totalM = 0
totalF = 0
while True:
    i = int(input('Idade:'))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo:')).strip().upper()[0]
    if i >= 18:
        total18 += 1
    if s  == 'M':
        totalM += 1
    if s == 'F' and i < 20:
        totalF += 1               
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0] 
    else:
        print('.') 
         
    print('Acabou')
    print(totalM)
    print(totalF)    

# Estatisticas em produtos

