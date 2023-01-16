from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor:'))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in  'PpIi':
        tipo = str(input('Par ou impar.')).strip().lower()[0]
    print(f'Vc jogou {jogador} e o computador {computador}. total de  {total} ')
    if tipo == 'Pp':
        if total % 2 == 0:
            print('Venceu')
            v += 1
        else:
            print('Pedeu')
            break
    elif tipo == 'Ii':
        if total % 2 == 1:
            print('Veceu')
            break
        else:
            print('Perdeu')
            break
    print('Vamos jogar novamente...')
print(f'Game over! Voce venceu {v} vezes.')

