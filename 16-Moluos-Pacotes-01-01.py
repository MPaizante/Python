#Exercitando modulos em python

def aumentar(preço = 0 , taxa = 0):
    res = preço + (preço * (taxa/100))
    return res


def diminuir(preço  = 0, taxa = 0):
    res = preço - (preço * (taxa / 100))
    return res
    
def dobro(preço = 0):
    res = preço * 2
    return res

   
def metade(preço = 0 ):
    res = preço / 2 
    return res


def moeda( preço = 0 , moeda = 'R$'):
    return f'{moeda}{preço}'.replace('.' , '.')
    


p = float(input('Digite o preço:'))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}.')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}. ')
print(f'O aumento de 10% de {moeda(p)} é {moeda(aumentar(p , 10))}. ')
print(f'O desconto de 10% de {moeda(p)} é {moeda(diminuir(p , 10))}. ')
print(f'Reduzindo 13% de {moeda(p)}, temos {moeda(diminuir(p , 13))}')


#Formatando moeadas