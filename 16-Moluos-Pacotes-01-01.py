#Exercitando modulos em python

def aumentar(preço = 0 , taxa = 0 , formato = False):
    res = preço + (preço * (taxa/100))
    return res if formato is False else moeda(res)


def diminuir(preço  = 0, taxa = 0 , formato = False):
    res = preço - (preço * (taxa / 100))
    return res if formato is False else moeda(res)
    
def dobro(preço = 0 , formato = False):
    res = preço * 2
    return res if not formato else moeda(res)

   
def metade(preço = 0  , formato = False):
    res = preço / 2 
    return res if not formato else moeda(res)


def moeda( preço = 0 , moeda = 'R$' , formato = False):
    return f'{moeda}{preço}'.replace('.' , '.')


def resumo(preço = 0, taxaa = 10, taxar = 5):
    print('-'*30)
    print('Resumo do Valor'.center(30))
    print('-'*30)
    print(f'Preço analisado: {moeda(preço)}')
    print(f'Dobro do preço:{dobro(preço, True)} ')
    print(f'Metade do preço:{metade(preço, True)} ')
    print('-'*30)
    


p = float(input('Digite o preço:'))
moeda.resumo(p)
print(f'A metade de {moeda(p)} é {moeda(metade(p))}.')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}. ')
print(f'O aumento de 10% de {moeda(p)} é {moeda(aumentar(p , 10))}. ')
print(f'O desconto de 10% de {moeda(p)} é {moeda(diminuir(p , 10))}. ')
print(f'Reduzindo 13% de {moeda(p)}, temos {moeda(diminuir(p , 13))}')

moeda.resumo(p)


