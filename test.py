numst = 0
contnum = 0
somanum = 0
numst = int(input('Digite um numero. Para parar digite 999.'))
while numst != 999:   
    somanum += numst
    contnum += 1
    numst = int(input('Digite um numero. Para parar digite 999.'))
print('Voce digitou {} numeros e a soma é {}.'.format(contnum , somanum ))
print('Acabou')



