#Função para votação
from datetime import date
def voto(ano):
    atual = date.today().year  
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos não vota.  '
    elif 16 <= idade <= 18 or idade > 65:
        return f'Voto opcional'
    else:
        return f'Com {idade} anos o voto é obrigatorio'


nasc = int(input('Em que ano nasceu?:'))
print(voto(nasc))
mes = date.today().month 

#função para fatorial
def fatorial (n ,show=False):
    f = 1
    for c in range(n , 0 , -1):
        if show:
            print(c , end='')
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
    
    
print(fatorial(5 , show=True))


#Ficha do Jogador

def ficha (jog = '<Desconhecido>', gol = 0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.' )



nome = str(input('Nome do jogador:'))
gols = str(input('Numero de gols:'))
if gols.isnumeric():
    gols = int(gols)
else:
    gols= 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome , gols)
    
def leiaInt(msg):
    ok = False
    v1 = 0
    while True:
        n1 = str(input(msg))
        if n1.isnumeric():
            v1 = int(n1)
            ok = True
        else:
            print('\033[0;31mErro! Digite novamente.\033[m')
        if ok:
            break
    return v1


n1 = leiaInt('Digite um numero:')
print(f'Voce acabou de digitar o numero {n1}')

#Analisando e gerando dicionarios

def notas (*n3, sit=False):
    r1 = dict()
    r1['total'] = len(n3)
    r1['maior'] = max(n3)
    r1['menor'] = min(n3)
    r1['media'] = sum(n3)/len(n3)
    if sit:
        if r1['media'] > 7:
            r1['situação'] = 'boa'
        elif r1['media'] >=5:
            r1['situação'] = 'razoavel'
        else:
            r1['situação'] = 'rui,'
    return r1

resp1 = notas (5.5 , 2.5 , 9 , 8.5, sit=True)
print(resp1)

#Interatividade helping system in python
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
