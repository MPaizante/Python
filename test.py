velocidade = float(input('Qual velocidade do carro?'))
multa = (velocidade-80) * 7
if velocidade > 80:
    print('Multado!')
    multa = (velocidade-80) * 7
    print('Vc vai pagar {:.2f}R$'.format(multa))
    print('dirija com segurança')
else:
    print('Tenha um bom dia.')