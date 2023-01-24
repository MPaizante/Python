c1 =('\033[m'
     '\033[0;30;41m');


def ajuda(com):
    help(com)
    
    
def titulo1(msg, cor=0):
    tam = len(msg)+4
    print(c1[cor], end=' ')
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)
    print(c1[0] , end='')


comando = ''
while True:
    titulo1('Sistema de Ajuda')
    comando = str(input("função ou biblioteca"))
    if comando.upper() == 'Fim':
        break
    else:
        ajuda(comando)
titulo1('Até logo!')