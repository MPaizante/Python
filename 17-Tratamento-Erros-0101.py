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


#Criando um menu
