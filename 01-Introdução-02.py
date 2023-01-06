n1 = int(input('Numero:'))
n2 = int(input('Numero:'))
s = n1 + n2
print('A soma foi ', s)

m1 = float(input('Carro:'))
m2 = float(input('Carro:'))
c = m1 + m2 
#print('A soma entre', m1,'e',m2,'foi de',c) forma antiga
print('A soma entre {} e {} foi de {}'.format(m1 ,m2 ,c))#forma nova ou pode botar {0} {1} {2}

p = input('Digite algo:')
print('O tipo primitivo desse valor é', type(p))
print('Só tem espços?', p.isspace())
print('É um numero?', p.isnumeric())
print('É alfabetico?', p.isalpha())
print('É alfanumerico?', p.isalnum())
print('É maiuscula?', p.isupper())
print('É minuscula?', p.islower())
print('Está captalizado?', p.istitle())
