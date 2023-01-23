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