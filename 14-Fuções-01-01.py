#Função que calcula area
def area(larg , comp):
    a = larg * comp
    print(f'Area do terreno é {a}m².')
    
    
print('Controle de terrenos')
print('-'*20)
l = float(input('Largura(m):'))
c = float(input('Comprimento(m):'))
area(l , c)


#Um print especial.
def escreva(msg):
    tam = len(msg)+4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    
    
escreva('Matheus Paizante de Araujo')  
escreva('Curso PYTHON')
escreva('Github')

#Função contador
from time import sleep
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