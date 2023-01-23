from time import sleep
#Um print especial.

def cont(i , f , p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}. ')
    sleep(1)
    
    
    if i < f:
        co = i
        while co <=f:
            print(f'{co}', end=' ', flush=True)
            sleep(0.5)
            co += p
        print('Fim')
    else:
        co = i
        while co >=f:
            print(f'{co}  ', end=' ', flush=True)
            sleep(0.5)
            co -= p
        print('Fim')       
        
        
cont(1 , 10 , 1)
cont(10 , 0 , 2)
ini = int(input('Inicio:'))
fim = int(input('Fim:'))
pas = int(input('Passo:'))
cont(ini , fim , pas)