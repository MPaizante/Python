d = float(input('Qual distancia?'))
print('Você está preste a começar uma viagem de {}Km'.format(d))
if d <= 200:
    pre1 = d * 0.50
    print('O preço vai ser R${:.2f}'.format(pre1))
    
else:
    pre = d * 0.45
    print('O preço vai ser R${:.2f}'.format(pre))