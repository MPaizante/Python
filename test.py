from operator import itemgetter
from random import randint
from time import sleep
jogo1 = {   'jogador1': randint(1 , 6),
            'jogador2': randint(1 , 6),
            'jogador3': randint(1 , 6),
            'jogador4': randint(1 , 6)
}
print(jogo1)
print('Valores sorteados:')
for ke , vi in jogo1.items():
    print(f'{ke} tirou {vi} no dado.')
    sleep(1)
ranking = sorted(jogo1.items(), key=itemgetter(1) )
