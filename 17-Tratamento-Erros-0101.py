try:
    a = int(input('NUmerador:'))
    b = int(input('Denominador:'))
    r = a/b
except Exception as erro: 
    print(f'Infelizmente deu ruim {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre')
    
    
#Funções aprofundadas python
def leiaint(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError , TypeError) :
            print('\033[31mErro: digte um numero inteiro valido.')
            continue
        except (KeyboardInterrupt):
            print('\n\033Entrada de dados interrompida pelo usuario')
            return 0
        else:
            return n1


num = leiaint('Digite um valor:')
print(f'O valor foi {num}')




#Site está acessivel? 
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/watch?v=_uvfRuHN6yM')
except urllib.error.URLError : 
    print('Deu erro')
else:
    print('Tudo Ok')
    #print(site.read())


#Criando um menu 115a
from time import sleep

def linha(tam = 42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    
    
def leiaint(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError , TypeError) :
            print('\033[31mErro: digte um numero inteiro valido.')
            continue
        except (KeyboardInterrupt):
            print('\n\033Entrada de dados interrompida pelo usuario')
            return 0
        else:
            return n1
        
    
def menu(lista):
    cabecalho('Menu Principal')
    c = 1 
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc = leiaint('Sua Opção:')
    
    
    
    
#from import ex115.tib.interface import*

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas' , ' Sair do Sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do Sistema')
        break
    else:
        print('ERRO!')
    sleep(0.5)


#Criando um menu 115b