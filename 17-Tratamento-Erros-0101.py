try:
    a = int(input('NUmerador:'))
    b = int(input('Denominador:'))
    r = a/b
except: 
    print('Infelizmente deu ruim.')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre')