from random import randint



def sorteia(lista):
    print('Sorteando 5 valores de lista:')
    for ct in range(0, 5):
        nt = randint(1,10)
        lista.append(nt)
        print(f'{nt}', end=' ', flush=True)
    print('pronto')
    
 
def somaPar(lista):   
    ssoma = 0
    for vvalor in lista:
        if vvalor % 2 == 0:
            ssoma += vvalor
    print(f'Somando os valores par de {lista}, temos {ssoma}.')
    
    
nnumeros = list()
sorteia(nnumeros)
print(nnumeros)
somaPar(nnumeros)