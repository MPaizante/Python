#Exercitando modulos em python

def aumentar(preço , taxa):
    res = preço + (preço * (taxa/100))
    return res


def diminuir(preço , taxa):
    res = preço - (preço * (taxa / 100))
    return res
    
def dobro(preço):
    res = preço * 2
    return res

   
def metade(preço):
    res = preço / 2 
    return res


p = float(input('Digite o preço:'))
print(f'A metade de {p} é {metade(p)}.')
print(f'O dobro de {p} é {dobro(p)}. ')
print(f'O aumento de 10% de {p} é {aumentar(p , 10)}. ')
print(f'O desconto de 10% de {p} é {diminuir(p , 10)}. ')