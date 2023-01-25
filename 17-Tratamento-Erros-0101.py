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