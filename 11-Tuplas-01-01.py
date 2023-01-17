lanche = ('Hamburguer' , 'Suco' , 'Pizza' , 'Pudim')
#Tuplas são imutaveis
print(lanche [1])
for comida in lanche:
    print(f'Vou comer {comida}.')
print('Comi bastante')
print(sorted(lanche))
a = (2 , 5 , 4)
b = (5 , 8, 1 ,2)
c = a + b
print(sorted(c))
print(c.count(2))#contar 
print(c.index(5))

pessoa = ('Gustavo' , 39 , 'M' , 99.88)
print(pessoa)