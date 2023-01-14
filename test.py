Nprimo = int(input('Digite um numero:'))
for primo in range(1 , Nprimo + 1):
    if Nprimo % primo == 0:
        print('\033[34m' , end='')
    else:
        print('\033[m', end='')
    print('{}'.format(primo), end='')